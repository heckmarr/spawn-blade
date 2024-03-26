#!/bin/bash
rm .tmp_start_draw
xinput | grep "Pen Pen" >> .tmp_start_draw
while read p; do
	LAST=${p##*id=};
	NUM=`echo $LAST | awk '{print $1}'`
	echo 'Device is '$NUM;
done <.tmp_start_draw
xrandr | grep "HDMI" > .tmp_start_draw;
while read p; do
	DEV=`echo $p | awk '{print $1}'`
	echo 'Display is '$DEV;
done <.tmp_start_draw

xinput map-to-output $NUM $DEV;
LENGTH=`echo $NUM | awk '{print length}';`
if [ "$LENGTH" == 0 ]
then

echo 'OUTPUT NOT MAPPED, DEVICE NOT PRESENT';

else

echo 'OUTPUT '$NUM' MAPPED TO '$DEV;
fi
