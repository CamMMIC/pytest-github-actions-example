#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import tests.utils.utils as utils

def test_detective():
    session_helper = utils.Boto3SessionHelper("audit", "eu-west-2")
    client = session_helper.create_client("detective")

    # Check that detective is enabled
    response = client.list_graphs()
    detective_graph_ids = response["GraphList"]

    # Assert that there is only one detector
    assert len(detective_graph_ids) == 1, "Expected only one Detective graph"

    # Get detective organization configuration
    response = client.describe_organization_configuration(GraphArn=response["GraphList"][0]["Arn"])

    # Check detective is auto enabled for new accounts
    assert response["AutoEnable"] == True