import boto3

ec2_client = boto3.client('ec2')

response = ec2_client.run_instances(
    ImageId='ami-05d56404106a1706c',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
    SubnetId='subnet-b5c069de',
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sda1',
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': 30,
                'VolumeType': 'gp2'
            },
        },
    ],
    SecurityGroupIds=[
        'sg-45b68c3c',
    ],
    KeyName='win_vol'
)