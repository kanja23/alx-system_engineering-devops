# Install Nginx
class { 'nginx':
  ensure => installed,
}

# Define a custom fact for retrieving the hostname
Facter.add('nginx_hostname') do
  setcode do
    Facter::Core::Execution.execute('hostname')
  end
end

# Configure Nginx with custom HTTP header
file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => file,
  content => "add_header X-Served-By $::nginx_hostname;",
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Class['nginx'],
}
