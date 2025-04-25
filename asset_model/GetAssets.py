#!/usr/bin/env python3
# This sample demonstrates how to use the /asset_model/assets endpoint in the
# REST API.

# For this scenario to work there must already be assets on the system the
# sample is being run against.  The scenario demonstrates the following
# actions:
#  - How to get assets.

# To view a list of the endpoints with the parameters they accept, you can view
# the REST API interactive help page on your deployment at
# https://<hostname>/api_doc.  You can also retrieve a list of available
# endpoints with the REST API itself at the /api/help/endpoints endpoint.

import sys
import os
import json
import requests



def main():
    # Create our client.
    headers = {"SEC": "your token"}
    url = 'https://10.1.202.4/api/asset_model/assets'
    response = requests.get(url=url, verify=False, headers=headers)

    # Verify that the call to the API was successful.
    if (response.status_code != 200):
        print('Failed to retrieve asset list.')
        sys.exit(1)

    # Display the number of assets retrieved.
    response_body = response.json()
    number_of_assets_retrieved = len(response_body)

    #init host list
    host_list = []

    # Display number of assets, and the IDs of the assets retrieved.
    print(str(number_of_assets_retrieved) + ' assets were retrieved.')
    if (number_of_assets_retrieved > 0):
        print("Asset IDs: ", end="")
        for asset in response_body:
            print(
                str({asset["id"]}) +
                " : hostname: " +
                str({asset['hostnames'][0]['name']}) +
                " : IP: " +
                str({asset['interfaces'][0]['ip_addresses'][0]['value']})
            )
            host_list.append(str({asset['hostnames'][0]['name']}).strip("{}'"))

    return(host_list)

if __name__ == "__main__":
    main()
