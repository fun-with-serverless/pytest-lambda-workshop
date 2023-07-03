# Testing AWS Lambda Function with Moto and Pytest
In this guide, we'll be writing unit tests for an AWS Lambda function using `moto` and `pytest`. The function scans a DynamoDB table and calculates the sum of all 'ticket_count' values.

## Test 1: Creating Fake Data and Checking the Sum
Here is an example of a test that creates fake data in the table and checks if the sum calculated by the function is correct:

```py linenums="1"
import boto3
import os
import moto
import json
from src.ticket_sum import handler

def test_sum_tickets_with_data():
    with moto.mock_dynamodb():
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table_name = 'test-table'
        os.environ['TABLE_NAME'] = table_name
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
        )

        items = [{'id':str(i), 'name': 'name'+str(i), 'ticket_count': str(i)} for i in range(5)]
        with table.batch_writer() as batch:
            for item in items:
                batch.put_item(Item=item)

        response = handler({}, {})

        assert response['statusCode'] == 200
        assert json.loads(response['body'])['message'] == 'Total tickets booked: 10.'
```
In this test, we use moto to mock DynamoDB service. We then create a table and add some fake data to it. After that, we call the Lambda function and assert that the response status code is `200` and the sum of ticket counts is correct.

## Pytest Fixtures
Pytest fixtures are functions that are run by pytest before (and sometimes after) the actual test functions. They are used to set up some context needed for the test. Here is a simple example of a pytest fixture:
```py linenums="1"
import pytest

@pytest.fixture
def setup_data():
    data = {"key1": "value1", "key2": "value2"}
    return data

def test_data_key1(setup_data):
    assert setup_data['key1'] == 'value1'
```
In this example, `setup_data` is a fixture that sets up some data that is used in the test function `test_data_key1`. Pytest automatically calls the fixture function and passes its return value as an argument to the test function.

## Test 2: Checking Sum Without Data
For the second test, we'll use a pytest fixture to set up the DynamoDB table:

```py linenums="1"
import pytest
import boto3
import os
import moto
import json
from your_lambda_file import handler  # replace this with your actual import

@pytest.fixture
def setup_dynamodb():
    with moto.mock_dynamodb():
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table_name = 'test-table'
        os.environ['TABLE_NAME'] = table_name
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
        )
        yield # This is where pytest pauses the fixture and runs the test

        # Cleanup: Any code here would run after the test.


def test_sum_tickets_no_data(setup_dynamodb):
    response = handler({}, {})

    assert response['statusCode'] == 200
    assert json.loads(response['body'])['message'] == 'Total tickets booked: 0.'
```

In the second test, we use a pytest fixture (`setup_dynamodb`) to set up the DynamoDB table. The test function `test_sum_tickets_no_data` uses this fixture, so pytest will automatically call `setup_dynamodb` before running the test. Since we don't add any data to the table, we expect the sum of ticket counts to be `0`.

### yield
When used in a pytest fixture, `yield` allows us to separate the setup and cleanup parts of the fixture. Code before the yield statement is the setup part, and it is executed before the test runs. Code after yield is the cleanup part, and it is executed after the test runs, even if the test fails or raises an exception.

## Exercise
Now it's your turn to put what you've learned into practice.

1. Your task is to refactor the first test (`test_sum_tickets_with_data`) to use the `setup_dynamodb` fixture we've created. 
2. Your next task is to write a unit test for the BookTicketFunction Lambda function. Use Moto to mock the DynamoDB service, ensuring that data is correctly written to the table when the Lambda function is invoked.
3. Write a test that covers the full flow of the two Lambda functions together.
First, invoke the `BookTicketFunction` Lambda to book some tickets.
Next, invoke the `SumTicketsFunction` Lambda to calculate the total number of tickets booked.
Compare the result from `SumTicketsFunction` with the number of tickets you initially booked. They should match.

**Remember to use the setup_dynamodb fixture to create the DynamoDB table.**