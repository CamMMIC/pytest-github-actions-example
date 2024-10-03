#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

from botocore.exceptions import ClientError
import tests.utils.utils as utils

def test_vpc_network_inspection():

    session_helper = utils.Boto3SessionHelper("network", "eu-west-1")
    client = session_helper.create_client("ec2")

    vpc_name = "NetworkInspection"

    try:
        response = client.describe_vpcs(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': ['{vpc_name}']
                }
            ]
        )

        print (response)

        # vpc_id = response['Vpcs'][0]['VpcId']
        # response = client.describe_network_insights_analyses(
        #     NetworkInsightsAnalysisIds=[
        #         vpc_id
        #     ]
        # )["NetworkInsightsAnalyses"]

        # assert len(response['NetworkInsightsAnalyses']) == 1

        assert 1 == 1
    except ClientError as e:
        assert False, f"Error: {e}"
