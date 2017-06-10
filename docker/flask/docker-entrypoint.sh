#!/bin/bash
cd /app

# カレントディレクトリのsite-packagesを検索パスに追加
site_packages_dir="/app/site-packages"
echo $site_packages_dir > /usr/local/lib/python3.6/site-packages/usrlocal.pth

pip install -r ./requirements.txt -t $site_packages_dir
uwsgi --ini ./uwsgi.ini