#!/data/data/com.termux/files/usr/bin/sh

apt update && apt install python wget

cd $HOME
wget https://raw.githubusercontent.com/Hax4us/Apkmod/master/setup.sh
chmod +x setup.sh
sh setup.sh
