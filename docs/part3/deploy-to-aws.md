# Deploying to a Real AWS Environment
## Why Test in a Real AWS Environment?
While local testing provides an efficient way to test and debug applications during development, it is crucial to also test in a real AWS environment. Here's why:

1. **Permissions Testing**: Local testing environments do not enforce AWS permissions, so any issues related to access controls or policies will not surface until the application is deployed to AWS. These could include permissions for accessing a DynamoDB table, invoking a Lambda function, or any other actions that require specific IAM permissions.

2. **Service Limitations**: AWS services have certain limitations, that aren't replicated in local environments. Testing in a real AWS environment helps ensure that your application operates correctly within these constraints.

3. **Service Interactions**: While local testing can simulate AWS services, it may not perfectly mimic all the nuances of how these services behave in a real AWS environment.

## Exercise: Deploying and Testing in AWS
Now that we understand the importance of testing in a real AWS environment, let's deploy and test our "Crisis at the Concert" application.

1. Deploy the Application: Use the `sam build && sam deploy`  command to deploy your application to AWS.

2. Test your api interface: After deployment, try invoking your api using curl or a similar tool. Initially, you'll encounter an error.

3. Pull Lambda Logs: To investigate the error, use the `sam logs -n YourFunctionName` command to retrieve the logs for your Lambda function. The logs should indicate a permissions issue when trying to access the DynamoDB table.

4. Add DynamoDB Permissions: To resolve this, you'll need to add the necessary permissions to your SAM template. Under the Policies property of your Lambda function's configuration, add a DynamoDBCrudPolicy and specify the name of your DynamoDB table. Your updated configuration might look like this:
```
Policies:
  - DynamoDBWritePolicy:
      TableName: !Ref TicketsTable
```
5. Redeploy and Test Again: After updating your SAM template, use the sam deploy command again to redeploy your application. Once deployment is complete, try invoking your Lambda function again. This time, it should successfully access the DynamoDB table and return the expected result.5. 
