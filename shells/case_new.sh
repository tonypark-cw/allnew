#!/bin/bash

if [ $# -eq 0 ] ; then
	echo "Enter the Country Code"
else
	case "$1" in
		ko) echo "WON";;
		us) echo "DOLLAR";;
		cn) echo "YUAN";;
		jp) echo "JPY";;
		*) echo "Your input [ $1 ] is not in the Country Code."
	esac
fi

