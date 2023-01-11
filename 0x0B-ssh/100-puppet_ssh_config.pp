# set up your client SSH configuration file so that you can connect to a server without typing a password

class ssh_config {
    file { '~/.ssh/config':
        ensure  => file,
        mode    => '0600',
        owner   => 'root',
        group   => 'root',
        content => "Host *
          IdentityFile ~/.ssh/school
          PubkeyAuthentication yes
          PasswordAuthentication no"
    }
}

