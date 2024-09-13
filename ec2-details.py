import boto3

aws_management = boto3.session.Session('default')

ec2_client = boto3.client('ec2')

list = ec2_client.describe_instances()['Reservations']

for instances in list:
    for each_instance in instances['Instances']:
        for name in each_instance['Tags']:
            tag_name = name['Value']
            
            print(tag_name)           