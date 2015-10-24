VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.network "forwarded_port", guest: 3306, host: 3306
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "ansible/vagrant.yml"
  end
end
