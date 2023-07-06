# Testing AWS Lambda Function with Moto and Pytest
In this guide, we'll be writing unit tests for an AWS Lambda function using `moto` and `pytest`. The function scans a DynamoDB table and calculates the sum of all 'ticket_count' values.

## Test 1: Creating Fake Data and Checking the Sum
Here is an example of a test that creates fake data in the table and checks if the sum calculated by the function is correct.

1. Under `tests` create a new file named `test_ticket_sum.py`.
2. Paste the following code into it.

```py linenums="1"
import boto3
import os
import moto
import json
from src.lambdas.ticket_sum import handler

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
For the second test, we'll use a pytest fixture to set up the DynamoDB table.
Add the following code to `test_ticket_sum.py`.

```py linenums="1"
import pytest

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
        # Pytest pauses the fixture here and begins the test. The "table" variable is returned
        # to the test and can be accessed within the test function as an argument.
        yield table

        # Cleanup: Any code here would run after the test.


def test_sum_tickets_no_data(setup_dynamodb):
    response = handler({}, {})

    assert response['statusCode'] == 200
    assert json.loads(response['body'])['message'] == 'Total tickets booked: 0.'
```

In the second test, we use a pytest fixture (`setup_dynamodb`) to set up the DynamoDB table. The test function `test_sum_tickets_no_data` uses this fixture, so pytest will automatically call `setup_dynamodb` before running the test. Since we don't add any data to the table, we expect the sum of ticket counts to be `0`.

### yield
In the context of pytest fixtures, the `yield` keyword is used to provide a value (in this case, `table`) to the test that's using the fixture (in this case, `test_sum_tickets_no_data`). The test function can accept the yielded value as an argument (`setup_dynamodb` in the test function).

In terms of execution flow, pytest runs the code before yield as a setup for the test. Then, pytest pauses the fixture, runs the test, and resumes the fixture to run the code following yield for cleanup.

When using the moto library for mocking AWS services, it's important to use yield within a context manager (`with` statement). This ensures that the mock stays in scope for the duration of the test. Otherwise, the mock would go out of scope after the setup phase, and the actual AWS service might be called during the test, leading to unexpected results or charges.

## Exercise
Now it's your turn to put what you've learned into practice.

1. Your task is to refactor the first test (`test_sum_tickets_with_data`) to use the `setup_dynamodb` fixture we've created. 
2. Your next task is to write a unit test for the BookTicketFunction Lambda function. Use Moto to mock the DynamoDB service, ensuring that data is correctly written to the table when the Lambda function is invoked.
3. Write a test that covers the full flow of the two Lambda functions together.
First, invoke the `BookTicketFunction` Lambda to book some tickets.
Next, invoke the `SumTicketsFunction` Lambda to calculate the total number of tickets booked.
Compare the result from `SumTicketsFunction` with the number of tickets you initially booked. They should match.

**Remember to use the setup_dynamodb fixture to create the DynamoDB table.**

## Deployment
After creating the tests and fixing the relevant code tibits it's time to run the service locally `sam build && sam deploy` and test it using sam local.
