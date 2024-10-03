#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import tests.utils.utils as utils

def test_ipams():

    ipam_name = "AcceleratorIpam"

    session_helper = utils.Boto3SessionHelper("network", "eu-west-2")
    client = session_helper.create_client("ec2")

    filters=[{"Name": "tag:Name", "Values": [ipam_name]}]
    ipams = client.describe_ipams(Filters=filters)["Ipams"]
    assert len(ipams) == 1, "No IPAMS found"
    ipam = ipams[0]

    tags = ipam.get("Tags", [])
    assert {"Key": "Name", "Value": ipam_name} in tags
    assert ipam["State"] in ["create-in-progress", "create-complete", "modify-in-progress", "modify-complete"]

def test_dublin_ipam_pool():

    ipam_pool_name = "DublinPool"

    session_helper = utils.Boto3SessionHelper("network", "eu-west-2")
    client = session_helper.create_client("ec2")

    filters=[{"Name": "tag:Name", "Values": [ipam_pool_name]}]
    ipam_pools = client.describe_ipam_pools(Filters=filters)["IpamPools"]
    assert len(ipam_pools) == 1, "IPAM Pool" + ipam_pool_name + " not Found"
    ipam_pool = ipam_pools[0]

    tags = ipam_pool.get("Tags", [])
    assert {"Key": "Name", "Value": ipam_pool_name} in tags
    assert ipam_pool["State"] in ["create-in-progress", "create-complete", "modify-in-progress", "modify-complete"]
    assert ipam_pool["IpamScopeType"] == 'private'
    assert ipam_pool["AddressFamily"] == 'ipv4'

    ipam_pool_cidrs = client.get_ipam_pool_cidrs(IpamPoolId = ipam_pool["IpamPoolId"], Filters = [])["IpamPoolCidrs"]
    assert len(ipam_pool_cidrs) == 1, "No IPAM Pool CIDRs Found for IPAM Pool " + ipam_pool_name
    assert ipam_pool_cidrs[0]["Cidr"] == "10.225.0.0/16"

def test_london_ipam_pool():

    ipam_pool_name = "LondonPool"

    session_helper = utils.Boto3SessionHelper("network", "eu-west-2")
    client = session_helper.create_client("ec2")

    filters=[{"Name": "tag:Name", "Values": [ipam_pool_name]}]
    ipam_pools = client.describe_ipam_pools(Filters=filters)["IpamPools"]
    assert len(ipam_pools) == 1, "IPAM Pool" + ipam_pool_name + " not Found"
    ipam_pool = ipam_pools[0]

    tags = ipam_pool.get("Tags", [])
    assert {"Key": "Name", "Value": ipam_pool_name} in tags
    assert ipam_pool["State"] in ["create-in-progress", "create-complete", "modify-in-progress", "modify-complete"]
    assert ipam_pool["IpamRegion"] == 'eu-west-2'
    assert ipam_pool["IpamScopeType"] == 'private'
    assert ipam_pool["AddressFamily"] == 'ipv4'

    ipam_pool_cidrs = client.get_ipam_pool_cidrs(IpamPoolId = ipam_pool["IpamPoolId"], Filters = [])["IpamPoolCidrs"]
    assert len(ipam_pool_cidrs) == 1, "No IPAM Pool CIDRs Found for IPAM Pool " + ipam_pool_name
    assert ipam_pool_cidrs[0]["Cidr"] == "10.220.0.0/16"
