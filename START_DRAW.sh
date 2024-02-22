#!/bin/bash
rm .tmp_start_draw
id="id=";
xinput | grep "Pen Pen" >> .tmp_start_draw
while read p; do
	LAST=${p##*id=};
	NUM=`echo $LAST | awk '{print $1}'`
	echo 'Device is '$NUM;
done <.tmp_start_draw
xinput map-to-output $NUM HDMI-0;
echo 'OUTPUT MAPPED TO HDMI-0';
