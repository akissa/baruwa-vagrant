#!/usr/bin/env bash
#
[ `grep 'distroverpkg=baruwa-release' /etc/yum.conf` ] || {
    sed -i 's:distroverpkg=centos-release:distroverpkg=baruwa-release:' /etc/yum.conf
    sed -i 's|http://bugs.centos.org/set_project.php?project_id=19&ref=http://bugs.centos.org/bug_report_page.php?category=yum|http://www.baruwa.com|' /etc/yum.conf
}
cat << 'EOF' > /etc/rsyslog.d/ratelimit.conf
$SystemLogRateLimitInterval 0
$SystemLogRateLimitBurst 0
$IMUxSockRateLimitBurst 0
$IMUXSockRateLimitInterval 0
$IMUxSockRateLimitSeverity 7
EOF
service rsyslog restart
