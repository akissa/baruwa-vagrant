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

* DIGITAL_OCEAN_HOSTNAME
* DIGITAL_OCEAN_CLIENT_ID
* DIGITAL_OCEAN_API_KEY
* DIGITAL_OCEAN_REGION
* DIGITAL_OCEAN_SIZE

## Run

After configuration you should run the following command to setup
the VPS.

    vagrant up --provider=digital_ocean


 ## Configuration

 After the VPS has been setup and converted you can now run baruwa-setup
 to complete configuration.
