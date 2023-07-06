# Welcome to the "Crisis at the Concert" Lambda Testing Workshop

![Crisis at the Concert A painting by Picasso](./images/logo-crisis-at-the-opera.png){ align=left }

Welcome to the "Crisis at the Concert" workshop! This event is designed to provide hands-on experience with unit testing, mocking AWS services, and local testing of AWS Serverless Application Model (SAM) applications.

The workshop is based on a fun and engaging scenario, "Crisis at the Concert", where you will play the role of an engineer tasked with fixing a malfunctioning concert event management system just before the big event.

The concert management system is a Serverless Application Model (SAM) application with features like ticket sales, event scheduling, and artist information. However, it's currently experiencing various "problems" that need to be addressed.

Your goal is to "save the concert" by identifying and fixing these issues using a range of testing and debugging tools.

## Workshop Curriculum
The workshop is divided into three main parts:

1. Unit Testing for AWS Lambda (1 hour):
In this section, you will learn about unit testing, its importance, and how to apply it to AWS Lambda functions. You will write your own unit tests to identify issues in the concert application.

2. Mocking AWS Services with Moto (1 hour):
Here, you'll learn about the Python library Moto and how it can be used to mock AWS services for testing purposes.

3. Local Testing with AWS SAM (30 minutes):
In the final part of the workshop, you'll learn about AWS SAM and how it can be used for local testing of AWS services like API Gateway, Lambda, and DynamoDB. You will run the concert application locally, interact with the locally running application, inspect logs, and debug issues.

By the end of this workshop, you should have a solid understanding of how to write unit tests for AWS Lambda functions, mock AWS services using Moto, and conduct local testing with AWS SAM. You'll also have the experience of applying these techniques to a practical scenario, giving you confidence to apply them in your own projects.

Let's dive in and save the concert!

## Prerequisites
Before you start, make sure you have the following:

* Basic knowledge of AWS, including AWS Lambda, DynamoDB and AWS SAM.
* Familiarity with Python programming language.
* AWS account with appropriate permissions to create and manage AWS Lambda functions, DynamoDB tables and CF stack creation.
* Python 3.9, AWS CLI, and AWS SAM CLI installed on your local machine.
* Clone `https://github.com/aws-hebrew-book/pytest-lambda-workshop` to your development machine.

!!! note

    We highly recommend using [Cloud9](https://aws.amazon.com/cloud9/) as your temporary development environment. It already comes equipped with the necessary prerequisites; however, you will need to update your Python version to 3.9. After cloning the GitHub repository, run `./update_python_on_cloud9.sh` to install Python 3.9.

We're excited for you to join us in this hands-on workshop. Let's get started!