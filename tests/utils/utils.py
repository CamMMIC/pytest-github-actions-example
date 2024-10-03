#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import boto3
from botocore.exceptions import ClientError
import os
import sys

class Boto3SessionHelper:
    newsession_id = ""
    newsession_key = ""
    newsession_token = ""

    def __init__(self, account_alias, region):
        self.region = region
        self.account_alias = account_alias
    
    def create_client(self, clientToCreate):

        if (self.account_alias == "network"):
            self.assume_role_to_networking_account()

        elif (self.account_alias == "audit"):
            self.assume_role_to_audit_account()

        elif (self.account_alias == "logarchive"):
            self.assume_role_to_la_account()
        
        elif (self.account_alias == "management"):
            self.assume_role_to_management_account()

        elif (self.account_alias != "management"):
            sys.stderr.write("Error: Invalid account alias. Please check the environment variables are set correctly.")

        client = boto3.client(
            clientToCreate,
            region_name = self.region,
            aws_access_key_id = self.newsession_id,
            aws_secret_access_key = self.newsession_key,
            aws_session_token = self.newsession_token
        )

        return client

    def assume_role_to_networking_account(self):

        # Get the networking account credentials from the environment
        network_account_id = os.environ["NETWORK_ACCOUNT_ID"]
        network_assume_role = os.environ["ASSUME_ROLE_NAME"]
        # network_account_id = "441363678600"
        # network_assume_role = "AWSControlTowerExecution"

        # Create session using the current creds
        boto_sts=boto3.client("sts")

        # AssumeRole to the Networking account
        role_arn="arn:aws:iam::" + network_account_id + ":role/" + network_assume_role
        stsresponse = boto_sts.assume_role(
            RoleArn = role_arn,
            RoleSessionName = "newsession"
        )

        self.newsession_id = stsresponse["Credentials"]["AccessKeyId"]
        self.newsession_key = stsresponse["Credentials"]["SecretAccessKey"]
        self.newsession_token = stsresponse["Credentials"]["SessionToken"]

    def assume_role_to_audit_account(self):

        # Get the audit account credentials from the environment
        audit_account_id = os.environ["AUDIT_ACCOUNT_ID"]
        audit_assume_role = os.environ["ASSUME_ROLE_NAME"]
        # audit_account_id = "635908288223"
        # audit_assume_role = "AWSControlTowerExecution"

        # Create session using the current creds
        boto_sts=boto3.client("sts")

        # AssumeRole to the Audit account
        role_arn="arn:aws:iam::" + audit_account_id + ":role/" + audit_assume_role
        stsresponse = boto_sts.assume_role(
            RoleArn = role_arn,
            RoleSessionName = "newsession"
        )

        self.newsession_id = stsresponse["Credentials"]["AccessKeyId"]
        self.newsession_key = stsresponse["Credentials"]["SecretAccessKey"]
        self.newsession_token = stsresponse["Credentials"]["SessionToken"]
    
    def assume_role_to_la_account(self):

        # Get the log archive account credentials from the environment
        la_account_id = os.environ["LA_ACCOUNT_ID"]
        la_assume_role = os.environ["ASSUME_ROLE_NAME"]
        # audit_account_id = "635908288223"
        # audit_assume_role = "AWSControlTowerExecution"

        # Create session using the current creds
        boto_sts=boto3.client("sts")

        # AssumeRole to the Audit account
        role_arn="arn:aws:iam::" + la_account_id + ":role/" + la_assume_role
        stsresponse = boto_sts.assume_role(
            RoleArn = role_arn,
            RoleSessionName = "newsession"
        )

        self.newsession_id = stsresponse["Credentials"]["AccessKeyId"]
        self.newsession_key = stsresponse["Credentials"]["SecretAccessKey"]
        self.newsession_token = stsresponse["Credentials"]["SessionToken"]

