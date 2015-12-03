# Baruwa Enterprise Edition Vagrant Setup

Sets up and converts a CentOS 6 VPS to Baruwa Enterprise Edition in the cloud.
Currently the following providers are supported.

* [Rimuhosting](http://rimuhosting.com/?r=41325919050882007081895014642231402396)
* [DigitalOcean](https://www.digitalocean.com/?refcode=2e62b2989fc4)
* [Linode](https://www.linode.com/?r=f3c4f62f65cc04d7542d57c077ebf83df1962d8a)

## Requirements

* [Vagrant](https://www.vagrantup.com/)

One of the following providers

* [Vagrant Rimu provider](https://github.com/akissa/vagrant-rimu)
* [Vagrant DigitalOcean provider](https://github.com/smdahlen/vagrant-digitalocean)
* [Vagrant Linode provider](https://github.com/displague/vagrant-linode)

## Installation

You need to install Vagrant and one of the provider plugins above.
You should then clone this repo to your machine.

    git clone https://github.com/akissa/baruwa-vagrant.git
    cd baruwa-vagrant

## Configuration

Configuration is by use of environment variables.

## Rimuhosting

The following variables are required.

* RIMUHOSTING_APIKEY
* RIMUHOSTING_HOSTNAME
* BARUWA_ACTIVATION_KEY

The following variables are optional.

* RIMUHOSTING_DISK1 - defaults to 20GB
* RIMUHOSTING_REGION - defaults to DCDALLAS, the Dallas DC
* RIMUHOSTING_SIZE - defaults to 4GB

## DigitalOcean

The following variables are required.

* DIGITAL_OCEAN_TOKEN
* BARUWA_ACTIVATION_KEY

The following variables are optional.

* DIGITAL_OCEAN_HOSTNAME - defaults to baruwa.home.topdog-software.com
* DIGITAL_OCEAN_REGION - defaults to Frankfurt 1
* DIGITAL_OCEAN_SIZE - defaults to 4GB

## Linode

The following variables are required.

* LINODE_TOKEN
* BARUWA_ACTIVATION_KEY

The following variables are optional.

* LINODE_REGION - defaults to frankfurt
* LINODE_SIZE - defaults to 4096
* LINODE_LABEL - defaults to baruwa-enterprise-edition-vagrant

## SSH Keys

Generate an SSH key pair for use by the plugin.

## Rimuhosting

    ssh-keygen -t rsa -b 4096 -f ~/.ssh/rimuhosting_rsa

## DigitalOcean

    ssh-keygen -t rsa -b 4096 -f ~/.ssh/digital_ocean_rsa

## Linode

    ssh-keygen -t rsa -b 4096 -f ~/.ssh/linode_rsa

## Run

After generating the ssh key pair, you should run the following
command to setup the VPS.

## Rimuhosting

    export RIMUHOSTING_APIKEY="rimuhosting apikey" RIMUHOSTING_HOSTNAME="fqdn hostname" BARUWA_ACTIVATION_KEY="key"
    vagrant up --provider=rimu

## DigitalOcean

    export DIGITAL_OCEAN_TOKEN="digitalocean token" BARUWA_ACTIVATION_KEY="key"
    vagrant up --provider=digital_ocean

## Linode

    export LINODE_TOKEN="linode token" BARUWA_ACTIVATION_KEY="key"
    vagrant up --provider=linode

After the VPS has been setup you can login and proceed with
configuration.

    vagrant ssh

## Configuration

After the VPS has been setup and converted you can now run baruwa-setup
to complete configuration.

## Contributing

1. Fork it (https://github.com/akissa/baruwa-vagrant/fork)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request


## License

All code is licensed under the
[AGPLv3+ License](https://github.com/akissa/baruwa-vagrant/blob/master/LICENSE).
