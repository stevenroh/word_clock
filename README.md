# word_clock

This repository will contain all the files needed to build a hardware "word clock".

![word_clock](https://user-images.githubusercontent.com/1651603/143878746-50eb6f86-4df7-41d1-9da9-13b445194868.jpg)

## WiFi Connect

wifi-connect from Balena helps to connect and switch to WiFi network. To install use this script :

https://raw.githubusercontent.com/balena-os/wifi-connect/master/scripts/raspbian-install.sh

Source : https://github.com/balena-os/wifi-connect#installation

## Service

Copy word_clock.service to `/etc/systemd/system/`

## 

```
sudo apt install git python3-pip
pip3 install -r requirements.txt
```