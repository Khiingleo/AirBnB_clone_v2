#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static

nginx_config="location /hbnb_static {\n\talias /data/web_static/current/;\n\t}\n"

sudo apt-get -y update

# install nginx if not already installed
if ! [ -x "$(command -v nginx)" ]; then
	sudo apt-get -y install nginx
fi

# create directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# create fake HTML file to test nginx config
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# create symbolic link if it doesn't exist, if it does, delete and recreate
if [ -L /data/web_static/current ]; then
	sudo rm /data/web_static/current
fi
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of /data/ folder to ubuntu user AND group(recursive)
sudo chown -R ubuntu:ubuntu /data/

# update the nginx configuration
sudo sed -i "/listen 80 default_server;/a $nginx_config" /etc/nginx/sites-available/default

# test for error
sudo nginx -t

# restart nginx after configuration
sudo service nginx restart
