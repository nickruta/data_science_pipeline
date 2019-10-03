from pyspark import SparkConf,SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import Row,SQLContext, SparkSession
import sys
import requests
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql.types import *

import json 
from pymongo import MongoClient

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars spark-streaming-kafka-0-8-assembly_2.11-2.4.3.jar pyspark-shell'

# create spark configuration
conf = SparkConf()
conf.setAppName("TwitterStreamApp")
conf.set('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.11:2.3.1')
conf.set("spark.mongodb.input.uri", 'mongodb://127.0.0.1/test_database_nr')
conf.set("spark.mongodb.output.uri", 'mongodb://127.0.0.1/test_database_nr')
conf.set("spark.mongodb.output.collection","test_collection_nr")
conf.set("spark.mongodb.input.collection","test_collection_nr")

# create spark context with the above configuration
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
# create the Streaming Context from the above spark context with interval size 2 seconds
ssc = StreamingContext(sc, 2)
# setting a checkpoint to allow RDD recovery
ssc.checkpoint("checkpoint_TwitterApp")
# read data from port 9009

# nr: test to create spark session
sparkSession = SparkSession(sc)

# need this to use createDataFrame later
sqlContext = SQLContext(sc)

dataStream = KafkaUtils.createDirectStream(
	ssc, topics = ['twitterstream'], kafkaParams = {"metadata.broker.list": 'localhost:9092'})

def aggregate_tags_count(new_values, total_sum):
	return sum(new_values) + (total_sum or 0)

def get_sql_context_instance(spark_context):
	if ('sqlContextSingletonInstance' not in globals()):
		globals()['sqlContextSingletonInstance'] = SQLContext(spark_context)
	return globals()['sqlContextSingletonInstance']
def process_rdd(time, rdd):
	print("----------- %s -----------" % str(time))
	try:
		# Get spark sql singleton context from the current context
		sql_context = get_sql_context_instance(rdd.context)
		# convert the RDD to Row RDD
		row_rdd = rdd.map(lambda w: Row(hashtag=w[0], hashtag_count=w[1]))
		# create a DF from the Row RDD
		hashtags_df = sql_context.createDataFrame(row_rdd)
		# Register the dataframe as table
		hashtags_df.registerTempTable("hashtags")
		# get the top 10 hashtags from the table using SQL and print them
		hashtag_counts_df = sql_context.sql("select hashtag, hashtag_count from hashtags order by hashtag_count desc limit 10")
		hashtag_counts_df.show()


		# call this method to prepare top 10 hashtags DF and send them
		# send_df_to_dashboard(hashtag_counts_df)

	except:
		e = sys.exc_info()[0]
		print("Error (nothing to process): %s" % e)

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
		return 'positive', word
	elif word in nwords:
		return 'negative', word
	else:
		return 'neutral', word

def updateFunction(newValue, runningCount):

	# print(newValue+runningCount)
	runningCount = newValue+runningCount
	return runningCount

# load positive and negative words for sentiment analysis
pwords = load_wordlist("./Dataset/positive.txt")
nwords = load_wordlist("./Dataset/negative.txt")

tweets = dataStream.map(lambda x: x[1].encode("ascii", "ignore"))

def processRecord(record):

	def processEach(tweet):
		json_loaded = json.loads(tweet)
		tweet_text = json_loaded['text'].encode('utf-8')
		words = tweet_text.split(' ')

		runningCount = 0
		found_pwords = []
		found_nwords = []
		for word in words:
			# print(wordSentiment(word, pwords, nwords)) 
			word_sentiment, found_word = wordSentiment(word, pwords, nwords)
			if word_sentiment is 'positive':
				found_pwords.append(found_word)
				runningCount = updateFunction(1, runningCount)
			if word_sentiment is 'negative':
				found_nwords.append(found_word)
				runningCount = updateFunction(-1, runningCount)

		sentiment = 'positive' if runningCount > 0 else 'negative' if runningCount < 0 else 'neutral' 

		json_loaded['added_tweet_sentiment_positive'] = found_pwords
		json_loaded['added_tweet_sentiment_negative'] = found_nwords
		json_loaded['added_tweet_sentiment'] = sentiment
		json_loaded['twitter_stream_filter_keyword'] = 'tesla'

		return json_loaded

		#  <class 'pyspark.sql.dataframe.DataFrame'
		# print(type(characters))

	rddCount = record.count()

	if rddCount > 0:

		print("Processing: ", rddCount, " records.")

		schema = StructType(
		    [
		        StructField('_1',
		            StructType(
		                [
						# "coordinates" : NumberLong(0),
						StructField('coordinates', StringType(),True),
						# "retweeted" : NumberLong(0),
						StructField('retweeted',BooleanType(),True),
						# "source" : NumberLong(0),
						StructField('source', StringType(),True),
						# "entities" : NumberLong(0),
						StructField('entities', StringType(),True),
						# "reply_count" : NumberLong(0),
						StructField('reply_count', StringType(),True),
						# "favorite_count" : NumberLong(0),
						StructField('favorite_count', StringType(),True),
						# "in_reply_to_status_id_str" : NumberLong(0),
						StructField('in_reply_to_status_id_str', StringType(),True),
						# "geo" : NumberLong(0),
						StructField('geo', StringType(),True),
						# "id_str" : NumberLong(0),
						StructField('id_str', StringType(),True),
						# "in_reply_to_user_id" : NumberLong(0),
						StructField('in_reply_to_user_id', LongType(),True),
						# "timestamp_ms" : NumberLong(0),
						StructField('timestamp_ms', StringType(),True),
						# "truncated" : NumberLong(0),
						StructField('truncated', BooleanType(),True),
						# "text" : NumberLong(0),
						StructField('text', StringType(),True),
						# "retweet_count" : NumberLong(0),
						StructField('retweet_count', StringType(),True),
						# "retweeted_status" : NumberLong(0),
						StructField('retweeted_status', StringType(),True),
						# "id" : NumberLong("1174888051958517761"),
						StructField('id', StringType(),True),
						# "in_reply_to_status_id" : NumberLong(0),
						StructField('in_reply_to_status_id', StringType(),True),
						# "filter_level" : NumberLong(0),
						StructField('filter_level', StringType(),True),
						# "created_at" : NumberLong(0),
						StructField('created_at', StringType(),True),
						# "place" : NumberLong(0),
						StructField('place', StringType(),True),
						# "favorited" : NumberLong(0),
						StructField('favorited', BooleanType(),True),
						# "lang" : NumberLong(0),
						StructField('lang', StringType(),True),
						# "contributors" : NumberLong(0),
						StructField('contributors', StringType(),True),
						# "in_reply_to_screen_name" : NumberLong(0),
						StructField('in_reply_to_screen_name', StringType(),True),
						# "is_quote_status" : NumberLong(0),
						StructField('is_quote_status', BooleanType(),True),
						# "in_reply_to_user_id_str" : NumberLong(0),
						StructField('in_reply_to_user_id_str', StringType(),True),
						# "user" : NumberLong(0),
						StructField('user', StringType(),True),
						# "added_tweet_sentiment" : NumberLong(0),
						StructField('added_tweet_sentiment', StringType(),True),
						# "quote_count" : NumberLong(0)
						StructField('quote_count', StringType(),True),
						# twitter_stream_filter_keyword
						StructField('twitter_stream_filter_keyword', StringType(),True),
						StructField('added_tweet_sentiment_positive', StringType(),True),
						StructField('added_tweet_sentiment_negative', StringType(),True),
		                ]
		            )
		        )
		    ]
		)

		processed_tweets = record.map(processEach).map(lambda x: Row(x))

		# <class 'pyspark.rdd.PipelinedRDD'>
		# print(type(processed_tweets))

		sql_context = get_sql_context_instance(record.context)
		df = sql_context.createDataFrame(processed_tweets, schema)

		# print the custom schema defined above as 'scehma'
		# df.printSchema()

		# flatten the fields present by moving them to the root from the 
		# _1 array they were in
		df = df.select("_1.*")

		# save to mongodb
		df.write.format("com.mongodb.spark.sql.DefaultSource").option("replaceDocument","false").mode("append").save()
 
tweets.foreachRDD(processRecord)


words = tweets.flatMap(lambda line:line.split(" "))
# split each tweet into words
# words = dataStream.flatMap(lambda line: line.split(" "))

# filter the words to get only hashtags, then map each hashtag to be a pair of (hashtag,1)
hashtags = words.filter(lambda w: '#' in w).map(lambda x: (x, 1))
# adding the count of each hashtag to its last count
tags_totals = hashtags.updateStateByKey(aggregate_tags_count)
# do processing for each RDD generated in each interval
tags_totals.foreachRDD(process_rdd)
# start the streaming computation
ssc.start()
# wait for the streaming to finish
ssc.awaitTermination()
