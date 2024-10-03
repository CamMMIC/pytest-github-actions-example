#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import tests.utils.utils as utils

def test_securityhub():
    session_helper = utils.Boto3SessionHelper("audit", "eu-west-2")
    client = session_helper.create_client("securityhub")

    # Check that securityhub is enabled
    administrator_account = client.describe_hub()
    assert administrator_account["HubArn"] == "arn:aws:securityhub:eu-west-2:635908288223:hub/default"
    
    # Check that the expected standards are enabled
    standards_data = client.get_enabled_standards()
    assert standards_data["StandardsSubscriptions"][0]["StandardsSubscriptionArn"] == "arn:aws:securityhub:eu-west-2:635908288223:subscription/aws-foundational-security-best-practices/v/1.0.0" 
    assert standards_data["StandardsSubscriptions"][1]["StandardsSubscriptionArn"] == "arn:aws:securityhub:eu-west-2:635908288223:subscription/cis-aws-foundations-benchmark/v/1.4.0"


    

