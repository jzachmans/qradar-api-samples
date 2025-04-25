from asset_model.notional_inventory import notional_inventory
from asset_model.GetAssets import main as GetAssets

import typing

def validate_qradar_inventory(expected_host, actual_inventory):
    if expected_host not in actual_inventory:
        print(expected_host + " missing from qradar logs")




def main():
    expected_inventory = notional_inventory()
    actual_inventory = GetAssets()
    for expected_host in expected_inventory:
        validate_qradar_inventory(expected_host, actual_inventory)



if __name__ == "__main__":
    main()