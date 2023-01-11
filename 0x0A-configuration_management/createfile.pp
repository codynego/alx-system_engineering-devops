file {'/home/nego/newerfile':
  ensure => file,
  mode   => '0744',
  owner  => 'nego',
  group  => 'nego',
  content => 'i love puppet',
}
