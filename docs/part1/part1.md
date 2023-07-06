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
In this segment of the workshop, we will deploy our SAM application and validate its functionality by invoking its API. The application is split across two directories: `crisis-at-the-concert-err` and `crisis-at-the-concert-fixed`. The `err`-suffixed directory hosts the application that requires your attention and problem-solving skills, while the `fixed` directory contains the final solution, complete with all the implemented tests.

### Step 1: Deploy the SAM Application
First, let's deploy our SAM application. Open your terminal and navigate to the root directory of the workshop project. From there, proceed to the `crisis-at-the-concert-err` directory.

!!! note

    This workshop assumes that you are working in the `us-east-1` region. If you are working in a different region, please update the `REGION` value in `consts.py`. Additionally, modify the SAM deployment command to include the appropriate region, e.g., sam `deploy --region ....`

Ensure that you have AWS credentials set up on your local machine. If you haven't done this yet, you can follow this [guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) to set them up.

Now, let's build our SAM application:
```bash
sam build
```

!!! note

    If you are using a shared AWS environment, it is recommended that you change the default stack name to avoid conflicts with others participating in the same workshop. Simply use `sam deploy --stack-name crisis-at-the-concert-${USER}`.

Once the build is successful, deploy the application:
```
sam deploy
```

After a few minutes, your application should be deployed, and you'll see output similar to this:

```
CloudFormation outputs from deployed stack
-----------------------------------------------------
Outputs
-----------------------------------------------------
Key                 BookTicketFunctionApi
Description         Here's an example of how to book a ticket using curl
Value               curl -X POST https://xxxx.execute-api.us-east-1.amazonaws.com/Prod/book_ticket/ -H "Content-Type: application/json" -d '{"name": "Noa Kiril","ticket_count": "50"}' 
-----------------------------------------------------
```

Keep note of the `Value` under `BookTicketFunctionApi`, as this is the endpoint we'll use to test our application.

### Step 2: Test the Application
Now that we've deployed our application, it's time to test it.

Using a tool like Postman, Insomnia, or even curl in your terminal, make a GET request to the `BookTicketFunctionApi` endpoint.
You can use the example supplied as part of the value.
Here's an example using curl:
```bash
curl -X POST https://xxxx.execute-api.us-east-1.amazonaws.com/Prod/book_ticket/ -H "Content-Type: application/json" -d '{"name": "Noa Kiril","ticket_count": "50"}'
```

Replace `https://xxxxxx.execute-api.us-west-2.amazonaws.com/Prod/book_ticket/` with your actual URL.

You should receive a JSON response from the server indicating an error.

Remember, our application is intentionally "broken" as part of the "Crisis at the Concert" scenario. Any errors or unexpected responses are opportunities for you to practice debugging and problem-solving!