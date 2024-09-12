import boto3

aws_management = boto3.session.Session('default')

client = boto3.client('ec2')

list = client.describe_instances()

for reservation in list['Reservations']:
    for instance in reservation['Instances']:
        if 'Tags' in instance:
            for tag in instance['Tags']:
                print(f"The Ec2 Instances Name(tag) is {tag['Value']}")