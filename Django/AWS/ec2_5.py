import boto3
from datetime import datetime, timedelta

cloudwatch = boto3.client('cloudwatch')

result = cloudwatch.get_metric_statistics(
            Namespace='AWS/RDS',
            MetricName='CPUUtilization',
            Dimensions=[
                {
                'Name': 'DBInstanceIdentifier',
                'Value': 'database-2'
                },
            ],
            StartTime=datetime(2020, 12, 11) - timedelta(seconds=600),
            EndTime=datetime(2020, 12, 11),
            Period=300,
            Statistics=[
                'Average',
            ],
            Unit='Percent'
        )

print(result)