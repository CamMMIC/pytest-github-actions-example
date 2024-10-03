import tests.utils.utils as utils

def test_vpn_connection(vpn_name, state, status):

    session_helper = utils.Boto3SessionHelper("network", "eu-west-1")
    client = session_helper.create_client("ec2")

    vpn_connections = client.describe_vpn_connections()["VpnConnections"]

    assert len(vpn_connections) > 0, "VPN " + vpn_name + " not found"

    # for vpn_connection in vpn_connections:
    #     if vpn_connection["Tags"][0]["Value"] == vpn_name:
    #         assert vpn_connection["State"] == state
    #         assert vpn_connection["VgwTelemetry"][0]["Status"] == status
    #         assert vpn_connection["VgwTelemetry"][1]["Status"] == status
    #         break

    found = False;

    for vpn_connection in vpn_connections:
        Tags = vpn_connection['Tags']

        tag_name_value = ""

        for tag in Tags:
            if tag['Key'] == "Name":
                tag_name_value = tag["Value"]
                if tag_name_value == vpn_name:
                    found = True;
                    assert tag_name_value == vpn_name, "Customer gateway " + vpn_name + " found."
                    assert vpn_connection["State"] == state
                    assert vpn_connection["VgwTelemetry"][0]["Status"] == status
                    assert vpn_connection["VgwTelemetry"][1]["Status"] == status
                    break

        if found:
            break;

    assert found == True, "Customer gateway " + vpn_name + " not found."

def test_customer_gateway(customer_gateway_name, state, ipAddress):

    session_helper = utils.Boto3SessionHelper("network", "eu-west-1")
    client = session_helper.create_client("ec2")

    customer_gateways = client.describe_customer_gateways()["CustomerGateways"]

    assert len(customer_gateways) > 0, "No Customer Gateways found"

    found = False;

    for customer_gateway in customer_gateways:
        Tags = customer_gateway['Tags']

        tag_name_value = ""

        for tag in Tags:
            if tag['Key'] == "Name":
                tag_name_value = tag["Value"]
                if tag_name_value == customer_gateway_name:
                    found = True;
                    assert tag_name_value == customer_gateway_name, "Customer gateway " + customer_gateway_name + " found."
                    assert customer_gateway["State"] == state
                    assert customer_gateway["IpAddress"] == ipAddress
                    break

        if found:
            break;

    assert found == True, "Customer gateway " + customer_gateway_name + " not found."
