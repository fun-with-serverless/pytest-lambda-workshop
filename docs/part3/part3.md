# AWS SAM Local for Local Testing
## What is AWS SAM Local?
AWS Serverless Application Model (SAM) Local is a CLI tool that allows developers to locally test and debug their AWS Lambda functions and API Gateway. AWS SAM Local uses Docker to run a Lambda-like environment on your local machine, allowing you to develop serverless applications without needing to deploy your application to AWS with each change.
## Local Testing in the "Crisis at the Concert" Scenario
In our "Crisis at the Concert" scenario, using AWS SAM Local for local testing can be incredibly useful. By running the concert application locally, we can iteratively make changes and immediately see their impact, helping us to debug and resolve issues more efficiently. This can greatly accelerate the process of troubleshooting and updating our Lambda functions to handle the ticketing system crisis.
## Starting API Gateway, and Lambda  Locally
To start your AWS services locally using AWS SAM, you'll need to use the sam local `start-api` command. This command starts a local API Gateway and runs your Lambda functions in response to requests.

Here's a basic example of starting your local API:
```
sam local start-api
```
Please note that AWS SAM Local must be run in the same directory as your SAM template.
## Defining Environment Variables
Environment variables can be defined in a JSON file and passed to the `sam local start-api` command using the `--env-vars` option. The JSON file should be structured as follows:
```
{
  "BookTicketFunction": {
    "TABLE_NAME": "my-table"
  }
}
```
You can find the table name in the output when AWS SAM `deploy` is running.

!!! note
    Please note that each function has a separate record in the JSON.

You can then pass this file to the sam local start-api command like so:
```
sam local start-api --env-vars env.json
```
## Exercise: Local Testing with AWS SAM
Now that you have an understanding of how to use AWS SAM Local, let's put it into practice with the following exercises:

1. Run the Concert Application Locally: Using the sam local start-api command, start your concert application locally. Don't forget to define any necessary environment variables in a JSON file and pass it to the command using the --env-vars option.

2. Perform Local Testing: Test your concert application by sending requests to the local API Gateway. You can use a tool like curl or Postman to send these requests. Experiment with different scenarios and observe the responses from your Lambda functions.

3. Check DynamoDB Values: After running your tests, check the values in your DynamoDB table in the AWS console. This can help you understand how your application is interacting with DynamoDB and whether it's behaving as expected.

Remember, local testing is a powerful tool for identifying and fixing issues in your application. Take advantage of AWS SAM Local to improve your serverless application development process.