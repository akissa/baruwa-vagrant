# -*- mode: ruby -*-
# vi: set ft=ruby :

host="baruwa.home.topdog-software.com"
Vagrant.configure(2) do |config|
  if ENV["DIGITAL_OCEAN_HOSTNAME"]
      config.vm.hostname = ENV["DIGITAL_OCEAN_HOSTNAME"]
  else
      config.vm.hostname = host
  end
  config.vm.box = "digital_ocean"
  config.ssh.private_key_path = "~/.ssh/digital_ocean_rsa"
  config.vm.provider :digital_ocean do |provider|
      provider.client_id = ENV["DIGITAL_OCEAN_CLIENT_ID"]
      provider.api_key = ENV["DIGITAL_OCEAN_API_KEY"]
      provider.image = "centos-6-5-x64"
      if ENV["DIGITAL_OCEAN_REGION"]
          provider.region = ENV["DIGITAL_OCEAN_REGION"]
      else
          provider.region = "fra1"
      end
      if ENV["DIGITAL_OCEAN_SIZE"]
          provider.size = ENV["DIGITAL_OCEAN_SIZE"]
      else
          provider.size = "4gb"
      end
  end
end
