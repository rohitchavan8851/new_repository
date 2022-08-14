import os
import boto3
s3 = boto3.client('s3')

# ## creating bucket
# responce = s3.create_bucket(
#     ACL='private',
#     Bucket='landing-zone-0908'
# )
# print(responce)
#print("Bucket created")


### uploading file on bucket
## s3.upload_file('path_of_file', 'Bucket_name', 'File_name.format')
# s3.upload_file('F:\python\For s3\Shree.csv', 'landing-zone-0908', 'Shree.csv')
# print("File uploaded successfully")


### Uploading multiple files
### old_dir = C:\Users\PC\PycharmProjects\pythonProject\Practice\Pycharm_aws_connection


os.chdir('F:\python\For s3')
items = os.listdir()
print("Items in local folder are:", items)

file_name = input("Enter the file name you want to load in s3:")
bucket = 'landing-zone-0908'

def upload_files(file_name, bucket, object_name = None, args = None):
    if object_name == None:
        object_name = file_name
    responce = s3.upload_file(file_name, bucket, object_name, ExtraArgs= args)
    return responce

upload_files(file_name, bucket)
print("File uploaded successfully")