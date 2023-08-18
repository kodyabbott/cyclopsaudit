# Cyclops Audit

The Cyclops Audit project is a Lambda function designed to perform specific auditing tasks. This document provides instructions on how to clone, build, and deploy the project using AWS Serverless Application Model (SAM).

## Prerequisites

Before proceeding, ensure you have the following:

- AWS CLI installed and configured with necessary permissions
- AWS SAM CLI
- S3 bucket that contains `describe-images.json`
- IAM user with the following permissions (recommendation to use administrator):
    - cloudformation:* to create CloudFormation stack
    - lambda:* to create Lambda function
    - iam:* to create IAM roles
    - s3:* to read and write from the specified S3 bucket
    - logs:* to write logs to CloudWatch
- Default values are obtained from the following configuration files:
    - ~/.aws/config – Your general AWS account settings.
    - ~/.aws/credentials – Your AWS account credentials.

## Cloning the Repository

Clone the repository using the following command:

```bash
git clone https://github.com/kodyabbott/cyclopsaudit.git
cd cyclopsaudit
```

## Updating the Bucket Name

Open the both the `template.yaml` and `samconfig.toml` files and replace `your-s3-bucket-name` with the name of the S3 bucket containing the file `describe-images.json`. This bucket will also store the output from the Lambda function as well as the AWS SAM files.

## Building the Project

Inside the project directory, build the Lambda function using the SAM CLI:

```bash
sam build
```

This command will download the necessary dependencies and prepare the build artifacts as defined in the `requirements.txt and `template.yaml`.

## Deploying the Project

Deploy the Lambda function using the following command:

```bash
sam deploy
```

Follow the on-screen instructions to complete the deployment. 
This command will package and deploy the application to AWS, creating or updating the necessary resources.

## Testing the Lambda Function

Test the deployed Lambda function through the AWS Console:

1. Go to AWS Console > Lambda Functions
2. Select the Lambda function starting with `ec2-images-analysis-AnalyzeEC2ImagesFunction-`
3. Click the `Test` tab and click the `Test` button. (no need to enter any JSON for the Test event)       
    
    > Note: The `TARGET_S3_BUCKET` environment variable should be set to the location of `describe-images.json`, as defined in the `Update bucket name` step from above.

4. Goto your `TARGET_S3_BUCKET` and you will find `answer_1.json`, `answer_2.json`, and `answer_3.json` which you can then download.

## Deleting the Lambda Function

1. Go to AWS Console > CloudFormation
2. Select `ec2-images-analysis`
3. Click `Delete` where you can then confirm  to delete the stack which will delete the Lambda function

Contributing

For contributions, please create pull requests and adhere to the code standards defined in the project.