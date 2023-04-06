#!/bin/bash

/replica/mongodb/bin/mongod --config /replica/master.conf &
/replica/mongodb/bin/mongod --config /replica/slave1.conf &
/replica/mongodb/bin/mongod --config /replica/slave2.conf &
/replica/mongodb/bin/mongod --config /replica/arbiter.conf &

sleep 2s

ps -ef | grep mongo

sleep 3s
netstat -ntlp | grep mongod
sleep 3s

/replica/mongodb/bin/mongo localhost:10000 < rs_start