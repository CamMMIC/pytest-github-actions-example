#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import boto3

def test_cloudwatch_alarms():

    # Alarms defined in accelerator
    defined_alarms = ['AWSAcceleratorFailedAlarm', 'CIS-1.7-RootAccountUsage', 'CIS-3.14-VPCChanges', 'CIS-4.10-SecurityGroupChanges', 'CIS-4.11-NetworkACLChanges', 'CIS-4.12-NetworkGatewayChanges', 'CIS-4.13-RouteTableChanges', 'CIS-4.4-IAMPolicyChanges', 'CIS-4.5-CloudTrailChanges', 'CIS-4.6-ConsoleAuthenticationFailure', 'CIS-4.7-DisableOrDeleteCMK', 'CIS-4.8-S3BucketPolicyChanges.', 'CIS-4.9-AWSConfigChanges']

    # Get cloudwatch alarms
    cloudwatch = boto3.client('cloudwatch', region_name='eu-west-2')
    alarms = cloudwatch.describe_alarms()
    # Get a list of alarm names
    alarm_names = [alarm['AlarmName'] for alarm in alarms['MetricAlarms']]

    # Assert there are 13 alarms configured
    assert len(alarm_names) == 13

    # Assert that all defined alarms are present
    for alarm in defined_alarms:
        assert alarm in alarm_names, f"Alarm {alarm} not found"
