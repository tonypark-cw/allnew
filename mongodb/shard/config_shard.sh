#!/bin/bash

systemctl stop mongod

export IP_TEMP=$(ip addr | grep enp0s3 | grep inet | cut -d " " -f6 | cut -d "/" -f1 )
# export IP_TEMP
echo $IP_TEMP

if [ -d data ]; then
    rm -rf ./data
fi

#config server
mkdir -pv /shard/data/configdb
mkdir -pv /shard/data/logs
touch /shard/data/logs/configsvr.log

mongod --config /shard/mongodConfig.conf &
sleep 3s

# mongo 192.168.1.41:27019 < rs.init
mongo $IP_TEMP:27019 < rs.init
sleep 3s


#router server
touch /shard/data/logs/mongorouter.log

mongos --config /shard/mongodRouter.conf &
sleep 3s


#shard1 server
mkdir -pv /shard/data/shard1db
touch /shard/data/logs/shard1.log

mongod --config /shard/mongodShard1.conf &
sleep 2s
# mongo 192.168.1.41:27021 < rs.init
mongo $IP_TEMP:27021 < rs.init

#shard2 server
mkdir -pv /shard/data/shard2db
touch /shard/data/logs/shard2.log

mongod --config /shard/mongodShard2.conf &
sleep 2s
# mongo 192.168.1.41:27022 < rs.init
mongo $IP_TEMP:27022 < rs.init

# process status
ps -ef | grep mongod
sleep 2s

# sharding check
# mongo 192.168.1.41:27017 < rs.addShard
mongo $IP_TEMP:27017 < rs.addShard

# netstatus
netstat -ntlp
