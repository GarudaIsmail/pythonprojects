import boto3
import json
import time
import sys
import os

accountid = os.getenv("AccountId")
rolename = os.getenv("RoleName")
region = os.getenv("region")
trg_accountid = []
trg_accountid.append(os.getenv("trg_accountid"))
ami_list = os.getenv("ami_name")
role_arn = "arn:aws:iam::"+accountid+":role/"+rolename

sts_connection = boto3.client('sts')
acct_b = sts_connection.assume_role(RoleArn=role_arn,RoleSessionName="ami_account")
    
ACCESS_KEY = acct_b['Credentials']['AccessKeyId']
SECRET_KEY = acct_b['Credentials']['SecretAccessKey']
SESSION_TOKEN = acct_b['Credentials']['SessionToken']
    
client = boto3.client(
        'ec2',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        aws_session_token=SESSION_TOKEN,
    )

def list_all_buckets():
    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

def amisharing():
    #client = boto3.client('ec2', region_name=region)
    response = client.describe_images(Owners=['self'])
#     print(response)
    try:
        for ami in response['Images']:
            print("ami_id:", ami['ImageId'])
#             for imageName in ami_list:
            if(ami_list == ami['Name']):
                print("malik")
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
    print('role_arn',role_arn)
    amisharing()
