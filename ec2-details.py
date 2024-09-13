import boto3

aws_management = boto3.session.Session('default')

ec2_client = boto3.client('ec2')

list = ec2_client.describe_instances()['Reservations']

for instances in list:
    for each_instance in instances['Instances']:
        for name in each_instance['Tags']:
            tag_name = name['Value']                                ### tag_name = name

            instance_id = each_instance['InstanceId']               ### instance_id = id

            instance_type = each_instance['InstanceType']           ### instance_type = InstanceType

            
            print(tag_name,instance_id)           