# test_lambda_function.py

import json
from src.ticket_booking import handler

def test_handler_missing_name_return_400():
    event = {
        'body': json.dumps({
            'ticket_count': '2'
        })
    }

    response = handler(event, {})

    assert response['statusCode'] == 400
    assert json.dumps({'message': 'Invalid request, name and ticket_count are required.'}) == response['body']

def test_handler_missing_ticket_count_return_400():
    event = {
        'body': json.dumps({
            'name': 'Dancing with the stars'
        })
    }

    response = handler(event, {})

    assert response['statusCode'] == 400
    assert json.dumps({'message': 'Invalid request, name and ticket_count are required.'}) == response['body']

def test_handler_ticket_count_is_not_string_return_400():
    event = {
        'body': json.dumps({
            'name': 'Dancing with the stars',
            'ticket_count': 2
        })
    }

    response = handler(event, {})

    assert response['statusCode'] == 400
    assert json.dumps({'message': 'Invalid request, ticket_count should be a number.'}) == response['body']