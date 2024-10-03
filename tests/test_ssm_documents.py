#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import boto3

import tests.utils.utils as utils


    

def test_audit_mgr():
    session_helper = utils.Boto3SessionHelper("audit", "eu-west-2")
    client = session_helper.create_client("ssm")

    # List all automation documents owned by me

    # Get current account id
    sts_client = session_helper.create_client('sts')
    account_id = sts_client.get_caller_identity()["Account"]

    # List all automation documents owned by the account
    response = client.list_documents(
        DocumentFilterList=[
            {
                'key': 'Owner',
                'value': 'Self'
            },
        ],
    )

    # Check if SSM-ELB-Enable-Logging is in response
    assert 'SSM-ELB-Enable-Logging' in [doc['Name'] for doc in response['DocumentIdentifiers']], f"Document is not found in account {account_id}"

    # Assert that Put-S3-Encryption exists, if not add comment with account id
    assert 'Put-S3-Encryption' in [doc['Name'] for doc in response['DocumentIdentifiers']], f"Document is not found in account {account_id}"

    # Assert that Attach-IAM-Instance-Profile exists, if not add comment with account id
    assert 'Attach-IAM-Instance-Profile' in [doc['Name'] for doc in response['DocumentIdentifiers']], f"Document is not found in account {account_id}"
   
    # Assert that Attach-IAM-Role-Policy exists, if not add comment with account id
    assert 'Attach-IAM-Role-Policy' in [doc['Name'] for doc in response['DocumentIdentifiers']], f"Document is not found in account {account_id}"
