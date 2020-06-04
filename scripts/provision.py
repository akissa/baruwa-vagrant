#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
# rovision.py: Vagrant shell provision script for Baruwa Enterprise Edition
# Copyright (C) 2015  Andrew Colin Kissa <andrew@topdog.za.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
provision.py: Vagrant shell provision script for Baruwa Enterprise Edition

Copyright 2015, Andrew Colin Kissa
Licensed under AGPLv3+
"""
import os
import sys
sys.path.append("/usr/share/rhn/")
try:
    from up2date_client import rhnreg
    HAVE_RHNREG = True
except ImportError:
    HAVE_RHNREG = False


BARUWA_NET_URL = 'https://bn.baruwa.com/XMLRPC'
PROFILES = [
    'backend', 'cache', 'indexer', 'mail', 'mq',
    'node', 'web', 'standalone', 'db'
]


def is_registered():
    """check if the system is registered"""
    if HAVE_RHNREG is False:
        return False
    rhnreg.cfg.set("serverURL", BARUWA_NET_URL)
    return rhnreg.registered()


def main():
    """Provision the VPS"""
    if not is_registered():
        dhost = 'https://baruwa.com/downloads/requirements/'
        pkgs_to_rm = [
            'iscsi-initiator-utils',
            'device-mapper-multipath-libs',
            'fuse',
            'device-mapper-multipath',
            'ntp',
            'audit-libs-python',
        ]
        pkgs_to_download = [
            'baruwa-release-6-9.el6.12.4.noarch.rpm',
            'dbus-python-0.83.0-6.1.el6.x86_64.rpm',
            'python-dmidecode-3.10.15-1.el6_9.x86_64.rpm',
            'python-ethtool-0.6-6.el6_9.x86_64.rpm',
            'python-gudev-147.1-4.el6_0.1.x86_64.rpm',
            'python-hwdata-1.7.3-1.el6.noarch.rpm',
            'rhn-check-1.9.10-3.el6.noarch.rpm',
            'rhn-client-tools-1.9.10-3.el6.noarch.rpm',
            'rhn-setup-1.9.10-3.el6.noarch.rpm',
            'rhnlib-2.5.55-2.el6.noarch.rpm',
            'rhnsd-5.0.9-2.el6.x86_64.rpm',
            'yum-rhn-plugin-1.9.4-3.el6.noarch.rpm',
            'm2crypto-0.20.2-9.el6.x86_64.rpm',
            'libxml2-python-2.7.6-21.el6_8.1.x86_64.rpm',
            'pyOpenSSL-0.13.1-2.el6.x86_64.rpm',
            'libgudev1-147-2.73.el6_8.2.x86_64.rpm',
            'pygobject2-2.20.0-5.el6.x86_64.rpm',
            'libnl-1.1.4-2.el6.x86_64.rpm',
        ]
        pkgs_to_install = [
            'baruwa-setup',
            'exim',
            'python-backports-ssl_match_hostname',
            'baruwa-utils',
        ]
        argc = len(sys.argv)
        if argc >= 3:
            profile = sys.argv[1]
            activation_key = sys.argv[2]
        elif argc == 2:
            profile = 'standalone'
            activation_key = sys.argv[1]
        else:
            raise ValueError('Incorrect Params provided')
        if profile not in PROFILES:
            profile = 'standalone'
        if profile in ['web', 'node', 'standalone']:
            pkgs_to_install.append('nginx')
            pkgs_to_install.append('baruwa-common')
        if profile in ['standalone', 'db', 'backend']:
            pkgs_to_install.append('pgbouncer')
            pkgs_to_install.append('postgresql-server')
            pkgs_to_install.append('rabbitmq-server')
        if profile in ['mq']:
            pkgs_to_install.append('rabbitmq-server')
        if profile in ['mail']:
            pkgs_to_install.append('baruwa-common')
            pkgs_to_install.append('spamassassin')
        if profile in ['node']:
            pkgs_to_install.append('spamassassin')
        cmd = "rhnreg_ks --serverUrl=%s --activationkey=%s" % \
            (BARUWA_NET_URL, activation_key)
        for pkg in pkgs_to_download:
            os.system("curl -sO %s%s" % (dhost, pkg))
        os.system("yum localinstall *.rpm -y")
        os.system(cmd)
        for pkg in pkgs_to_rm:
            os.system("yum erase %s -y" % pkg)
        os.system("rm -rf *.rpm")
        files_to_rm = [
            '/etc/yum.repos.d/epel.repo',
            '/etc/yum.repos.d/epel-testing.repo',
            '/etc/yum.repos.d/CentOS-Base.repo.rpmsave'
            '/etc/yum.repos.d/CentOS-Base.repo']
        for filename in files_to_rm:
            if os.path.exists(filename):
                print "Unlinking repo file: %s" % filename
                os.unlink(filename)
        os.system(
            "rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-BARUWA-6"
        )
        for pkg in pkgs_to_install:
            print "Installing bootstrap package %s" % pkg
            os.system("yum install %s -y" % pkg)
    else:
        print "The system is already registered"


if __name__ == '__main__':
    main()
