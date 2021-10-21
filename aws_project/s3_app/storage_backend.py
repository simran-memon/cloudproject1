from storages.backends.s3boto3 import S3Boto3Storage

class MyS3Storage(S3Boto3Storage):
    bucket_name = 'my-s3-account-test-bucket'
    location = 'documents'
    file_overwrite = False
