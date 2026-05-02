import boto3
import datetime

s3 = boto3.client('s3')
bucket = 'nishant-practice-bk'

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d-%H-%M")

log_content = "Backup run at: " + date
with open('backup_log.txt', 'w') as f:
    f.write(log_content)

filename = "backup-" + date + ".txt"
s3.upload_file('backup_log.txt', bucket, filename)

print("Backup completed at: " + date)
print("File saved as: " + filename)