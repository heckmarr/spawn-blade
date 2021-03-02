#To be put in /tmp/LOGIN.sh and made executable
#! /bin/bash
openvt -s bash
sleep 10

#To be put in /etc/udev/rules.d/login.rules
ATTRS(idVendor)=="YOURUSBKEYVENDORID", ATTRS(idProduct)=="YOURUSBKEYPRODUCTID", RUN="/tmp/LOGIN.sh"

#The idVendor and idProduct are four digit keys found via lsusb
#Enjoy!
