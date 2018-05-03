import boto3;
from boto3.dynamodb.conditions import Key, Attr

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('restaurant')

def delete_restaurant_by_id(event, context):
    idKey = event["restaurantId"]
    response = table.query(
        KeyConditionExpression=Key('id').eq(int(idKey))
    )
    items = response['Items']
    for item in items:
        itemId = item['id']
        itemCity = item['city']
        response = table.delete_item(
            Key={'id': itemId ,
                 'city' : itemCity}
             )
    return response
    
    