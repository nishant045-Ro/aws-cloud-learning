import boto3

s3 = boto3.client('s3')

print("My S3 Buckets:")
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(" - " + bucket['Name'])

s3.upload_file('myfirst.py', 'nishant-practice-bk', 'myfirst.py')
print("\nFile uploaded to S3 successfully!")