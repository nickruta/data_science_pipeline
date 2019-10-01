import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
import numpy as np
import pandas as pd


#always start with the lambda_handler
def lambda_handler(event, context):

    # make the connection to dynamodb
    dynamodb = boto3.resource('dynamodb')

    # select the table
    table = dynamodb.Table("tweet")

    # Table scan
    response = table.scan(Limit=1000)

    # convert to a pandas dataframe to use c-based computations provided
    response_df = pd.DataFrame(response['Items'])

    # use pandas to get the average tweet length
    response_df["text_count"]=response_df["text"].apply(lambda x: len(x))
    text_mean = response_df["text_count"].mean()

    # # used to iterate the resonse
    # for i in response['Items']: 
    #     # get all the table entries in json format
    #     json_str = json.dumps(i)
    #     #using json.loads will turn your data into a python dictionary
    #     resp_dict = json.loads(json_str)
    #     # Getting particular column entries
    #     # will return None if 'Name' doesn't exist
    #     print (resp_dict.get('text'))

    return_dict = {"average_tweet_length":text_mean}

    return {
            "statusCode": 200,
            "body": json.dumps(return_dict)
        }