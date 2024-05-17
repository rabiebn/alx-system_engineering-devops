# increasing fd limit for the user holberton

exec {"/usr/bin/env sed -i -r 's/holberton hard nofile [0-9]*/holberton hard nofile 1000/' /etc/security/limits.conf":}
exec {"/usr/bin/env sed -i -r 's/holberton soft nofile [0-9]*/holberton soft nofile 1000/' /etc/security/limits.conf":}
