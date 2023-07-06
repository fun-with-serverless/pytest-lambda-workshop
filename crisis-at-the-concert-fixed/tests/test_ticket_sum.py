import boto3
import os
import moto
import json
import pytest
from src.ticket_sum import handler
from src.consts import REGION


@pytest.fixture
def setup_dynamodb():
    with moto.mock_dynamodb():
        dynamodb = boto3.resource('dynamodb', region_name=REGION)
        table_name = 'test-table'
        os.environ['TABLE_NAME'] = table_name
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
        )
        yield table# This is where pytest pauses the fixture and runs the test

        # Cleanup: Any code here would run after the test.

def test_sum_tickets_with_data(setup_dynamodb):
    items = [{'id': str(i), 'name': 'name'+str(i), 'ticket_count': i} for i in range(5)]
    with setup_dynamodb.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)

    response = handler({}, {})

    assert response['statusCode'] == 200
    assert json.loads(response['body'])['message'] == 'Total tickets booked: 10.'

def test_sum_tickets_no_data(setup_dynamodb):
    response = handler({}, {})

    assert response['statusCode'] == 200
    assert json.loads(response['body'])['message'] == 'Total tickets booked: 0.'