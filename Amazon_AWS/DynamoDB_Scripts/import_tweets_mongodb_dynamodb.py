import boto3
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

# # Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('tweet')
print(table.key_schema)


# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb://localhost:27017/test")
db=client.test
# Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)

tweet = db.tweet.find({})

# for doc in tweet:
# 	print(doc['lang'])

with table.batch_writer() as batch:
	for doc in tweet:

		# print(doc)
		# doc['_id'] = str(doc['_id'])
		# doc['id'] = int(doc['id'])
		batch.put_item(
			Item={
                'id': doc['id'],
                'text': doc['text'],
                'added_tweet_sentiment': doc['added_tweet_sentiment'],
                'added_tweet_sentiment_positive': str(doc['added_tweet_sentiment_positive']),
                'added_tweet_sentiment_negative': doc['added_tweet_sentiment_negative']
            }
		)
