#!/bin/bash

uid=$1
cnt=$2

while [ $cnt -gt 0 ]; do
	let uid+=1
	username=`grep $uid /etc/passwd | cut -f1 -d:`
	userdel -r $username
	echo [ $username ]
	let cnt-=1
done
echo Complete.
