import boto3
from pprint import pprint

aws_management = boto3.session.Session('default')

ec2_client = boto3.client('ec2')

list = ec2_client.describe_instances()['Reservations']

for instance in list:
    for tags in instance['Instances']:
        for name in tags['Tags']:
            print(f"The Ec2 Instances Name(tag) is {name['Value']}")