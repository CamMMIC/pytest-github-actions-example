#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import tests.utils.utils as utils

def test_log_archive_bucket():
    session_helper = utils.Boto3SessionHelper("logarchive", "eu-west-2")
    client = session_helper.create_client("s3")

    # get s3 buckets
    response = client.list_buckets()
    buckets = response["Buckets"]
    # assert that there is at least one bucket
    assert len(buckets) > 0

    bucket_names = [bucket["Name"] for bucket in buckets]

    print(buckets)

    # assert that there is at least one bucket for logs we expect
    assert any('aws-accelerator-central-logs' in bucket for bucket in bucket_names), "No S3 bucket found with accelerator-central-logs in the name"
    assert any('aws-accelerator-elb-access-logs' in bucket for bucket in bucket_names), "No S3 bucket found with accelerator-central-logs in the name"
    assert any('aws-accelerator-s3-access-logs' in bucket for bucket in bucket_names), "No S3 bucket found with accelerator-central-logs in the name"
    assert any('aws-controltower-logs' in bucket for bucket in bucket_names), "No S3 bucket found with accelerator-central-logs in the name"
    assert any('aws-controltower-s3-access-log' in bucket for bucket in bucket_names), "No S3 bucket found with accelerator-central-logs in the name"


    # for each bucket, check if it is encrypted
    for bucket in bucket_names:
        response = client.get_bucket_encryption(Bucket=bucket)
        rules = response["ServerSideEncryptionConfiguration"]["Rules"]
        assert any(rule["ApplyServerSideEncryptionByDefault"]["SSEAlgorithm"] == "aws:kms" or rule["ApplyServerSideEncryptionByDefault"]["SSEAlgorithm"] == "AES256"  for rule in rules), f"Bucket {bucket} is not encrypted"
