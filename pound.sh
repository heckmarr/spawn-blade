#!/usr/bin/env bash
if [ /home/.tator ]; then
	loginctl unlock-session 2
	#rm /home/.tator
fi
