#To be put in /tmp/LOGIN.sh and made executable
#! /bin/bash
openvt -s bash
sleep 10

#To be put in /etc/udev/rules.d/login.rules

10-local.rules
ATTR{product}=="PRODUCTID", ATTR{serial}=="SERIAL", RUN+="/usr/bin/pound.sh"


#The idVendor and idProduct are four digit keys found via lsusb
#Enjoy!
