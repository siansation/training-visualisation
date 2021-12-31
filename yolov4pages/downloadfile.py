import boto3

model = "ssd//"
filename = "ssd_training_log_resnet18.csv"  #"yolov4_training_log_resnet18.csv"

s3_client = boto3.client('s3', endpoint_url='http://127.0.0.1:9000',aws_access_key_id='minioadmin',
    aws_secret_access_key='minioadmin',region_name='us-east-1' )

s3_client.download_file('logs', filename, "C:\\Users\\User\\Documents\\ml_visualize\yolov4pages\\newssdfile3.csv")

