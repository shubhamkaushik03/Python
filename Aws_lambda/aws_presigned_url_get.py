from botocore.client import Config
import boto3

def lambda_handler(event, context):

    s3 = boto3.client('s3', region_name="us-east-1")

    bucket_name = 'testimagesbucketupload'
    presigned_url = s3.generate_presigned_url('get_object',
                                Params={'Bucket': bucket_name,
                                        'Key': "GetPersonaPhoto.jpg"},
                                ExpiresIn=3600)
    return presigned_url
    

    
