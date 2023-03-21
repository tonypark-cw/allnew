#!/bin/bash

input="user.data"

while IFS=',' read -r username uid  gid comment
do
	userdel -r "$username"
	echo "Delete $username"
done < $input
