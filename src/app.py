import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Resume')

def lambda_handler(event, context):
    try:
        response = table.get_item(Key={'id': 'john_doe'})
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item']['resume'])
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Resume not found'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
