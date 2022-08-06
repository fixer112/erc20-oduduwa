from brownie import Oduduwa
from scripts.helpful_scripts import get_account
from web3 import Web3


initial_supply = Web3.toWei(1000, "ether")  # 1000


def main():
    account = get_account()
    erc20 = Oduduwa.deploy(initial_supply, {"from": account})


# brownie run script/oduduwa.py --network bsc-main
