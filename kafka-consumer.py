from kafka import KafkaConsumer
from time import sleep
from json import dumps, loads
import json
import boto3

consumer = KafkaConsumer('[instane name]', 
                         bootstrap_servers=['[your public EC2 port]:9092'],
                         value_deserializer=lambda x: loads(x.decode('utf-8')))

s3 = boto3.client('s3')
bucket_name = '[bucket name]'

try:
  for count, message in enumerate(consumer):
    message_json = dumps(message.value)
    object_key = f"stock_market_{count}.json"
    s3.put_object(Body=message_json, Bucket=bucket_name, Key=object_key)
    print(f"Uploaded {object_key} with message: {message_json} to S3 bucket {bucket_name}")
except Exception as e:
  print(f"An error occurred: {e}")
