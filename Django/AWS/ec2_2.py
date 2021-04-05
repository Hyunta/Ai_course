import boto3

ec_client = boto3.client('ec2')

ec2_desc = ec_client.describe_instances()

for ec2_resv in ec2_desc['Reservations']:
    ec2_instance = ec2_resv['Instances'][0]
    ec2_instance_id = ec2_instance['InstanceId']
    ec2_state = ec2_instance['State']['Name']
    print(ec2_instance_id)
    print(ec2_state)

    if (ec2_state == 'stopped') :
        response = ec_client.start_instances(
            InstanceIds=[
                ec2_instance_id
            ],
        )
        print(response)
    print()