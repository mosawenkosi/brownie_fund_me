from brownie import FundMe
from scripts.helpful_scripts import get_account, deploy_mocks
from scripts.deploy import deploy_fund_me


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account, "gas_limit": 6721975})
    tx = fund_me.withdraw({"from": account, "gas_limit": 6721975, "allow_revert": True})
    tx.wait(1)


def main():
    deploy_fund_me()
    fund()
    withdraw()
