# Make sure the Apt package lists are up to date, so we're downloading versions that exist.
cookbook_file "apt-sources.list" do
  path "/etc/apt/sources.list"
end
execute 'apt_update' do
  command 'apt-get update'
end

# Base configuration recipe in Chef.
package "wget"
package "ntp"
cookbook_file "ntp.conf" do
  path "/etc/ntp.conf"
end
execute 'ntp_restart' do
  command 'service ntp restart'
end

# install pip
package "python-pip"
package "python3-django"

# install django
execute 'install_django' do
  command 'pip install Django==1.10.3'
end

# deploy mysite
execute 'deploy_mysite' do
  cwd '/home/ubuntu/project/mysite'
  command 'nohup python ./manage.py runserver 0:3000 &'
end
