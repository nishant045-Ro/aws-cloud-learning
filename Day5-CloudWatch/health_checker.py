import boto3
from datetime import datetime

# ================================
# HEALTH CHECKER + CLOUDWATCH
# ================================

# Your details
REGION = 'us-east-1'
INSTANCE_ID = 'YOUR_INSTANCE_ID'  # Replace this!

# Connect to AWS
ec2 = boto3.client('ec2', region_name=REGION)
cloudwatch = boto3.client('cloudwatch', region_name=REGION)

def check_ec2_health():
    """Check if EC2 instance is running"""
    response = ec2.describe_instances(
        InstanceIds=[INSTANCE_ID]
    )
    
    # Get instance state
    state = response['Reservations'][0]['Instances'][0]['State']['Name']
    print(f"🔍 Instance state: {state}")
    
    return state

def send_metric_to_cloudwatch(health_value):
    """Send health metric to CloudWatch"""
    cloudwatch.put_metric_data(
        Namespace='MyApp/HealthChecker',
        MetricData=[
            {
                'MetricName': 'ServerHealth',
                'Value': health_value,
                'Unit': 'Count',
                'Dimensions': [
                    {
                        'Name': 'InstanceId',
                        'Value': INSTANCE_ID
                    }
                ]
            }
        ]
    )

def main():
    print("=" * 40)
    print("🏥 HEALTH CHECKER RUNNING")
    print(f"⏰ Time: {datetime.now()}")
    print("=" * 40)
    
    # Check health
    state = check_ec2_health()
    
    # Send result to CloudWatch
    if state == 'running':
        print("✅ Server is HEALTHY!")
        send_metric_to_cloudwatch(1)  # 1 = healthy
    else:
        print("❌ Server is UNHEALTHY!")
        send_metric_to_cloudwatch(0)  # 0 = unhealthy
    
    print("📊 Metric sent to CloudWatch!")
    print("=" * 40)

# Run the checker
main()