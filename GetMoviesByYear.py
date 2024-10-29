import boto3
import json
from decimal import Decimal

def convert_decimal(obj):
    if isinstance(obj, list):
        return [convert_decimal(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: convert_decimal(v) for k, v in obj.items()}
    elif isinstance(obj, Decimal):
        return float(obj)
    else:
        return obj

def lambda_handler(event, context):
    year = event['pathParameters']['year']
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Movies')
    
    response = table.scan(
        FilterExpression='releaseYear = :year',
        ExpressionAttributeValues={':year': int(year)}
    )
    
    movies = convert_decimal(response['Items'])
    
    return {
        'statusCode': 200,
        'body': json.dumps(movies)
    }
