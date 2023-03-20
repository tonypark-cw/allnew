#!/bin/bash

a=1

while [ $a != "0" ]; do
	echo -n "input : "
	read a
	if [[ $a -lt 2 ]] || [[ $a -gt  9 ]]
	then
		echo " Type between 2 - 9 digit "
		continue
	else
		if [ $a != "0" ]; then
			for ((k=1;k<=9;k++))
			do
				echo " $a * $k = `expr $a \* $k `"
			done
		fi
	fi
done
echo Exit
