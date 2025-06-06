import boto3
import os

s3 = boto3.client('s3', endpoint_url='http://host.docker.internal:4566')

def handler(event, context):
    source_bucket = 's3-start'
    dest_bucket = 's3-finish'

    for record in event['Records']:
        key = record['s3']['object']['key']
        copy_source = {'Bucket': source_bucket, 'Key': key}
        s3.copy_object(Bucket=dest_bucket, CopySource=copy_source, Key=key)
