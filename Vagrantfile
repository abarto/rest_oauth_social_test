# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/trusty64"

  config.vm.hostname = "rest-oauth-social-test.local"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  config.vm.network "forwarded_port", guest: 80, host: 8000
  config.vm.network "forwarded_port", guest: 81, host: 8005

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  config.vm.synced_folder ".", "/home/vagrant/rest_oauth_social_test/"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   sudo apt-get update
  #   sudo apt-get install -y apache2
  # SHELL

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y python3 python3-dev postgresql postgresql-server-dev-all nginx

    sudo -u postgres psql --command="CREATE USER fake_social_site WITH PASSWORD 'fake_social_site';"
    sudo -u postgres psql --command="CREATE DATABASE fake_social_site WITH OWNER fake_social_site;"
    sudo -u postgres psql --command="GRANT ALL PRIVILEGES ON DATABASE fake_social_site TO fake_social_site;"
    sudo -u postgres psql --command="CREATE USER my_api WITH PASSWORD 'my_api';"
    sudo -u postgres psql --command="CREATE DATABASE my_api WITH OWNER my_api;"
    sudo -u postgres psql --command="GRANT ALL PRIVILEGES ON DATABASE my_api TO my_api;"

    echo '
# fake_social_site.conf

upstream django_fake_social_site {
  server 127.0.0.1:8005;
}

server {
  listen      81;
  server_name 127.0.0.1 localhost rest-oauth-social-test rest-oauth-social-test.local;
  charset     utf-8;

  client_max_body_size 75M;

  location /media  {
      alias /home/vagrant/rest_oauth_social_test/fake_social_site/media;
  }

  location /static {
      alias /home/vagrant/rest_oauth_social_test/fake_social_site/static;
  }

  location / {
      proxy_pass       http://django_fake_social_site;
      proxy_redirect   off;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Host $server_name:8005;
  }
}
    ' > /etc/nginx/conf.d/fake_social_site.conf

    echo '
# my_api.conf

upstream django_my_api {
  server 127.0.0.1:8000;
}

server {
  listen      80;
  server_name 127.0.0.1 localhost rest-oauth-social-test rest-oauth-social-test.local;
  charset     utf-8;

  client_max_body_size 75M;

  location /media  {
      alias /home/vagrant/rest_oauth_social_test/my_api/media;
  }

  location /static {
      alias /home/vagrant/rest_oauth_social_test/my_api/static;
  }

  location / {
      proxy_pass       http://django_my_api;
      proxy_redirect   off;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Host $server_name:8000;
  }
}
    ' > /etc/nginx/conf.d/my_api.conf

  SHELL

  config.vm.provision "shell", inline: <<-SHELL
      service nginx restart
  SHELL

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    pyvenv-3.4 --without-pip fake_social_site_venv
    source fake_social_site_venv/bin/activate
    curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | python

    pip install -r rest_oauth_social_test/fake_social_site_requirements.txt

    cd rest_oauth_social_test/fake_social_site/

    python manage.py migrate

    echo '
    [
    {
        "model": "auth.user",
        "pk": 1,
        "fields": {
            "date_joined": "2015-07-08T00:22:51.199Z",
            "is_superuser": true,
            "user_permissions": [],
            "is_staff": true,
            "first_name": "",
            "password": "pbkdf2_sha256$20000$fUZfRXo5pI0X$uq5/DUsH4ArHdhr5Dv0gfKauW6HMrX4o3ANE5d7sois=",
            "email": "vagrant@rest-oauth-social-test.local",
            "username": "admin",
            "groups": [],
            "last_name": "",
            "last_login": "2015-07-10T17:04:01.932Z",
            "is_active": true
        }
    },
    {
        "model": "auth.user",
        "pk": 2,
        "fields": {
            "date_joined": "2015-07-08T00:52:05Z",
            "is_superuser": false,
            "user_permissions": [],
            "is_staff": false,
            "first_name": "John",
            "password": "pbkdf2_sha256$20000$FUn3mhnbQNHz$SDYMXBmFNOcT/tKK6Xq162M8PoWv+ox3YsplPD8OWeI=",
            "email": "john.doe@rest-oauth-social-test.local",
            "username": "user1",
            "groups": [],
            "last_name": "Doe",
            "last_login": null,
            "is_active": true
        }
    },
    {
        "model": "auth.user",
        "pk": 3,
        "fields": {
            "date_joined": "2015-07-08T00:53:06Z",
            "is_superuser": false,
            "user_permissions": [],
            "is_staff": false,
            "first_name": "Jane",
            "password": "pbkdf2_sha256$20000$IZ3WijqqoQQA$kszc9d98228H9Gkl/Ar64Sst2UVkrweA45TxUubgdPQ=",
            "email": "jane.doe@rest-oauth-social-test.local",
            "username": "user2",
            "groups": [],
            "last_name": "Doe",
            "last_login": null,
            "is_active": true
        }
    },
    {
        "model": "oauth2_provider.application",
        "pk": 1,
        "fields": {
            "client_id": "ZQcMr611iZMcUskTGoRcyZuhqCjZYy08lyOsWM5d",
            "user": [
                "admin"
            ],
            "authorization_grant_type": "password",
            "client_secret": "Ve0AVjI4G7JwPj0spAz4jvY0nNxGGfK9q6IJXqARRS3oobDY0sYxqepH0i1euXDLfcbWe8Dx27atNMyJvg3vRLssUBJd4otkoNgxD6jwje5l3ipJnwGpNy3QFq0EhB1g",
            "skip_authorization": true,
            "client_type": "public",
            "name": "my-api-app",
            "redirect_uris": ""
        }
    }
    ]
    ' > data.json

    python manage.py loaddata data.json
    python manage.py collectstatic --noinput
  SHELL

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    pyvenv-3.4 --without-pip my_api_venv
    source my_api_venv/bin/activate
    curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | python

    pip install -r rest_oauth_social_test/my_api_requirements.txt

    cd rest_oauth_social_test/my_api/

    python manage.py migrate

    echo '
    [
    {
        "fields": {
            "email": "vagrant@rest-oauth-social-test.local",
            "date_joined": "2015-07-08T00:22:51.199Z",
            "last_name": "",
            "is_superuser": true,
            "first_name": "",
            "is_active": true,
            "groups": [],
            "username": "admin",
            "is_staff": true,
            "password": "pbkdf2_sha256$20000$fUZfRXo5pI0X$uq5/DUsH4ArHdhr5Dv0gfKauW6HMrX4o3ANE5d7sois=",
            "last_login": "2015-07-10T17:13:51.000Z",
            "user_permissions": []
        },
        "pk": 1,
        "model": "auth.user"
    },
    {
        "fields": {
            "email": "vagrant@rest-oauth-social-test.local",
            "date_joined": "2015-07-10T17:14:48.459Z",
            "last_name": "",
            "is_superuser": false,
            "first_name": "",
            "is_active": true,
            "groups": [],
            "username": "admin04f4c347c0224e8c",
            "is_staff": false,
            "password": "!9MLVmBxi1XULFkBCqI0KrOH5wjpiNxKXIsNxX15U",
            "last_login": "2015-07-10T17:14:48.468Z",
            "user_permissions": []
        },
        "pk": 3,
        "model": "auth.user"
    },
    {
        "fields": {
            "client_id": "UvIhfUE25cCw0dOWNzvST2ciOm30uO3IqsdZRgj1",
            "client_secret": "eO3q0dVZl4pUglQEVKZLf5HPh2uRR4eF3XFYIhbESMXk8kPsin5PJdfh6e947ZvbJFHQiZIpXJfSuQswGkscEgA7rruTILiupwIOWxQQJ2QjRb6vUdbk63RooetpveLF",
            "skip_authorization": true,
            "user": [
                "admin"
            ],
            "authorization_grant_type": "password",
            "name": "my-api-app",
            "redirect_uris": "",
            "client_type": "public"
        },
        "pk": 1,
        "model": "oauth2_provider.application"
    },
    {
        "fields": {
            "name": "Concept A",
            "modified": "2015-07-10T16:58:16.232Z",
            "created": "2015-07-10T16:58:16.231Z",
            "parent": null
        },
        "pk": 1,
        "model": "concepts.concept"
    },
    {
        "fields": {
            "name": "Concept B",
            "modified": "2015-07-10T16:58:23.013Z",
            "created": "2015-07-10T16:58:23.012Z",
            "parent": null
        },
        "pk": 2,
        "model": "concepts.concept"
    },
    {
        "fields": {
            "name": "Concept C",
            "modified": "2015-07-10T16:58:28.898Z",
            "created": "2015-07-10T16:58:28.897Z",
            "parent": null
        },
        "pk": 3,
        "model": "concepts.concept"
    },
    {
        "fields": {
            "name": "Concept A.1",
            "modified": "2015-07-10T16:58:39.840Z",
            "created": "2015-07-10T16:58:39.837Z",
            "parent": 3
        },
        "pk": 4,
        "model": "concepts.concept"
    },
    {
        "fields": {
            "name": "Concept A.2",
            "modified": "2015-07-10T16:58:49.310Z",
            "created": "2015-07-10T16:58:49.306Z",
            "parent": 4
        },
        "pk": 5,
        "model": "concepts.concept"
    },
    {
        "fields": {
            "modified": "2015-07-10T16:59:35.524Z",
            "description": "This is Item A",
            "owner": [
                "admin"
            ],
            "name": "Item A",
            "created": "2015-07-10T16:59:35.520Z",
            "mass": 1.0
        },
        "pk": 1,
        "model": "items.item"
    },
    {
        "fields": {
            "modified": "2015-07-10T16:59:55.429Z",
            "description": "This is Item B",
            "owner": [
                "admin"
            ],
            "name": "Item B",
            "created": "2015-07-10T16:59:55.426Z",
            "mass": 2.0
        },
        "pk": 2,
        "model": "items.item"
    },
    {
        "fields": {
            "modified": "2015-07-10T17:00:06.267Z",
            "description": "This is Item C",
            "owner": [
                "admin"
            ],
            "name": "Item C",
            "created": "2015-07-10T17:00:06.265Z",
            "mass": 3.0
        },
        "pk": 3,
        "model": "items.item"
    },
    {
        "fields": {
            "modified": "2015-07-10T17:00:41.641Z",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras sodales urna nisi, in tempus purus malesuada non. Maecenas sed viverra urna. Nunc eget dui nulla. Mauris vel dolor turpis. Pellentesque vitae blandit felis. Fusce tincidunt tellus ac mollis malesuada. Phasellus facilisis faucibus diam, vitae convallis lacus blandit sit amet. Vestibulum vitae eros urna. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac.",
            "owner": [
                "admin"
            ],
            "name": "Item D",
            "created": "2015-07-10T17:00:41.637Z",
            "mass": 4.0
        },
        "pk": 4,
        "model": "items.item"
    },
    {
        "fields": {
            "modified": "2015-07-10T17:01:45.859Z",
            "description": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to",
            "owner": [
                "admin"
            ],
            "name": "Item Group #1",
            "created": "2015-07-10T17:01:45.853Z",
            "items": [
                4,
                3,
                2
            ]
        },
        "pk": 1,
        "model": "items.itemgroup"
    }
    ]
    ' > data.json

    python manage.py loaddata data.json
    python manage.py collectstatic --noinput
  SHELL

  config.vm.provision "shell", run: "always", privileged: false, inline: <<-SHELL
    source /home/vagrant/fake_social_site_venv/bin/activate

    cd /home/vagrant/rest_oauth_social_test/fake_social_site

    gunicorn --bind 127.0.0.1:8005 --daemon --workers 4 fake_social_site.wsgi
  SHELL

  config.vm.provision "shell", run: "always", privileged: false, inline: <<-SHELL
    source /home/vagrant/my_api_venv/bin/activate

    cd /home/vagrant/rest_oauth_social_test/my_api

    gunicorn --bind 127.0.0.1:8000 --daemon --workers 4 my_api.wsgi
  SHELL
end
