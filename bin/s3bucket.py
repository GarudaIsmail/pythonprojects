import boto3

def list_all_buckets():
    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

if __name__ == "__main__":
    print('programname', sys.argv[0])
    list_all_buckets()
