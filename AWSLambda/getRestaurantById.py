import boto3;
from boto3.dynamodb.conditions import Key, Attr

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('restaurant')

def get_restaurant_id(event, context):
    idKey = event["restaurantId"]
    response = table.query(
        KeyConditionExpression=Key('id').eq(int(idKey))
    )
    return response['Items']