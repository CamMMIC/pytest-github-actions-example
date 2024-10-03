#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import boto3

def test_scp_revert_manual_changes():

    lambdaClient = boto3.client("lambda", region_name = "us-east-1")

    #get all lambda functions
    response = lambdaClient.list_functions()
    functions = response["Functions"]

    #filter functions that start with "scp-"
    scp_functions = [func for func in functions if func["FunctionName"].startswith("AWSAccelerator-FinalizeSt-RevertScpChangesRevertSc")]
    
    # assert there is 1 function
    assert len(scp_functions) == 1

    eventClient = boto3.client("events", region_name = "us-east-1")

    #get all rules with the prefix
    response = eventClient.list_rules(NamePrefix="AWSAccelerator-FinalizeSt-RevertScpChangesModifyScp")
    rules = response["Rules"]

    print(rules)

    #assert there is 1 rule
    assert len(rules) == 1

    #assert the rule is enabled
    assert rules[0]["State"] == "ENABLED"
