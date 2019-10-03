from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import operator
import numpy as np
# import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import os

from pyspark.sql import SparkSession

import pandas as pd
from hdfs import InsecureClient

import json

os.environ['HADOOP_USER_NAME'] = 'hadoop'

def main():

	os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars spark-streaming-kafka-0-8-assembly_2.11-2.4.3.jar pyspark-shell'

	conf = SparkConf().setMaster("local[2]").setAppName("Streamer")
	sc = SparkContext(conf=conf)

	# Creating a streaming context with batch interval of 10 sec
	ssc = StreamingContext(sc, 10)
	ssc.checkpoint("checkpoint")
	pwords = load_wordlist("./Dataset/positive.txt")
	nwords = load_wordlist("./Dataset/negative.txt")

	# default 100
	counts, tweets = stream(ssc, pwords, nwords, 10)
	# make_plot(counts)

	counts_list = counts
	df = pd.DataFrame(data = {'counts' : counts_list, 'tweets' : tweets})

	# HDFS SAVE
	# # Connecting to Webhdfs by providing hdfs host ip and webhdfs port (50070 by default)
	# client_hdfs = InsecureClient('http://' + 'localhost' + ':50070', user='hadoop')
	# # Writing Dataframe to hdfs
	# with client_hdfs.write('/test_data/test_counts_' + 'test2' + '.csv', encoding = 'utf-8') as writer:
	#     df.to_csv(writer)

def make_plot(counts):
	"""
	This function plots the counts of positive and negative words for each timestep.
	"""
	positiveCounts = []
	negativeCounts = []
	time = []

	for val in counts:
		positiveTuple = val[0]
		positiveCounts.append(positiveTuple[1])
		negativeTuple = val[1]
		negativeCounts.append(negativeTuple[1])

	for i in range(len(counts)):
		time.append(i)

	posLine = plt.plot(time, positiveCounts,'bo-', label='Positive')
	negLine = plt.plot(time, negativeCounts,'go-', label='Negative')
	plt.axis([0, len(counts), 0, max(max(positiveCounts), max(negativeCounts))+50])
	plt.xlabel('Time step')
	plt.ylabel('Word count')
	plt.legend(loc = 'upper left')
	plt.show()


def load_wordlist(filename):
	"""
	This function returns a list or set of words from the given filename.
	"""
	words = {}
	f = open(filename, 'rU')
	text = f.read()
	text = text.split('\n')
	for line in text:
		words[line] = 1
	f.close()
	return words


def wordSentiment(word,pwords,nwords):
	if word in pwords:
		return ('positive', 1)
	elif word in nwords:
		return ('negative', 1)


def updateFunction(newValues, runningCount):
	if runningCount is None:
	   runningCount = 0
	return sum(newValues, runningCount) 


def sendRecord(record):
	connection = createNewConnection()
	connection.send(record)
	connection.close()


def stream(ssc, pwords, nwords, duration):
	kstream = KafkaUtils.createDirectStream(
	ssc, topics = ['twitterstream'], kafkaParams = {"metadata.broker.list": 'localhost:9092'})

	def processRecord(record):
		rddCount = record.count() + 1

		if rddCount > 0:
			record.repartition(rddCount).saveAsTextFile('hdfs://localhost:9000/test_data/file' + '_' + str(rddCount))

	kstream.foreachRDD(processRecord)

	tweets = kstream.map(lambda x: x[1].encode("ascii", "ignore"))
	my_tweets = tweets

	# Each element of tweets will be the text of a tweet.
	# We keep track of a running total counts and print it at every time step.
	words = tweets.flatMap(lambda line:line.split(" "))
	
	# words.pprint()

	# my_tweets = tweets.flatMap(lambda line:line)
	# my_tweets.pprint()

	# words.pprint()


	positive = words.map(lambda word: ('Positive', 1) if word in pwords else ('Positive', 0))
	negative = words.map(lambda word: ('Negative', 1) if word in nwords else ('Negative', 0))
	allSentiments = positive.union(negative)


	sentimentCounts = allSentiments.reduceByKey(lambda x,y: x+y)
	runningSentimentCounts = sentimentCounts.updateStateByKey(updateFunction)
	runningSentimentCounts.pprint()

	# tweets.saveAsTextFile ("hdfs:///test1/");

	# The counts variable hold the word counts for all time steps
	counts = []
	sentimentCounts.foreachRDD(lambda t, rdd: counts.append(rdd.collect()))

	# Start the computation
	ssc.start() 
	ssc.awaitTerminationOrTimeout(duration)
	ssc.stop(stopGraceFully = True)

	return counts, my_tweets

if __name__=="__main__":
	main()

