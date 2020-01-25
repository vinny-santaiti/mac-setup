# pip install boto3==1.4.8
import boto3

bucket = 'bucket_name'
prefix = 'folder_name/'

client = boto3.client('s3', aws_access_key_id="access_key", aws_secret_access_key="secret_key")

def list_files(client, bucket, prefix):
    response = client.list_objects(Bucket=bucket, Prefix=prefix)
    for content in response.get('Contents', []):
        yield content.get('Key')

files = list_files(client, bucket, prefix)
for file in files:
    print (file)

s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket)
for obj in bucket.objects.filter(Prefix=prefix):  # bucket.objects.all()
    print(obj.key)
