import boto3
import os
import json
import uuid

def lambda_handler(event, context):
    table_name = os.environ['DYNAMODB_TABLE_NAME']
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    # Generate a unique game_id
    quote_id = str(uuid.uuid4())


    # Extract the data from the event
    body = json.loads(event['body'])
    quote = body['quote']
    author = body['author']

    
    # Put the item into the table
    response = table.put_item(
        Item={
            'id': quote_id,
            'quote': quote,
            'author': author
        }
    )

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
        },
        'body': json.dumps('Item added successfully')
    }
