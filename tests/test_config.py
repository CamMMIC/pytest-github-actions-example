#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import tests.utils.utils as utils
import boto3

def test_config():
    client = boto3.client("config", region_name = "eu-west-2")

    # List all config recorders to check that one exists
    response = client.describe_configuration_recorders()
    assert len(response["ConfigurationRecorders"]) > 0

    # List all delivery channels to check that one exists
    response = client.describe_delivery_channels()
    assert len(response["DeliveryChannels"]) > 0

    # Check that current account has a config aggregator
    aggregator_response = client.describe_configuration_aggregators()
    assert len(aggregator_response["ConfigurationAggregators"]) > 0

    # Check that its name is aws-controltower-ConfigAggregatorForOrganizations
    config_aggregator_name = aggregator_response["ConfigurationAggregators"][0]["ConfigurationAggregatorName"]
    assert config_aggregator_name == "aws-controltower-ConfigAggregatorForOrganizations"

    # Check that aggregator is applied to whole organization and not singular accounts
    assert "OrganizationAggregationSource" in aggregator_response["ConfigurationAggregators"][0]


    

