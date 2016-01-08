# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.ssh.insert_key = true

  config.vm.provider :rimu do |provider, override|
    override.ssh.private_key_path = '~/.ssh/rimuhosting_rsa'
    provider.api_key = ENV['RIMUHOSTING_APIKEY']
    provider.host_name = ENV['RIMUHOSTING_HOSTNAME']
    provider.distro_code = 'centos6.64'
    if ENV['RIMUHOSTING_REGION']
      provider.data_centre = ENV['RIMUHOSTING_REGION']
    else
      provider.data_centre = 'DCDALLAS'
    end
    if ENV['RIMUHOSTING_SIZE']
      provider.memory_mb = ENV['RIMUHOSTING_SIZE']
    else
      provider.memory_mb = 4096
    end
    if ENV['RIMUHOSTING_DISK1']
      provider.disk_space_mb = ENV['RIMUHOSTING_DISK1']
    else
      provider.disk_space_mb = 20000
    end
  end

  config.vm.provider :digital_ocean do |provider, override|
    override.vm.box = 'digital_ocean'
    override.ssh.private_key_path = '~/.ssh/digital_ocean_rsa'
    if ENV['DIGITAL_OCEAN_HOSTNAME']
      override.vm.hostname = ENV['DIGITAL_OCEAN_HOSTNAME']
    else
      override.vm.hostname = 'baruwa.home.topdog-software.com'
    end
    provider.token = ENV['DIGITAL_OCEAN_TOKEN']
    provider.image = 'centos-6-5-x64'
    if ENV['DIGITAL_OCEAN_REGION']
      provider.region = ENV['DIGITAL_OCEAN_REGION']
    else
      provider.region = 'fra1'
    end
    if ENV['DIGITAL_OCEAN_SIZE']
      provider.size = ENV['DIGITAL_OCEAN_SIZE']
    else
      provider.size = '4gb'
    end
  end

  config.vm.provider :linode do |provider, override|
    override.ssh.private_key_path = '~/.ssh/linode_rsa'
    override.vm.box = 'linode'
    override.vm.box_url = 'https://github.com/displague/vagrant-linode/raw/master/box/linode.box'
    provider.token = ENV['LINODE_TOKEN']
    provider.distribution = 'CentOS 6.5'
    if ENV['LINODE_REGION']
      provider.datacenter = ENV['LINODE_REGION']
    else
      provider.datacenter = 'frankfurt'
    end
    if ENV['LINODE_SIZE']
      provider.plan = ENV['LINODE_SIZE']
    else
      provider.plan = '4096'
    end
    if ENV['LINODE_LABEL']
      provider.label = ENV['LINODE_LABEL']
    else
      provider.label = 'baruwa-enterprise-edition-vagrant'
    end
  end

  config.vm.provision 'shell' do |s2|
    s2.path = 'scripts/syslog.sh'
  end

  config.vm.provision 'shell' do |s|
    s.path = 'scripts/provision.py'
    s.args = [ENV['BARUWA_ACTIVATION_KEY']]
  end
end
