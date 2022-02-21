import boto3
import json
import time
import sys
import os

accountid = os.getenv("accountid")
region = os.getenv("region")
trg_accountid = os.getenv("trg_accountid")
ami_list = os.getenv("ami_name")

def list_all_buckets():
    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

def amisharing():
    client = boto3.client('ec2', region_name=region)
    response = client.describe_images(Owners=['self'])
#     print(response)
    try:
        for ami in response['Images']:
            print("ami_id:" ami['ImageId'])
            for imageName in ami_list:
                print(imageName)
                if(imageName == ami['Name']):
                    response2 = client.modify_image_attribute(
                        Attribute='launchPermission',
                        ImageId=ami['ImageId'],
                        OperationType='add',
                        UserIds=trg_accountid
                    )
                    print(response2)
    except Exception as e:
        print(e)

if __name__ == "__main__":
#     list_all_buckets()
    print('accountid:', accountid)
    print('region:', region)
    print('target account id:', trg_accountid)
    print('AMI id:', ami_list)
    amisharing()
