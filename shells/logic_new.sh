#!/bin/bash

opt1=$1
opt2=$2

if [ $# -ne 2 ]; then
	echo "Input two parameters."
else
	if [[ ( "$opt1" == 'test' && "$opt2" == 'aaa' ) ||  ( "$opt1" == 'aaa' && "$opt2" == 'test' ) ]]; then
		echo good
	else
		echo bad
	fi
fi
