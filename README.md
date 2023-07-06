# 🎸 Crisis at the Concert
<p align="center">
   <img src="./docs/images/logo-crisis-at-the-opera.png" alt="[Crisis at the Concert A painting by Picasso]"/>
</p>

Welcome to the "Crisis at the Concert" workshop! This event is designed to provide hands-on experience with unit testing, mocking AWS services, and local testing of AWS Serverless Application Model (SAM) applications.

The workshop is based on a fun and engaging scenario, "Crisis at the Concert", where you will play the role of an engineer tasked with fixing a malfunctioning concert event management system just before the big event.

The concert management system is a Serverless Application Model (SAM) application with features like 🎟️ ticket sales, event scheduling, and artist information. However, it's currently experiencing various "problems" 🚧 that need to be addressed.

Your goal is to "save the concert" 🎸 by identifying and fixing these issues using a range of testing and debugging tools.

# 🎓 Workshop Curriculum
The workshop is divided into three main parts:

1. Unit Testing for AWS Lambda:
In this section, you will learn about unit testing, its importance, and how to apply it to AWS Lambda functions. You will write your own unit tests to identify issues in the concert application.

2. Mocking AWS Services with Moto:
Here, you'll learn about the Python library Moto and how it can be used to mock AWS services for testing purposes. You will update the Lambda functions to fix the issues identified in the concert application and then use Moto to mock the AWS services used by these functions.

3. Local Testing with AWS SAM:
In the final part of the workshop, you'll learn about AWS SAM and how it can be used for local testing of AWS services like API Gateway, Lambda, and DynamoDB. You will run the concert application locally, interact with the locally running application, inspect logs, and debug issues.

By the end of this workshop, you should have a solid understanding of how to write unit tests for AWS Lambda functions, mock AWS services using Moto, and conduct local testing with AWS SAM. You'll also have the experience of applying these techniques to a practical scenario, giving you confidence to apply them in your own projects.

Let's dive in and save the concert!

👉 **[The workshop is available online](http://pytest-lambda-workshop.s3-website-us-west-2.amazonaws.com/)** 👈

# 🖥️ How to run locally
1. Make sure you have `poetry` installed.
2. Run `poetry install`.
3. Run `poetry run mkdocs serve` to have the workshop running locally.
