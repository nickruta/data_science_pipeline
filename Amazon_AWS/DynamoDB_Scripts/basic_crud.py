import boto3
from boto3.dynamodb.conditions import Key, Attr

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('tweet')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
# print(table.creation_date_time)
print(table.key_schema)

# table.put_item(
#    Item={
#         'username': 'janedoe',
#         'first_name': 'Jane',
#         'last_name': 'Doe',
#         'age': 25,
#         'account_type': 'standard_user',
#     }
# )

# response = table.get_item(
#     Key={
#         'username': 'janedoe',
#         'last_name': 'Doe'
#     }
# )
# item = response['Item']
# print(item)


# table.update_item(
#     Key={
#         'username': 'janedoe',
#         'last_name': 'Doe'
#     },
#     UpdateExpression='SET age = :val1',
#     ExpressionAttributeValues={
#         ':val1': 26
#     }
# )


# response = table.get_item(
#     Key={
#         'username': 'janedoe',
#         'last_name': 'Doe'
#     }
# )
# item = response['Item']
# print(item)


# table.delete_item(
#     Key={
#         'username': 'janedoe',
#         'last_name': 'Doe'
#     }
# )


response = table.scan(
    FilterExpression=Attr('id').gte('0')
)
items = response['Items']
print(len(items))
print(items[0])