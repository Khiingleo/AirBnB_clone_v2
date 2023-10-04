#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static

nginx_config="s|location /hbnb_static/ {.*|location /hbnb_static/"
nginx_config+="{\n\talias /data/web_static/current/;\n}|"

sudo apt-get -y update

# install nginx if not already installed
if ! [ -x "$(command -v nginx)" ]; then
	sudo apt-get -y install nginx
fi

# create directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# create fake HTML file to test nginx config
echo "Test file to check nginx config" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# create symbolic link if it doesn't exist, if it does, delete and recreate
if [ -L /data/web_static/current ]; then
	sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# give ownership of /data/ folder to ubuntu user AND group(recursive)
sudo chown -R ubuntu:ubuntu /data/

# update the nginx configuration
sudo sed -i "$nginx_config" /etc/nginx/sites-available/default

# restart nginx after configuration
sudo service nginx restart
