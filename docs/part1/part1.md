# Unit Testing and the "Crisis at the Concert"

## Introduction to Unit Testing
Unit testing is a software testing method by which individual parts of the code are tested to determine whether they are fit for use. In the context of AWS Lambda, a "unit" is often a single function or method. Unit tests are automated tests written and run by software developers to ensure that a particular section of an application (known as the "unit") meets its design and behaves as expected.

Unit tests have several benefits:

* **Detect problems early**: Unit tests can catch changes that break existing functionality. This makes issues easier and cheaper to fix.
* **Simplify integration**: By testing parts of a system in isolation, you can ensure that each part is working correctly before combining them. This can prevent bugs from being introduced during integration.
* **Documentation**: Unit tests can serve as documentation by example, showing how a piece of code is expected to behave.
* **Design**: Writing unit tests can help drive a better design by encouraging modular, decoupled code.

## Introduction to the "Crisis at the Concert"
Welcome to the "Crisis at the Concert" scenario! This scenario presents a malfunctioning concert event management system built with AWS Serverless Application Model (SAM). The application includes features such as ticket sales, event scheduling, and artist information. However, there's a crisis: the concert is about to happen, but the system is malfunctioning!

Your mission, should you choose to accept it, is to save the concert. To do this, you'll need to write unit tests to uncover the issues in the system, debug the code, and fix the problems to ensure that the concert can go ahead as planned. This will be a challenging but rewarding task, as you will learn and apply unit testing techniques in a real-world scenario.

In the following sections, you will explore the concert application, write unit tests to identify issues, and use these tests to guide your debugging and problem-solving efforts. Good luck!

## Deploying and Testing the "Crisis at the Concert" Application
In this part of the workshop, we will deploy our SAM application and test it by calling its API.

### Step 1: Deploy the SAM Application
First, let's deploy our SAM application. Open your terminal and navigate to the root directory of the "Crisis at the Concert" project.

Ensure that you have AWS credentials set up on your local machine. If you haven't done this yet, you can follow this [guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) to set them up.

Now, let's build our SAM application:
```bash
sam build
```

Once the build is successful, deploy the application:
```
sam deploy --guided
```
During the guided deployment, you'll be prompted to enter some configuration parameters (e.g., stack name, AWS Region). Once you've entered these details, the deployment will begin. After a few minutes, your application should be deployed, and you'll see output similar to this:

```
CloudFormation outputs from deployed stack
-----------------------------------------------------
Outputs
-----------------------------------------------------
Key                 ConcertApiURL
Description         API Gateway endpoint URL for Prod stage for Concert function
Value               https://xxxxxx.execute-api.us-west-2.amazonaws.com/Prod/concert/
-----------------------------------------------------
```

Keep note of the `Value` under `ConcertApiURL`, as this is the endpoint we'll use to test our application.

### Step 2: Test the Application
Now that we've deployed our application, it's time to test it.

Using a tool like Postman, Insomnia, or even curl in your terminal, make a GET request to the `ConcertApiURL` endpoint.

Here's an example using curl:
```bash
curl https://xxxxxx.execute-api.us-west-2.amazonaws.com/Prod/concert/
```

Replace `https://xxxxxx.execute-api.us-west-2.amazonaws.com/Prod/concert/` with your actual `ConcertApiURL`.

You should receive a JSON response from the server. If there's a problem with the application, the response should help you identify what's wrong.

Remember, our application is intentionally "broken" as part of the "Crisis at the Concert" scenario. Any errors or unexpected responses are opportunities for you to practice debugging and problem-solving!