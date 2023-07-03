import json
import boto3
import os

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.getenv('TABLE_NAME'))

    body = json.loads(event['body'])
    if 'namer' not in body or 'ticket_count' not in body:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid request, name and ticket_count are required.'})
        }

    name = body['name']
    ticket_count = body['ticket_count']

    if type(ticket_count) is not str:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid request, ticket_count should be a number.'})
        }

    try:
        table.put_item(
            Item={
                'name': name,
                'ticket_count': ticket_count
            }
        )
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error.'})
        }

    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Successfully booked {ticket_count} tickets for {name}.'})
    }
