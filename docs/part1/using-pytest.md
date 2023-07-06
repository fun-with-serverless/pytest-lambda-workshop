# Writing Unit Tests with Pytest for AWS Lambda
`pytest` is a popular framework for writing and running Python unit tests. It provides an easy way to collect tests, and has a rich plugin architecture for extending its functionality.

## Installation
To install `pytest` and `boto3`, use pip:
```bash
pip install pytest
pip install boto3
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
A pytest test case is a function that begins with `test_`, and resides in a Python file beginning with `test_`. 

1. A `test` folder and a t`est_ticket_booking.py` file exist as part of the crisis-at-the-concert-err source.
2. Here is an example of a test for the BookTicketFunction lambda, paste it into `test_ticket_booking.py`:

```python linenums="1"
import json
from src.ticket_booking import handler
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

1. **Test for failure when ticket_count are missing**: Create a test that sends an event without a ticket_count and checks that the handler function returns a response with a status code of 400.

2. **Test for failure when ticket_count is not a string**: Create a test that sends an event where ticket_count is not a string (for example, it could be a number) and checks that the handler function returns a response with a status code of 400.

Remember to assert both the status code and the response body message in your tests to make sure your lambda is responding as expected.

Run your tests with `pytest` and check their result.