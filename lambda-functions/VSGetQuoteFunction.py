import boto3
import os
import json
import random

def lambda_handler(event, context):
    table_name = os.environ['DYNAMODB_TABLE_NAME']
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    # Fetch the entire list of quotes from DynamoDB
    response = table.scan()
    items = response['Items']

    # Randomly select one quote from the list
    if items:
        random_item = random.choice(items)
        random_quote = random_item['quote']
        random_author = random_item.get('author', 'Unknown')  # Assuming 'author' might be optional
    else:
        random_quote = "No quotes available."
        random_author = "N/A"

    # Return the randomly selected quote in the API response
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
        },
        'body': json.dumps({
            'quote': random_quote,
            'author': random_author
        })
    }
