#!/bin/bash
echo "Backup started..."
aws s3 sync cloudproject/ s3://nishant-practice-bk/backup/
echo "Backup completed!"