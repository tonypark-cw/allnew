#1/bin/bash

input="/etc/passwd"
i=1

echo "count : username	uid	gid	home	shell"

while IFS=':' read -r username	 password uid gid comment home shell
do
	echo " $i : $username	 -	$uid	-	$gid	-	$home	-	$shell"
	i=$[ $i + 1 ]
done < $input
