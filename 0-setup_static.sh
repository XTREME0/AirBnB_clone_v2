#!/usr/bin/env bash
# setup server 
sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "<html>
	<head>
	</head>
	<body>
		Hello
	</body>
      </html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

config_text="location /hbnb_static {\n    alias /data/web_static/current/;\n}"
sudo sed -i "/server_name _;/a $config_text" /etc/nginx/sites-available/default

sudo service nginx restart
