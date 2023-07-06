import json
import boto3
import os
from .consts import REGION


def handler(event, context):
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    table = dynamodb.Table(os.getenv("TABLE_NAME"))

    try:
        response = table.scan(
            AttributesToGet=[
                "ticket_count",
            ]
        )
    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error."}),
        }

    ticket_counts = response["Items"]
    total_tickets = sum(int(ticket["ticket_count"]) for ticket in ticket_counts)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Total tickets booked: {total_tickets}."}),
    }
