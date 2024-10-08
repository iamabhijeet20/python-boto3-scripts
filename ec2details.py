import boto3

aws_management = boto3.session.Session('default')

ec2_client = boto3.client('ec2')

list = ec2_client.describe_instances()['Reservations']

for instances in list:
    for each_instance in instances['Instances']:
        for name in each_instance['Tags']:
            tag_name = name.get('Value', 'no Tag name')                                    ### tag_name = name

            instance_id = each_instance.get('InstanceId', 'No Instance Id')                ### instance_id = id

            instance_type = each_instance.get('InstanceType', 'No instance Type')          ### instance_type = InstanceType

            Az = each_instance['Placement']
            AvailabilityZone = Az.get('AvailabilityZone', 'No Az available')               ### AvailabilityZone = Az

            PublicIp = each_instance.get('PublicIpAddress', 'No Public Address')           ### PublicIp = PublicIpAddress

            KeyName = each_instance.get('KeyName', 'No Key Name')                          ### KeyName = KeyName

        for network in each_instance['NetworkInterfaces']:
            for groups in network['Groups']:
                GroupId = (groups.get('GroupId','No Group ID'))                            ### GroupId = GroupId
                GroupName = (groups.get('GroupName', 'No Group Name'))                     ### GroupName = GroupName

            VpcId = each_instance.get('VpcId','No VPC Id')                                 ### VpcId = VpcId


        # print(tag_name,instance_id,instance_type,AvailabilityZone,PublicIp,KeyName,GroupId,GroupName,VpcId)           