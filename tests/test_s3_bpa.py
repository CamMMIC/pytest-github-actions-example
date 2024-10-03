#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.


import boto3

def test_s3_bpa():

    # Use sts to get current account
    sts = boto3.client("sts")
    account = sts.get_caller_identity()["Account"]

    client = boto3.client("s3control", region_name = "eu-west-1")

    # Get s3 block public access settings using s3 control client
  
    response = client.get_public_access_block(
    AccountId=account
    )
    
    assert response["PublicAccessBlockConfiguration"]["BlockPublicAcls"] == True
    assert response["PublicAccessBlockConfiguration"]["IgnorePublicAcls"] == True
    assert response["PublicAccessBlockConfiguration"]["BlockPublicPolicy"] == True
    assert response["PublicAccessBlockConfiguration"]["RestrictPublicBuckets"] == True



    

