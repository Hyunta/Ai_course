import boto3

BUCKET = "khtbucket23"
KEY = "C:\DKU_DBMS\DB server\cartoon/20201120102033_15217e7a69065e8805f3666c89301e03_IMAG01_2.jpg"


def detect_text(bucket, key):
    client = boto3.client('rekognition')

    response = client.detect_text(Image={'S3Object': {'Bucket': bucket, 'Name': key}})

    textDetections = response['TextDetections']

    return textDetections

for text in detect_text(BUCKET, KEY):
    print('Detected text:' + text['DetectedText'])
    print
    ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
    print('Id: {}'.format(text['Id']))
    if 'ParentId' in text:
        print('Parent Id: {}'.format(text['ParentId']))
    print('Type:' + text['Type'])
    print()