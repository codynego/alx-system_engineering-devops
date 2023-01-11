# File resource to create/update a file at /tmp/school

file {'/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  centent => 'I love Puppet'
}
