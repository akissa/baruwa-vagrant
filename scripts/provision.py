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
        ]
        pkgs_to_download = [
            'baruwa-release-6-7.el6.12.4.noarch.rpm',
            'dbus-python-0.83.0-6.1.el6.x86_64.rpm',
            'python-dmidecode-3.10.13-3.el6_4.x86_64.rpm',
            'python-ethtool-0.6-5.el6.x86_64.rpm',
            'python-gudev-147.1-4.el6_0.1.x86_64.rpm',
            'python-hwdata-1.7.3-1.el6.noarch.rpm',
            'rhn-check-1.9.10-2.el6.noarch.rpm',
            'rhn-client-tools-1.9.10-2.el6.noarch.rpm',
            'rhn-setup-1.9.10-2.el6.noarch.rpm',
            'rhnlib-2.5.55-2.el6.noarch.rpm',
            'rhnsd-5.0.9-2.el6.x86_64.rpm',
            'yum-rhn-plugin-1.9.4-2.el6.noarch.rpm',
        ]
        activation_key = sys.argv[1]
        cmd = "rhnreg_ks --serverUrl=%s --activationkey=%s" % \
            (BARUWA_NET_URL, activation_key)
        for pkg in pkgs_to_download:
            os.system("curl -sO %s%s" % (dhost, pkg))
        os.system("yum localinstall *.rpm -y")
        os.system(cmd)
        for pkg in pkgs_to_rm:
            os.system("yum erase %s -y" % pkg)
        os.system(
            "rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-BARUWA-6"
        )
        os.system("yum install baruwa-setup -y")
        os.system("rm -rf *.rpm")
    else:
        print "The system is already registered"


if __name__ == '__main__':
    main()
