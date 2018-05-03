import boto3;
import json;

def add_restaurant(event, context):
    print(json.dumps(event, indent=2))
    dynamodb = boto3.resource('dynamodb')
    restaurantTable = dynamodb.Table('restaurant')
    response = restaurantTable.put_item(Item=event)
    print(event)
    return response