import boto3
import datetime

ec2 = boto3.client('ec2', region_name='us-east-1')
s3 = boto3.client('s3')
bucket = 'nishant-practice-bk'

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d-%H-%M")

response = ec2.describe_instances()
report = "Health Check - " + date + "\n"

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        report += "ID: " + instance['InstanceId'] + "\n"
        report += "State: " + instance['State']['Name'] + "\n"
        report += "IP: " + str(instance.get('PublicIpAddress', 'No IP')) + "\n"
        report += "---\n"

print(report)

filename = "health-" + date + ".txt"
with open(filename, 'w') as f:
    f.write(report)

s3.upload_file(filename, bucket, filename)
print("Report saved to S3!")