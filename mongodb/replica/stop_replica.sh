#!/bin/bash

/replica/mongodb/bin/mongod --config /replica/master.conf &
/replica/mongodb/bin/mongod --config /replica/slave1.conf &
/replica/mongodb/bin/mongod --config /replica/slave2.conf &
/replica/mongodb/bin/mongod --config /replica/arbiter.conf &

master=$(ps -ef | grep 'mongod' | grep 'master')
slave1=$(ps -ef | grep 'mongod' | grep 'slave1')
slave2=$(ps -ef | grep 'mongod' | grep 'slave2')
arbiter=$(ps -ef | grep 'mongod' | grep 'arbiter')

second1=$(echo ${master} | cut -d " " -f2)
second2=$(echo ${slave1} | cut -d " " -f2)
second3=$(echo ${slave2} | cut -d " " -f2)
second4=$(echo ${arbiter} | cut -d " " -f2)

for var in $second1 $second2 $second3 $second4
do
    echo $var
    if [ -n ${var} ]; then
        result=$(kill -9 ${var})
        echo process is killed.
    else 
        echo running process not found.
    fi
done