import json
import boto3
import base64

rekognition = boto3.client('rekognition', region_name='us-east-1')

CORS_HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'POST, OPTIONS'
}


def lambda_handler(event, context):
    try:
        http_method = event['requestContext']['http']['method']
    except:
        return {'statusCode': 400, 'body': 'Error'}

    if http_method == 'OPTIONS':
        return {'statusCode': 200, 'headers': CORS_HEADERS, 'body': ''}
    
    if http_method == 'POST':
        try:
            image_data = event['body'].strip()
            missing_padding = len(image_data) % 4
            if missing_padding:
                image_data += '=' * (4 - missing_padding)
            image_bytes = base64.b64decode(image_data)
        except Exception as e:
            return {
                'statusCode': 400,
                'headers': CORS_HEADERS,
                'body': json.dumps(f"Base64 error: {str(e)}")
            }

        try:
            response = rekognition.detect_labels(
                Image={'Bytes': image_bytes},
                MaxLabels=10,
                MinConfidence=80.0
            )
            
            labels = [label['Name'] for label in response['Labels']]
            
            return {
                'statusCode': 200,
                'headers': CORS_HEADERS,
                'body': json.dumps({'labels': labels})
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'headers': CORS_HEADERS,
                'body': json.dumps(f"Rekognition error: {str(e)}")
            }

    return {'statusCode': 405, 'headers': CORS_HEADERS, 'body': 'Method not supported'}