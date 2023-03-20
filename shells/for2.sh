#!/bin/bash

row="one two three four five"

for mon in $row
do
	for ((i=1;i<=9;i++)) do
		echo "$mon $i"
	done
done
	
