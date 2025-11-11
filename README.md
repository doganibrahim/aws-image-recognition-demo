# AWS Rekognition Image Analysis
A simple web application that analyzes images using AWS Rekognition to detect objects and labels.

## Technologies
- HTML/CSS/JavaScript
- AWS Lambda (Python 3.12)
- AWS Rekognition
- AWS API Gateway

## Setup
1. Create an AWS Lambda function in **us-east-1** region
2. Upload `lambda_function.py` code to Lambda
3. Add **AmazonRekognitionReadOnlyAccess** policy to Lambda execution role
4. Create an HTTP API Gateway and integrate with Lambda
5. Configure CORS on API Gateway
6. Update `API_ENDPOINT` in `index.html` with your API Gateway URL
7. Open `index.html` in a browser or serve via a live server

## Usage
1. Select an image
2. Click **"Analyze"** button
3. View detected labels

## AWS Configuration
- **Region:** us-east-1 (N. Virginia)
- **Lambda Runtime:** Python 3.12
- **API Gateway:** HTTP API with CORS enabled
- **Required Permissions:** Rekognition:DetectLabels

## Note
The Lambda function works in **us-east-1** region. Ensure your API Gateway and Lambda are in the same region.

## Demo
Upload an image and get instant AI-powered object detection results.