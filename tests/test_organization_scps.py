#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import tests.utils.utils as utils
import boto3

# tests whether custom SCPs are applied to correct OUs. Does not check for control-tower owned SCPs as may change outside of our control by managed service
def test_organization_scp():

    client = boto3.client("organizations", region_name = "eu-west-2")

    response = client.list_roots()

    # get root id
    root_id = response["Roots"][0]["Id"]

    # Get Service Control Policies for root_id
    response = client.list_policies_for_target(
        TargetId=root_id,
        Filter='SERVICE_CONTROL_POLICY'
    )

    # Get list of scp Ids from response
    scp_names = [scp["Name"] for scp in response["Policies"]]

    # Make sure that expected SCPs are present
    assert len(scp_names) == 4
    assert "RootSecurityBaseline1" in scp_names
    assert "RootSecurityBaseline2" in scp_names
    assert "FullAWSAccess" in scp_names
    assert "ExplicitlyBlockedServices" in scp_names

    # Get list of OrganizationUnit Ids from response
    response = client.list_organizational_units_for_parent(
        ParentId=root_id
    )
    ou_ids = [ou["Id"] for ou in response["OrganizationalUnits"]]

    # Get SCPs for each OU
    for ou_id in ou_ids:
        # Get name from ou_id
        ou_name = client.describe_organizational_unit(
            OrganizationalUnitId=ou_id
        )["OrganizationalUnit"]["Name"]

        print(ou_name)

        response = client.list_policies_for_target(
            TargetId=ou_id,
            Filter='SERVICE_CONTROL_POLICY'
        )

        scp_names = [scp["Name"] for scp in response["Policies"]]

        assert "FullAWSAccess" in scp_names

        # If ou_name is Sandbox or Security or Workloads or Infrastucture
        # then AcceleratorGuardrails1 and AcceleratorGuardrails2 should exist
        if ou_name in ["Sandbox", "Security", "Workloads", "Infrastructure"]:
            assert "AcceleratorGuardrails1" in scp_names
            assert "AcceleratorGuardrails2" in scp_names 
