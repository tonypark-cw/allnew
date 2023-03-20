#!/bin/bash

case "$1" in
	ko) echo "WON";;
	us) echo "DOLLAR";;
	cn) echo "YUAN";;
	jp) echo "JPY";;
	*) echo "Enter the Country Code"
esac

