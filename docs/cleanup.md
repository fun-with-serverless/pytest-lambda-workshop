# AWS Serverless Application Model (SAM) Cleanup

When working with AWS Serverless Application Model (SAM), it's important to remember to delete the resources you've created once you're done with them. This is not only a good practice to keep your AWS account organized, but it also helps you avoid any unnecessary costs from resources you no longer use.

## AWS Resources Cleanup
The AWS SAM CLI provides a command `sam delete` that simplifies the process of deleting the resources created by your SAM application. It deletes the AWS CloudFormation stack, the artifacts that were packaged and deployed to Amazon S3 and Amazon ECR, and the AWS SAM template file.

## Running the Cleanup Command
To delete your SAM application, navigate to your project directory (where your SAM template file is located) in your terminal and run the following command:
```
sam delete
```

## Non-Interactive Mode
If you want to run the sam delete command in non-interactive mode, you can use the `--no-prompts option`.
```
sam delete --no-prompts
```