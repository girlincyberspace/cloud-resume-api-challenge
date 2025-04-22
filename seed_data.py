import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Resume')

with open('resume.json') as f:
    resume_data = json.load(f)

table.put_item(Item={
    'id': 'john_doe',
    'resume': resume_data
})
