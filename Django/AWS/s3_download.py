import boto3
from botocore.exceptions import ClientError


def download_from_s3(object_name, bucket_name, file_name=None):
    if file_name is None:
        file_name = object_name
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, object_name, file_name)


def upload_to_s3(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        print(e)
        return False
    return True




#upload_file('ec2.py','sjbbuck')
download_from_s3('test','sjbbuck', 'test.py')