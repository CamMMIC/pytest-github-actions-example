#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import tests.utils.utils as utils
import boto3

def test_landing_zone():

    client = boto3.client("controltower", region_name = "eu-west-2")

    landing_zones = client.list_landing_zones()["landingZones"]
    assert len(landing_zones ) > 0, "No CT Landing Zones Found"

    landing_zone_arn = landing_zones[0]["arn"]

    landing_zone = client.get_landing_zone(landingZoneIdentifier = landing_zone_arn)["landingZone"]
    assert len(landing_zone ) > 0, "No CT Landing Zone Found"
    assert landing_zone["driftStatus"]["status"] == "IN_SYNC"