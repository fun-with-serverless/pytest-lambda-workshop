import json
import boto3
import os
import random
import string


def handler(event, context):
    body = json.loads(event["body"])
    if "name" not in body or "ticket_count" not in body:
        return {
            "statusCode": 400,
            "body": json.dumps(
                {"message": "Invalid request, name and ticket_count are required."}
            ),
        }

    name = body["name"]
    ticket_count = body["ticket_count"]

    if type(ticket_count) is not int:
        return {
            "statusCode": 400,
            "body": json.dumps(
                {"message": "Invalid request, ticket_count should be a number."}
            ),
        }

    try:
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(os.getenv("TABLE_NAME"))
        table.put_item(
            Item={
                "id": _generate_random_string(5),
                "name": name,
                "ticket_count": ticket_count,
            }
        )
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error."}),
        }

    return {
        "statusCode": 200,
        "body": json.dumps(
            {"message": f"Successfully booked {ticket_count} tickets for {name}."}
        ),
    }


def _generate_random_string(length):
    letters = string.ascii_letters
    result_str = "".join(random.choice(letters) for _ in range(length))
    return result_str
