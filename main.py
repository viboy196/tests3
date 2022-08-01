import boto3
from botocore.client import Config

AWS_ACCESS_KEY_ID = '009b644845be7b092701'
AWS_SECRET_ACCESS_KEY = 'NpihhCkd6Z/5iNQ/HMM3vI3DCaAoUSs+/VcPWtmk'
END_POINT = 'https://s3-north.viettelidc.com.vn'
BUCKET_NAME = 'dichvunuoc'
FILE_NAME = 'anh2.jpg'

s3 = boto3.resource('s3',
endpoint_url = END_POINT,
aws_access_key_id=AWS_ACCESS_KEY_ID,
aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
print('Connected')
# Image download
s3.Bucket(BUCKET_NAME).download_file(FILE_NAME, 'anh2.jpg'); # Change the second part
# This is where you want to download it too.

print ("Done")
