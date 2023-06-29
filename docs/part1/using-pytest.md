# Writing Unit Tests with Pytest for AWS Lambda
`pytest` is a popular framework for writing and running Python unit tests. It provides an easy way to collect tests, and has a rich plugin architecture for extending its functionality.

## Installation
To install `pytest`, use pip:
```bash
pip install pytest
```

## Folder Structure
A typical Python project structure with `pytest` might look like this:
```
.
├── src
│   └── lambda_function.py
└── tests
    └── test_lambda_function.py
```
In this structure, the src directory contains your source code (`lambda_function.py`), and the tests directory contains your test code (`test_lambda_function.py`).

## Writing Tests
A pytest test case is a function that begins with `test_`, and resides in a Python file beginning with `test_`. Here is an example of a test for the BookTicketFunction lambda:
```python linenums="1"
# test_lambda_function.py

import json
import pytest
from src.lambda_function import handler
from botocore.exceptions import BotoCoreError

def test_handler_valid_input_return_success():
    event = {
        'body': json.dumps({
            'name': 'John Doe',
            'ticket_count': '2'
        })
    }

    response = handler(event, {})

    assert response['statusCode'] == 200
    assert 'Successfully booked' in response['body']
```

This test checks that the handler function returns a successful response when given valid input.

## Running Tests
To run tests, navigate to your project root directory and use the command:
```bash
pytest
```
`pytest` will automatically discover and run all tests in files named `test_*.py` or `*_test.py` in the current directory and its subdirectories.

Try running your test, it should fail, do you know why? Fix the code and rerun the test.

## Exercise
Now, try writing two additional unit tests for the `BookTicketFunction` lambda:

1. **Test for failure when name or ticket_count are missing**: Create a test that sends an event without a name or ticket_count and checks that the handler function returns a response with a status code of 400.

2. **Test for failure when ticket_count is not a string**: Create a test that sends an event where ticket_count is not a string (for example, it could be a number) and checks that the handler function returns a response with a status code of 400.

Remember to assert both the status code and the response body message in your tests to make sure your lambda is responding as expected.

Run your tests with `pytest` and check their result.