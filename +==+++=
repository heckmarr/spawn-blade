#!/bin/bash

for x in *" "*; do
	mv -- "$x" "${x// /-}"
done

for x in *"zip"*; do
	mkdir -- "$x.d";
	copy $x "$x.d/$x";
	cd "$x.d";	
	unzip $x;
	cd ..;
done

for x in *"zip.d"*; do
	mv -- "$x" "${x//zip.d/d}";
	echo 'Done';
done
