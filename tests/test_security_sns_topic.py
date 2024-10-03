#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import boto3

def test_security_sns_topic():

    # Get sns clien
    sns = boto3.client('sns', region_name='eu-west-2')

    # Get list of sns topics
    response = sns.list_topics()
    topics = response['Topics']

    # Check if there are any topics
    assert len(topics) > 0, "No SNS topics found"

    # Check that one of the topics is aws-accelerator-Security
    topic_arns = [topic['TopicArn'] for topic in topics]
    
    assert any('aws-accelerator-Security' in topic for topic in topic_arns), "No SNS topic found with aws-accelerator-Security in the name" 

    # Get the topic that contain aws-accelerator-Security
    security_topic_arn = next((topic for topic in topic_arns if 'aws-accelerator-Security' in topic), None)

    assert security_topic_arn is not None, "No SNS topic found with aws-accelerator-Security in the name"

    # Get security_topic_arn attributes
    response = sns.get_topic_attributes(TopicArn=security_topic_arn)
    attributes = response['Attributes']

    # Check that the topic has a KMS master key id
    assert 'KmsMasterKeyId' in attributes, "No KMS master key id found for the SNS topic"
   
    # check that there is one subscription confirmed 
    assert attributes['SubscriptionsConfirmed'] == '1', "No subscriptions confirmed found for the SNS topic"


