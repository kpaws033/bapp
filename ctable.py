import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table (
    TableName = "UserCheckin",
    KeySchema = [
      { 'AttributeName': "Username", 
        "KeyType": "HASH" }
    ],
    AttributeDefinitions = [
      { 
        'AttributeName': "Username", 
        'AttributeType': "S" }
    ],
    ProvisionedThroughput = {
      'ReadCapacityUnits': 5,
      'WriteCapacityUnits': 5
    }

)
print(table)