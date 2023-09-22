import boto3

sts_client = boto3.client('sts')

# Call the assume_role method of the STSConnection object and pass the role
# ARN and a role session name
assumed_role_object = sts_client.assume_role(
    RoleArn="arn:aws:iam::334839806476:role/anmv_role_getS3_for_across_account",
    RoleSessionName="AssumeRoleSession"
)

# From the response that contains the assumed role, get the temporary
# credentials that can be used to make subsequent API calls
credentials = assumed_role_object['Credentials']

# Use the temporary credentials that AssumeRole returns to make a
# connection to Amazon S3
s3 = boto3.resource(
    's3',
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken'],
)

# s3 = boto3.resource('s3')
BUCKET_NAME = "anmv-my-bucket"
KEY_FILE = "Coding/form-gen-file.html"

if __name__ == '__main__':
    s3.Object(BUCKET_NAME, KEY_FILE).download_file('download/anmv.html')
