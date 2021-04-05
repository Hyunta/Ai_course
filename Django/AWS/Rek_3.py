import boto3

def detect_text(photo, bucket ,region="ap-northeast-2"):
    rekognition = boto3.client("rekognition", region)

    response = rekognition.detect_text(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': photo
            }
        }
    )

    textDetections = response['TextDetections']
    print('Detected text\n----------')
    for text in textDetections:
        print('Detected text:' + text['DetectedText'])
        print('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
        print('Id: {}'.format(text['Id']))
        if 'ParentId' in text:
            print('Parent Id: {}'.format(text['ParentId']))
        print('Type:' + text['Type'])
        print()
    return len(textDetections)


def main():
    bucket = 'khtbucket23'
    photo = 'text.jpg'
    text_count = detect_text(photo, bucket)
    print("Text detected: " + str(text_count))


if __name__ == "__main__":
    main()
    print()
