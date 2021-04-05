import boto3

BUCKET = "khtbucket23"
FILE = "test2.jpg"
FEATURES_BLACKLIST = ("Landmarks", "Emotions", "Pose", "Quality", "BoundingBox", "Confidence")

def detect_faces(bucket, file, attributes=['ALL'], region="ap-northeast-2"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.detect_faces(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": file,
            }
        },
        Attributes=attributes,
    )
    return response['FaceDetails']

for face in detect_faces(BUCKET, FILE):
    print("Face ({Confidence}%)".format(**face))
    # emotions
    for emotion in face['Emotions']:
        print("  {Type} : {Confidence}%".format(**emotion))
    print()
    # quality
    for quality, value in face['Quality'].items():
        print("  {quality} : {value}".format(quality=quality, value=value))
    print()
    # facial features
    for feature, data in face.items():
        if feature not in FEATURES_BLACKLIST:
            for key, value in data.items():
                print("  {feature}({key}) :{value}".format(feature=feature, key=key, value=value))