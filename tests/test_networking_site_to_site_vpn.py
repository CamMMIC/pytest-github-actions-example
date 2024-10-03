#   © 2024 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#   This AWS Content is provided subject to the terms of the AWS Customer Agreement available at
#   http://aws.amazon.com/agreement or other written agreement between Customer and either
#   Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

import tests.utils.utils as utils
import tests.utils.common as common

def test_vpn_connection():
    common.test_vpn_connection('Accelerator-Vpn-Dublin', 'available', 'UP');


def test_customer_gateway():
    common.test_customer_gateway('Accelerator-Cgw-Dublin', 'available', '89.37.69.28');