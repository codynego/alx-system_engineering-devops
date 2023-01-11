#'''
# This class configures the SSH client to use the private key located at 
# ~/.ssh/school, and to refuse to authenticate using a password
#'''
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

