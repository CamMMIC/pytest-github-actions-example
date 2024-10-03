#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import boto3

def test_ebs_encryption_by_default():

    client = boto3.client("ec2", region_name = "eu-west-2")

    isEbsEncryption = client.get_ebs_encryption_by_default()
    
    # Check that ebs encryption is true
    assert isEbsEncryption["EbsEncryptionByDefault"] == True
