#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import tests.utils.utils as utils
import boto3

def test_cloudtrail():

    cloudtrail_name = "aws-controltower-BaselineCloudTrail"

    client = boto3.client("cloudtrail", region_name = "eu-west-2")

    trail = client.get_trail(Name = cloudtrail_name)["Trail"]
    assert len(trail ) > 0, "No CloudTrail trail named " + cloudtrail_name + " Found"

    assert trail["IsMultiRegionTrail"] == True
    assert trail["HomeRegion"] == "eu-west-2"
    assert trail["LogFileValidationEnabled"] == True
    assert trail["IsOrganizationTrail"] == True
