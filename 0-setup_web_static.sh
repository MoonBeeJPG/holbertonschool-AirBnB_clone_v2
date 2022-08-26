#!/usr/bin/env bash
# script that sets up your web servers for the deployement of web_static
CREATE /data/ IF NOT EXISTS
CREATE /data/web_static/ IF NOT EXISTS
CREATE /data/web_static/releases/ IF NOT EXISTS
CREATE /data/web_static/releases/test/ IF NOT EXISTS
CREATE /data/web_static/releases/test/index.html IF NOT EXISTS
LN -s /data/web_static/releases/test/ /test/
#GRANTS owner /data/ USER ubuntu
sudo chown 755 ubuntu /data/web_static_releases/test/
UPDATE nginx 
