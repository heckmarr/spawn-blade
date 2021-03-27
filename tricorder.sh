#!/bin/bash

for A in $(ls)
do
	stat on $A;
done
