# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.ssh.insert_key = true

  config.vm.provider :rimu do |provider, override|
    override.ssh.private_key_path = '~/.ssh/rimuhosting_rsa'
    provider.api_key = ENV['RIMUHOSTING_APIKEY']
    provider.host_name = ENV['BARUWA_HOSTNAME']
    provider.distro_code = 'centos6.64'
    override.nfs.functional = false
    if ENV['RIMUHOSTING_REGION']
      provider.data_centre = ENV['RIMUHOSTING_REGION']
    else
      provider.data_centre = 'DCDALLAS'
    end
    if ENV['RIMUHOSTING_SIZE']
      provider.memory_mb = ENV['RIMUHOSTING_SIZE']
    else
      provider.memory_mb = 8192
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
    override.nfs.functional = false
    override.vm.allowed_synced_folder_types = :rsync
    if ENV['BARUWA_HOSTNAME']
      override.vm.hostname = ENV['BARUWA_HOSTNAME']
    else
      override.vm.hostname = 'baruwa.home.topdog-software.com'
    end
    provider.token = ENV['DIGITAL_OCEAN_TOKEN']
    provider.image = 'centos-6-x64'
    if ENV['DIGITAL_OCEAN_REGION']
      provider.region = ENV['DIGITAL_OCEAN_REGION']
    else
      provider.region = 'fra1'
    end
    if ENV['DIGITAL_OCEAN_SIZE']
      provider.size = ENV['DIGITAL_OCEAN_SIZE']
    else
      provider.size = '8gb'
    end
  end

  config.vm.provider :linode do |provider, override|
    override.ssh.private_key_path = '~/.ssh/linode_rsa'
    override.nfs.functional = false
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
      provider.plan = '8192'
    end
    if ENV['LINODE_LABEL']
      provider.label = ENV['LINODE_LABEL']
    else
      provider.label = 'baruwa-enterprise-edition-vagrant'
    end
  end

  config.vm.provider :vultr do |provider, override|
    override.ssh.private_key_path = '~/.ssh/vultr_rsa'
    override.nfs.functional = false
    override.vm.box = 'vultr'
    override.vm.box_url = 'https://github.com/p0deje/vagrant-vultr/raw/master/box/vultr.box'
    provider.token = ENV['VULTR_TOKEN']
    provider.os = 'CentOS 6 x64'
    if ENV['VULTR_REGION']
      provider.region = ENV['VULTR_REGION']
    else
      provider.region = 'Frankfurt'
    end
    if ENV['VULTR_SIZE']
      provider.plan = ENV['VULTR_SIZE']
    else
      provider.plan = '4096 MB RAM,60 GB SSD,3.00 TB BW'
    end
  end

  config.vm.provision 'shell' do |s2|
    s2.path = 'scripts/bootstrap.sh'
    s2.args = [ENV['BARUWA_PROFILE'], ENV['BARUWA_HOSTNAME']]
  end

  config.vm.provision 'shell' do |s|
    s.path = 'scripts/provision.py'
    s.args = [ENV['BARUWA_PROFILE'], ENV['BARUWA_ACTIVATION_KEY']]
  end
end
