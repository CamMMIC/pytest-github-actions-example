#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import tests.utils.utils as utils

def test_transit_gateway():

    transit_gateway_name = 'NetworkMain-Dublin'

    session_helper = utils.Boto3SessionHelper("network", "eu-west-1")
    client = session_helper.create_client("ec2")

    filters=[{"Name": "tag:Name", "Values": [transit_gateway_name]}]
    gateways = client.describe_transit_gateways(Filters=filters)["TransitGateways"]
    assert len(gateways) > 0, "Transit Gateway " + transit_gateway_name + " not found"
    gateway = gateways[0]

    tags = gateway.get("Tags", [])
    assert {"Key": "Name", "Value": transit_gateway_name} in tags
    assert gateway["State"] == 'available'
