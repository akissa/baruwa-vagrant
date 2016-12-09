#!/usr/bin/env bash
#
[ `grep 'distroverpkg=baruwa-release' /etc/yum.conf` ] || {
    sed -i 's:distroverpkg=centos-release:distroverpkg=baruwa-release:' /etc/yum.conf
    sed -i 's|http://bugs.centos.org/set_project.php?project_id=19&ref=http://bugs.centos.org/bug_report_page.php?category=yum|http://www.baruwa.com|' /etc/yum.conf
}
/usr/bin/test -e /etc/rsyslog.d/ratelimit.conf || {
cat << 'EOF' > /etc/rsyslog.d/ratelimit.conf
$SystemLogRateLimitInterval 0
$SystemLogRateLimitBurst 0
$IMUxSockRateLimitBurst 0
$IMUXSockRateLimitInterval 0
$IMUxSockRateLimitSeverity 7
EOF
service rsyslog restart
}
if [ -e /etc/yum.repos.d/CentOS-Base.repo ]; then
    [ `grep 'mirrors.kernel.org' /etc/yum.repos.d/CentOS-Base.repo` ] || {
        unalias cp 2>/dev/null || /bin/true
        cp -f /vagrant/scripts/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo
    }
fi
if grep -Fxq '127.0.0.1 guest' /etc/hosts; then
cat << 'EOF' > /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
EOF
fi
[ `grep '# Initial configuration by baruwa-vagrant' /etc/sysconfig/iptables` ] || {
case "$1" in
    "backend")
        cat /vagrant/scripts/files/backend > /etc/sysconfig/iptables
        touch /etc/baruwa/acme.disable
        ;;
    "cache")
        cat /vagrant/scripts/files/cache > /etc/sysconfig/iptables
        touch /etc/baruwa/acme.disable
        ;;
    "indexer")
        cat /vagrant/scripts/files/indexer > /etc/sysconfig/iptables
        touch /etc/baruwa/acme.disable
        ;;
    "mail")
        cat /vagrant/scripts/files/mail > /etc/sysconfig/iptables
        touch /etc/baruwa/acme.disable
        ;;
    "mq")
        cat /vagrant/scripts/files/mq > /etc/sysconfig/iptables
        touch /etc/baruwa/acme.disable
        ;;
    "node")
        cat /vagrant/scripts/files/node > /etc/sysconfig/iptables
        touch /etc/baruwa/acme.disable
        ;;
    "web")
        cat /vagrant/scripts/files/web > /etc/sysconfig/iptables
        touch /etc/baruwa/acme.disable
        ;;
    *)
        cat /vagrant/scripts/files/standalone > /etc/sysconfig/iptables
        ;;
esac
service iptables restart
chkconfig iptables on
if [ "$2" != "" ]; then
    hostname "$2"
    if [ "$?" = "0" ]; then
        export HOSTNAME="$2"
    fi
fi
}
if grep -Fxq 'HOSTNAME=vultr.guest' /etc/sysconfig/network; then
    sed -ie "s/^HOSTNAME=.*$/HOSTNAME=$(hostname)/" /etc/sysconfig/network
    if ! grep -Fxq 'PEERDNS=no' /etc/sysconfig/network-scripts/ifcfg-eth0; then
        echo 'PEERDNS=no' >> /etc/sysconfig/network-scripts/ifcfg-eth0
        echo 'make_resolv_conf(){:}' >> /etc/dhclient-enter-hooks
    fi
fi
