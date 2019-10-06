import flask
from flask import Response, jsonify
from flask_mongoalchemy import MongoAlchemy, BaseQuery
from flask_cors import CORS, cross_origin

from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson import ObjectId, json_util
import json
import os
import requests

def create_app(config=None):
	app = flask.Flask(__name__)
	app.config["DEBUG"] = True
	app.config["MONGO_URI"] = "mongodb://mongodb:27017/test" # use for docker
	# app.config["MONGO_URI"] = "mongodb://localhost:27017/test" # use for local


	mongo = PyMongo(app)

	def get_tweets():
		tweets = mongo.db.tweet.find()

		tweets_list = []
		for tweet in tweets:
			print(tweet)
			del tweet['_id']
			tweets_list.append(dict(tweet))

		return tweets_list

	@app.route('/', methods=['GET'])
	def home():
		return "<h1>Twitter Data Analysis</h1><p>This site is a web services API for machine learning using twitter data.</p>"

	# A route to return all of the available tweets in the mongodb test.tweets database collection.
	@app.route('/api/get/tweets/all', methods=['GET'])
	def api_all():
		tweets_list = get_tweets()
		return Response(json.dumps(tweets_list),  mimetype='application/json')

	# A route to return one prediction for each tweet in mongodb test.tweets database collection.
	# #corss_origin() needed for get call from front end at different address
	@app.route('/api/get/tweets/prediction', methods=['GET'])
	@cross_origin()
	def api_predictions():

		tweets_list = get_tweets()

		# for tweet in tweets_list:
		# 	for key, value in tweet.items() :
		# 		print(key)
		# 		print(value)

		prediction = list(["up"])
		return Response(json.dumps(prediction),  mimetype='application/json')

	# A route to return tweets statistics. it is using an Amazon AWS REST Endpoint
	# created in an AWS Lambda function that accesses a DynamoDB table of the tweets
	# #corss_origin() needed for get call from front end at different address
	@app.route('/api/get/tweets/statistics', methods=['GET'])
	@cross_origin()
	def api_statistics():

		# GET request to Amazon AWS endpoint using AWS Lambda Function
		r = requests.get('https://h21j20azc3.execute-api.us-east-1.amazonaws.com/default/createTweetsStatistics')
		data = json.loads(r.text)
		return Response(json.dumps(data),  mimetype='application/json')

	return app

if __name__ == "__main__":
	app = create_app()
	app.run(host='0.0.0.0')