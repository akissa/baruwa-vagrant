# Baruwa Enterprise Edition Vagrant Setup

Sets up and converts a CentOS 6 VPS to Baruwa Enterprise Edition.
Currently the following providers are supported.

* DigitalOcean

## Requirements

* Vagrant
* Vagrant DigitalOcean provider

## Configuration

Configuration is by use of environment variables. The following
variables are required.

* DIGITAL_OCEAN_TOKEN
* BARUWA_ACTIVATION_KEY

The following variables are optional.

* DIGITAL_OCEAN_HOSTNAME - defaults to baruwa.home.topdog-software.com
* DIGITAL_OCEAN_REGION - defaults to Frankfurt 1
* DIGITAL_OCEAN_SIZE - defaults to 4GB

## SSH Keys

Generate an SSH key pair for use by the plugin.

    ssh-keygen -t rsa -b 4096 -f ~/.ssh/digital_ocean_rsa

## Run

After generating the ssh key pair, you should run the following
command to setup the VPS.

    export DIGITAL_OCEAN_TOKEN="digitalocean token" BARUWA_ACTIVATION_KEY="key"
    vagrant up --provider=digital_ocean

After the VPS has been setup you can login and proceed with
configuration.

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
