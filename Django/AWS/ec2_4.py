import boto3
from datetime import datetime, timedelta

def create_instance():
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

cloudwatch = boto3.client('cloudwatch')

result = cloudwatch.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[
                {
                'Name': 'InstanceId',
                'Value': 'i-0a3c104c312a7019d'
                },
            ],
            StartTime=datetime.utcnow() - timedelta(seconds=600),
            EndTime=datetime.utcnow(),
            Period=300,
            Statistics=[
                'Average',
            ],
            Unit='Percent'
        )

cpu_avg =  result['Datapoints'][0]['Average']
print(str(cpu_avg))

if cpu_avg > 70:
    create_instance

print(result)