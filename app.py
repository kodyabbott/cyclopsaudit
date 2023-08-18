import json
import boto3
import os
from datetime import datetime, timedelta

# AWS S3 client
s3_client = boto3.client('s3')

# Function to read data from S3
def read_data_from_s3(bucket_name, key):
    response = s3_client.get_object(Bucket=bucket_name, Key=key)
    content = response['Body'].read().decode('utf-8')
    return json.loads(content)

# Function to write data to S3
def write_data_to_s3(bucket_name, key, data):
    s3_client.put_object(Body=json.dumps(data), Bucket=bucket_name, Key=key)

# Main Lambda handler
def lambda_handler(event, context):
    # Read the TARGET_S3_BUCKET from environment variables
    bucket_name = os.environ['TARGET_S3_BUCKET']

    # Read data from S3
    describe_images_data = read_data_from_s3(bucket_name, 'describe-images.json')
    
    # Given date to treat as today's date
    given_date = "2023-02-01T00:00:00.000Z"
    today_date = datetime.fromisoformat(given_date.replace("Z", "+00:00"))
    target_date_120_days = today_date + timedelta(days=120)
    target_date_90_days = today_date + timedelta(days=90)

    # Answer 1
    deprecated_images_count = sum(1 for image in describe_images_data['Images'] if 'DeprecationTime' in image and datetime.fromisoformat(image['DeprecationTime'].replace("Z", "+00:00")) <= target_date_120_days)
    answer_1 = {"Answer": deprecated_images_count}
    write_data_to_s3(bucket_name, 'answer_1.json', answer_1)

    # Answer 2
    windows_images_expiring = [image['Name'] for image in describe_images_data['Images'] if image.get('Platform') == 'windows' and 'DeprecationTime' in image and datetime.fromisoformat(image['DeprecationTime'].replace("Z", "+00:00")) <= target_date_90_days]
    answer_2 = {"Answer": windows_images_expiring}
    write_data_to_s3(bucket_name, 'answer_2.json', answer_2)

    # Answer 3
    # Check for images that contain both "bottlerocket" and "k8s" in either the Name or Description fields (case-insensitive)
    bottlerocket_images = sorted(
        (image for image in describe_images_data['Images']
        if 'bottlerocket' in image.get('Name', '').lower() or 'bottlerocket' in image.get('Description', '').lower()
        if 'k8s' in image.get('Name', '').lower() or 'k8s' in image.get('Description', '').lower()),
        key=lambda x: x['CreationDate'], reverse=True
    )
    bottlerocket_images_list = [{"Name": image['Name'], "CreationDate": image['CreationDate']} for image in bottlerocket_images]
    answer_3 = {"Answer": bottlerocket_images_list}
    write_data_to_s3(bucket_name, 'answer_3.json', answer_3)

    return {
        'statusCode': 200,
        'body': json.dumps('Processing completed successfully!')
    }
