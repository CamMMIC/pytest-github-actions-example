#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import boto3



def test_audit_mgr():
    client = boto3.client('auditmanager')

    # Check that detective is enabled
    auditAdminResponse = client.get_organization_admin_account()
   
    # Get the account ID from auditAdminResponse
    auditManagerAdminAccount = auditAdminResponse['adminAccountId']

    client = boto3.client('organizations')

    # Get account with name Audit 
    listAccountsResponse = client.list_accounts()
    for account in listAccountsResponse['Accounts']:
        if account['Name'] == 'Audit':
            auditAccount = account['Id']

    

    assert auditAccount == auditManagerAdminAccount
