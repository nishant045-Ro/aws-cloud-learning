import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

instance_id = 'i-096f7b63fe1501d6e'

ec2.start_instances(InstanceIds=[instance_id])
print("Instance " + instance_id + " is starting!")