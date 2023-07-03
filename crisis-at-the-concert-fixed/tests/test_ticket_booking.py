# test_lambda_function.py

import json
from src.ticket_booking import handler as ticket_booking_handler
from src.ticket_sum import handler as ticket_sum_handler
import moto
import boto3
import os
import pytest


@pytest.fixture
def setup_dynamodb():
    with moto.mock_dynamodb():
        dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
        table_name = "test-table"
        os.environ["TABLE_NAME"] = table_name
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[{"AttributeName": "name", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "name", "AttributeType": "S"}],
            ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
        )
        yield table  # This is where pytest pauses the fixture and runs the test

        # Cleanup: Any code here would run after the test.


def test_handler_missing_name_return_400():
    event = {"body": json.dumps({"ticket_count": "2"})}

    response = ticket_booking_handler(event, {})

    assert response["statusCode"] == 400
    assert (
        json.dumps({"message": "Invalid request, name and ticket_count are required."})
        == response["body"]
    )


def test_handler_missing_ticket_count_return_400():
    event = {"body": json.dumps({"name": "Dancing with the stars"})}

    response = ticket_booking_handler(event, {})

    assert response["statusCode"] == 400
    assert (
        json.dumps({"message": "Invalid request, name and ticket_count are required."})
        == response["body"]
    )


def test_handler_ticket_count_is_not_number_return_400():
    event = {"body": json.dumps({"name": "Dancing with the stars", "ticket_count": "2"})}

    response = ticket_booking_handler(event, {})

    assert response["statusCode"] == 400
    assert (
        json.dumps({"message": "Invalid request, ticket_count should be a number."})
        == response["body"]
    )


def test_handler_booking_written_successfully_200_returned(setup_dynamodb):
    event = {
        "body": json.dumps({"name": "Dancing with the stars", "ticket_count": 2})
    }

    response = ticket_booking_handler(event, {})

    assert response["statusCode"] == 200
    assert (
        setup_dynamodb.scan(
            AttributesToGet=[
                "ticket_count",
            ]
        )["Items"][
            0
        ]["ticket_count"]
        == 2
    )


def test_full_happy_flow(setup_dynamodb):
    event1 = {"body": json.dumps({"name": "Dancing with the stars", "ticket_count": 2})}
    event2 = {
        "body": json.dumps({"name": "Viki Cristina Barcelona", "ticket_count": 5})
    }

    book_response1 = ticket_booking_handler(event1, {})
    book_response2 = ticket_booking_handler(event2, {})

    ticket_sum_response = ticket_sum_handler({}, {})

    assert book_response1["statusCode"] == 200
    assert book_response2["statusCode"] == 200
    assert ticket_sum_response["statusCode"] == 200
    assert (
        json.loads(ticket_sum_response["body"])["message"] == "Total tickets booked: 7."
    )
