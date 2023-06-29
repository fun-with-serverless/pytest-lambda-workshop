# Identifying What to Test in Your Code
When writing unit tests for your code, it's essential to identify the key areas that require testing. This often includes areas where your code interacts with external inputs, produces outputs, processes logic, interacts with data, or includes control flow elements such as loops. Here are some questions to help guide what parts of your code should be tested:

## Input
* What's your input? What kind of data are you expecting?
* What will happen if any of the parameters are null?
* What will happen if there's a mismatch in the parameters?
* How does your code handle parameters of a different type than expected?
* How does your code handle parameters of invalid size (length)?

## Logic
* What will happen if you output null?
* What will happen if your code doesn't provide its output on time?
* Does your logic handle all possible outputs defined?
* Are all branches of your logic still relevant and necessary?

## Loops
* Are you sure your code will always exit the loop?
* Are you sure the loop is necessary?
* Does your code exit the loop quickly upon encountering an error?
* Does your code avoid entering the loop if it's not necessary?

## Control Flow
* Have you tested all branches in your code?
* Do you need branching in your code?
