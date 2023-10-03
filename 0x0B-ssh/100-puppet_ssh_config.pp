# Set up server configuration with puppet
file_line{'Set alias name':
  path => '/etc/ssh/ssh_config',
  line => 'Host 34.207.57.188
    HostName 34.207.57.188
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
