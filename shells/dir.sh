#!/bin/bash

if [ -d $1 ]; then
	echo "$1 directory is the exist directory "
else
	echo "$1 directory is not the exist directory."
fi
