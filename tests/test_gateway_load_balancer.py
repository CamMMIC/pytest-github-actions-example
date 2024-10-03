#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import tests.utils.utils as utils

def test_gateway_load_balancer():

    session_helper = utils.Boto3SessionHelper("network", "eu-west-1")
    client = session_helper.create_client("elbv2")

    load_balancers = client.describe_load_balancers()["LoadBalancers"]

    assert len(load_balancers) > 0, "No Gateway Load Balancer found"
    load_balancer = load_balancers[0]

    assert load_balancers[0]["Type"] == "gateway"
    assert load_balancer["State"]["Code"] in ["active", "provisioning"]
