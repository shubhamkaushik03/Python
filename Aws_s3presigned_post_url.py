import json
import boto3


def lambda_handler(event, context):
    print(event)
    s3 = boto3.client('s3', region_name='us-east-1')
    bucket_name = 'testimagesbucketupload'
   
    URL = s3.generate_presigned_post(
            Bucket= bucket_name, 
            Key="${filename}", 
            ExpiresIn=3600)
    data = {"url": URL['url'], "fields": URL['fields']}
    print(type(data))
    # print(data)
    return data
   
        
