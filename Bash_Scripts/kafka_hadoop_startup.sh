#!/bin/sh

# start zookeeper in a new tab
gnome-terminal --tab -e "bash -c \"cd /home/jarvis/Desktop/kafka_2.11-2.3.0/;bin/zookeeper-server-start.sh config/zookeeper.properties;exec bash\""

# start kafka server in a new tab
gnome-terminal --tab -e "bash -c \"cd /home/jarvis/Desktop/kafka_2.11-2.3.0/;bin/kafka-server-start.sh config/server.properties;exec bash\""

# finally, start hadoop services in the current tab
sudo -u hadoop /home/hadoop/hadoop-2.8.5/sbin/start-all.sh
