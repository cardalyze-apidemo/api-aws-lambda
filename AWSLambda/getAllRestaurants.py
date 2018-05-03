import boto3;

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('restaurant')

def get_restaurant(event, context):
    response = table.scan("")
    return response['Items']
    