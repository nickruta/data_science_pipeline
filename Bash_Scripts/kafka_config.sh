#!/bin/sh

# kafka topic creation in a new tab
gnome-terminal --tab -e "bash -c \"cd /home/jarvis/Desktop/kafka_2.11-2.3.0/;bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic twitterstream;exec bash\""

# start kafka consumer for above topic in a new tab
gnome-terminal --tab -e "bash -c \"cd /home/jarvis/Desktop/kafka_2.11-2.3.0/;bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic twitterstream --from-beginning;exec bash\""

# start the twitter python app to stream tweets
gnome-terminal --tab -e "bash -c \"cd /home/jarvis/Desktop/Twitter-Sentiment-Analysis-Using-Spark-Streaming-And-Kafka-master/;source activate py27;python app.py;exec bash\""
