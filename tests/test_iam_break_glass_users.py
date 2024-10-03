#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import boto3
from botocore.exceptions import ClientError

def test_break_glass_users():

    iam=boto3.client("iam", region_name = "eu-west-1")

    users = iam.list_users()["Users"]

    assert len(users) > 0
    assert any(i['UserName'] == 'breakGlassUser01' for i in users)
    assert any(i['UserName'] == 'breakGlassUser02' for i in users)
