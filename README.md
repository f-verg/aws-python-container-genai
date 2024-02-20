# aws-lambda-python-container
Lambda container with Langchain, boto3 and postgres client

## Test the container locally

Build the new image
```bash
docker build --platform linux/amd64 -t lambda-python-container:dev .
```

Run the container locally
```bash
docker run --platform linux/amd64 -p 9000:8080 lambda-python-container:dev
```

From a separate terminal, invoke the lambda:
```bash
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

## Deploy the image to ECR and Lambda

**Login to ECR:**
```bash
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin <YOUR-ACCOUNT-NO>.dkr.ecr.us-east-1.amazonaws.com
```

**Create a repository for the container on ECR:**
```bash
aws ecr create-repository --repository-name <YOUR-REPO-NAME> --region eu-central-1 --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
```

**Copy the new ECR Repository URI and then tag the new image:** 
```bash
docker tag lambda-python-container:dev <ECRrepositoryUri>:latest
```

**Push the container image:**
```bash
docker push <YOUR-ACCOUNT-NO>.dkr.ecr.eu-central-1.amazonaws.com/<YOUR-REPO-NAME>:latest
```

Create an execution role for the function, if you don't already have one. You need the Amazon Resource Name (ARN) of the role in the next step.

**Create the Lambda function. For ImageUri, specify the repository URI from earlier. Make sure to include :latest at the end of the URI.**
```bash
aws lambda create-function \
  --function-name lambda-python-container \
  --package-type Image \
  --code ImageUri=<YOUR-ACCOUNT-NO>.dkr.ecr.eu-central-1.amazonaws.com/<YOUR-REPO-NAME>:latest \
  --role arn:aws:iam::<YOUR-ACCOUNT-NO>:role/<LAMBDA-ROLE-NAME>
```

**Invoke the lambda function**
```bash
aws lambda invoke --function-name lambda-python-container response.json
```

You can see the response from your Lambda function in the response.json file
