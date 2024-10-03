#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import tests.utils.utils as utils

def test_cpi_hosted_zone():

    host_name = "cpi06.uk-cpi.com."

    session_helper = utils.Boto3SessionHelper("network", "eu-west-1")
    client = session_helper.create_client("route53")

    hosted_zones = client.list_hosted_zones_by_name(DNSName=host_name)["HostedZones"]

    assert len(hosted_zones) > 0, "Hosted Zone " + host_name + " not found"
    assert hosted_zones[0]["Name"] == host_name
    assert hosted_zones[0]["Config"]["PrivateZone"] == True

def test_inbound_endpoint():

    session_helper = utils.Boto3SessionHelper("network", "eu-west-1")
    client = session_helper.create_client("route53resolver")

    filters=[{"Name": "Direction", "Values": ["INBOUND"]}]
    resolver_endpoints = client.list_resolver_endpoints(Filters=filters)["ResolverEndpoints"]

    assert len(resolver_endpoints) > 0, "No INBOUND Resolver Endpoints found"
    resolver_endpoint = resolver_endpoints[0]

    assert resolver_endpoint["Status"] in ["CREATING", "OPERATIONAL"]

def test_outbound_endpoint():
    session_helper = utils.Boto3SessionHelper("network", "eu-west-1")
    client = session_helper.create_client("route53resolver")

    filters=[{"Name": "Direction", "Values": ["OUTBOUND"]}]
    resolver_endpoints = client.list_resolver_endpoints(Filters=filters)["ResolverEndpoints"]

    assert len(resolver_endpoints) > 0, "No OUTBOUND Resolver Endpoints found"

    resolver_endpoint = resolver_endpoints[0]

    assert resolver_endpoint["Status"] in ["CREATING", "OPERATIONAL"]

def test_on_prem_resolver_rule():
    session_helper = utils.Boto3SessionHelper("network", "eu-west-1")
    client = session_helper.create_client("route53resolver")

    rule_name = "on-premises-network-rule-dublin"

    resolver_rules = client.list_resolver_rules(
        Filters=[
            {"Name": "TYPE", "Values": ["FORWARD"]},
            {"Name": "NAME", "Values": [rule_name]},
        ]
    )["ResolverRules"]
    assert len(resolver_rules) == 1, "Resolver Rule " + rule_name + " not found"

    target_ips = resolver_rules[0].get("TargetIps", [])
    assert {'Ip': '10.60.21.12', 'Port': 53, 'Protocol': 'Do53'} in target_ips

def test_aws_services_resolver_rule():
    session_helper = utils.Boto3SessionHelper("network", "eu-west-1")
    client = session_helper.create_client("route53resolver")

    rule_name = "aws-services-rule"

    resolver_rules = client.list_resolver_rules(
        Filters=[
            {"Name": "TYPE", "Values": ["SYSTEM"]},
            {"Name": "NAME", "Values": [rule_name]},
        ]
    )["ResolverRules"]
    assert len(resolver_rules) == 1, "Resolver Rule " + rule_name + " not found"
    assert resolver_rules[0]["DomainName"] == "amazonaws.com."

def test_phz_resolver_rule():
    session_helper = utils.Boto3SessionHelper("network", "eu-west-1")
    client = session_helper.create_client("route53resolver")

    rule_name = "phz-rule"
    resolver_rules = client.list_resolver_rules(
        Filters=[
            {"Name": "TYPE", "Values": ["SYSTEM"]},
            {"Name": "NAME", "Values": [rule_name]},
        ]
    )["ResolverRules"]
    assert len(resolver_rules) == 1, "Resolver Rule " + rule_name + " not found"
    assert resolver_rules[0]["DomainName"] == "cpi06.uk-cpi.com."
