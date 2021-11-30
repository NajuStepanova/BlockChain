from web3 import Web3
import json

with open ('C:\\Users\\User\\OneDrive\\Документы\\GitHub\\KimBar\\clientApp\\diplomas.abi') as f:
    abi = json.load(f)

infura_url = 'https://ropsten.infura.io/v3/acb75898fa414832af2552933e15e3fc'
address = '0x575C9aCeDfED8F7D7fFa2Ce3cdf5BC41A919b7a0'
contract_address = '0x293FE9b90484474Ea13026b5D1514A3DF99e0eA9'

w3 = Web3(Web3.HTTPProvider(infura_url))
w3.eth.defaultAccoint = address

#balance = w3.eth.getBalance(address)
#print(w3.fromWei(balance, 'ether'))
contract = w3.eth.contract(address = contract_address, abi = abi)

print(contract.functions.getBalance().call())

print(contract.functions.employeesGet().call())
