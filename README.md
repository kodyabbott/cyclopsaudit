# Cyclops Audit

The Cyclops Audit project is a Lambda function designed to perform specific auditing tasks. This document provides instructions on how to clone, build, and deploy the project using AWS Serverless Application Model (SAM).

## Prerequisites

- AWS CLI installed and configured with necessary permissions
- AWS SAM CLI
- Python 3.8 or higher

## Cloning the Repository

Clone the repository using the following command:

```bash
git clone https://github.com/kodyabbott/cyclopsaudit.git
cd cyclopsaudit
```
## Building the Project

Inside the project directory, build the Lambda function using the SAM CLI:

```bash
sam build
```

This command will download the necessary dependencies and prepare the build artifacts as defined in the requirements.txt and template.yaml.

## Deploying the Project

Deploy the Lambda function using the following command:

```bash
sam deploy --guided
```

Follow the on-screen instructions to complete the deployment. This command will package and deploy the application to AWS, creating or updating the necessary resources.

## Testing the Lambda Function

You can invoke the Lambda function locally by using the following command:

```bash
sam local invoke
```

Contributing

For contributions, please create pull requests and adhere to the code standards defined in the project.