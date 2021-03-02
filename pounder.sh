#!/usr/bin/env bash


export XAUTHORITY=/home/root/.Xauthority
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"

/usr/bin/sudo -u root -c /home/barbados/Code/spawn-blade/pound.sh


