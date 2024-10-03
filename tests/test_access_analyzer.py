#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import tests.utils.utils as utils

def test_access_analyzer():
    session_helper = utils.Boto3SessionHelper("audit", "eu-west-2")
    client = session_helper.create_client("accessanalyzer")

    # Check that access analyzer is enabled
    response = client.list_analyzers() 
    analyzers = response['analyzers']

    # Assert that there is only one analyzer
    assert len(analyzers) == 1, "Expected only one access analyzer"

    # Get the analyzer name
    analyzer_name = analyzers[0]['name']

    # Get the analyzer details
    analyzer_details = client.get_analyzer(analyzerName=analyzer_name)

    # Check that the analyzer status is active
    assert analyzer_details['analyzer']['status'] == 'ACTIVE', f"Analyzer '{analyzer_name}' is not active"

    print(f"Analyzer '{analyzer_name}' is active")




