#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployement of web_static
sudo apt update
sudo apt -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sed -i "/listen 80 default_server;/a location /hbnb_static/ {alias /data/web_static/current/;}" /etc/nginx/sites-available/default
service nginx restart
