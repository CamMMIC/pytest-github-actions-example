#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import tests.utils.utils as utils

def test_guardduty():
    session_helper = utils.Boto3SessionHelper("audit", "eu-west-2")
    client = session_helper.create_client("guardduty")

    # Check that guardduty is enabled
    response = client.list_detectors() 
    detector_ids = response["DetectorIds"]

    # Assert that there is only one detector
    assert len(detector_ids) == 1, "Expected only one GuardDuty detector"

    detector_id = detector_ids[0]

    # Get the detector details
    detector = client.get_detector(DetectorId=detector_id)

    # Assert that the detector ID exists
    assert "Status" in detector, "DetectorId not found in response"
    assert detector["Status"] == "ENABLED", "DetectorId is not enabled"


    detectorFeatures = detector["Features"]

    for feature in detectorFeatures:
        name = feature["Name"]

        match name:
            case "CLOUD_TRAIL" | "DNS_LOGS" | "FLOW_LOGS" | "S3_DATA_EVENTS":
                assert feature["Status"] == "ENABLED", f"{name} should be enabled but is {feature['Status']}"
            case _:
                assert feature["Status"] == "DISABLED", f"{name} should be disabled but is {feature['Status']}"
    
        if "AdditionalConfiguration" in feature:
            for additional_config in feature["AdditionalConfiguration"]:
                additional_name = additional_config["Name"]
                additional_status = additional_config["Status"]
                assert additional_status == "DISABLED", f"{additional_name} should be disabled but is {additional_status}"
