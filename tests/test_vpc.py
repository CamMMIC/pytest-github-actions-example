#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import tests.utils.utils as utils

def test_network_inspection_vpc():

    session_helper = utils.Boto3SessionHelper("network", "eu-west-1")
    client = session_helper.create_client("ec2")

    run_vpc_tests ("NetworkInspection-Dublin", client)

def test_network_endpoints_vpc():

    session_helper = utils.Boto3SessionHelper("network", "eu-west-1")
    client = session_helper.create_client("ec2")

    run_vpc_tests ("NetworkEndpoints-Dublin",client)

def run_vpc_tests(vpc_name, ec2_client):

    filters=[{"Name": "tag:Name", "Values": [vpc_name]}]
    vpcs = ec2_client.describe_vpcs(Filters=filters)["Vpcs"]

    assert len(vpcs) > 0, "VPC " + vpc_name + " not found"

    vpc = vpcs[0]
    tags = vpc.get("Tags", [])
    assert {"Key": "Name", "Value": vpc_name} in tags
    assert vpc["State"] == "available"

    vpc_id = vpc["VpcId"]

    filters=[{"Name": "tag:Name", "Values": [vpc_name]}]
    flow_logs = ec2_client.describe_flow_logs(Filters=[{"Name": "resource-id", "Values": [vpc_id]}])

    assert len(flow_logs) > 0, "No flow logs defined for VPC " + vpc_name

def test_vpc_endpoints():

    session_helper = utils.Boto3SessionHelper("network", "eu-west-1")
    client = session_helper.create_client("ec2")

    # filters=[{"Name": "vpc-endpoint-type", "Values": "Interface"}]
    # endpoints = ec2.describe_vpc_endpoints(Filters=filters)["VpcEndpoints"]

    endpoints = client.describe_vpc_endpoints()["VpcEndpoints"]

    assert len(endpoints) > 0, "No Interface Endpoints found"

    print (endpoints)

    services = ["ec2","ec2messages","ssm","ssmmessages","kms","logs","rds","rds-data","sts","sns","execute-api","secretsmanager"]

    for service in services:

        # search endpoints for an entry matching service
        for endpoint in endpoints:
            if endpoint["ServiceName"] == service:
                print (endpoint)
                assert endpoint["State"] in ["Available", "Pending"]
                assert endpoint["VpcEndpointType"] == "Interface"
                break
