import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

response = ec2.describe_instances()

print("My EC2 Instances:")
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("ID: " + instance['InstanceId'])
        print("State: " + instance['State']['Name'])
        print("Type: " + instance['InstanceType'])
        print("IP: " + str(instance.get('PublicIpAddress', 'No IP')))
        print("---")

print("Done!")