import boto3
import os
import base64
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("BUCKET_NAME")

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)


def list_files_in_bucket(bucket_name):
    try:
        files = s3.list_objects_v2(Bucket=bucket_name)
        return files.get('Contents', [])
    except Exception as e:
        print("Error listing files in bucket:", e)
        return []
def list_folders_in_bucket(bucket_name):
    folders = []
    try:
        responses = s3.list_objects_v2(Bucket=bucket_name)
        for content in responses.get('Contents', []):
            if content.get("Size") != 0:
                folder = content.get("Key").split("/")[-2]
                folders.append(folder)
        return set(folders)
    except Exception as e:
        print("Error listing files in bucket:", e)
        return []

def download_file(bucket_name, s3_key, local_path):
    try:
        s3.download_file(bucket_name, s3_key, local_path)
        print(f"File {s3_key} downloaded to {local_path}")
    except Exception as e:
        print("Error downloading file:", e)

def download_n_encode(bucket_name, file_name):
    try:
        paginator = s3.get_paginator("list_objects_v2")
        pages = paginator.paginate(Bucket=bucket_name)
        
        for page in pages:
            for content in page.get('Contents', []):
                key = content.get("Key")
                if key.endswith(file_name):  
                    print(f"File found: {key}")
                    
                    s3_object = s3.get_object(Bucket=bucket_name, Key=key)
                    file_data = s3_object['Body'].read()
                    
                    encoded_file = base64.b64encode(file_data).decode('utf-8')
                    return encoded_file
        
        print(f"File '{file_name}' not found in the bucket.")
        return None
    except Exception as e:
        print("Error finding, downloading, or encoding file in S3:", e)
        return None

def expand_s3_folder(bucket_name,folder_name):
    files = []
    date_mod =[]
    try:
        responses = s3.list_objects_v2(Bucket=bucket_name)
        for content in responses.get('Contents', []):
            if content.get("Key").__contains__(folder_name):
                file = content.get("Key").split("/")[-1]
                files.append(file)
                date_mod.append(content.get('LastModified'))
        return files,date_mod
    except Exception as e:
        print("Error listing files in bucket:", e)
        return []


def download_all_files(bucket_name, download_dir):
    files = list_files_in_bucket(bucket_name)
    if not files:
        print("No files to download.")
        return
    
    for file in files:
        s3_key = file['Key']
        local_path = os.path.join(download_dir, s3_key)
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        download_file(bucket_name, s3_key, local_path)


def get_s3_file_url(bucket_name,folder_name,file_name,expiration=60):
    try:
        # Generate a presigned URL for the S3 object
        full_key = f"{folder_name}/{file_name}"
        response = s3.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': full_key},
                                                    ExpiresIn=expiration)
    except Exception as e:
        print(e)
        return None

    return response

