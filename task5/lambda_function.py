import json
import boto3
import requests
import os
import datetime
import logging

# Setup basic logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Environment Variables (set these in Lambda config)
S3_BUCKET = os.environ.get('S3_BUCKET')
API_URL = os.environ.get('API_URL', 'https://api.coindesk.com/v1/bpi/currentprice.json')

def lambda_handler(event, context):
    logger.info("Lambda function started.")
    
    try:
        # Fetch data from public API
        response = requests.get(API_URL)
        response.raise_for_status()  # raise an exception for bad responses
        
        data = response.json()
        logger.info(f"Fetched data from API: {data}")
        
        # Create a unique filename based on current time
        now = datetime.datetime.utcnow()
        filename = f"crypto-data/data_{now.strftime('%Y-%m-%dT%H-%M-%S')}.json"
        
        # Upload to S3
        s3_client = boto3.client('s3')
        s3_client.put_object(
            Bucket=S3_BUCKET,
            Key=filename,
            Body=json.dumps(data),
            ContentType='application/json'
        )
        
        logger.info(f"Data successfully saved to s3://{S3_BUCKET}/{filename}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Success', 'filename': filename})
        }
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data from API: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
