from web3 import Web3
import json

with open ('D:\\Blockchain\clientApp\diplomas.abi') as f:
    abi = json.load(f)

infura_url = 'https://ropsten.infura.io/v3/acb75898fa414832af2552933e15e3fc'
address = '0x575C9aCeDfED8F7D7fFa2Ce3cdf5BC41A919b7a0'
contract_address = '0xf07c0932c9Ba128a867F0BbE254d249a9BD1713A'

w3 = Web3(Web3.HTTPProvider(infura_url))
w3.eth.defaultAccount = address

#balance = w3.eth.getBalance(address)
#print(w3.fromWei(balance, 'ether'))
contract = w3.eth.contract(address = contract_address, abi = abi)

print(contract.functions.GetBalance().call())

print(contract.functions.GetEmployees().call())

private_key = 'df026d5b64841afeeee757fc247e704c5cdcaf0d5110d544bf27983a97fad486'

nonce = w3.eth.getTransactionCount(address)
tr = contract.functions.InquireDiplomaByNumber('АБВ 123456').buildTransaction({
    'nonce': nonce,
    'from': address,
    'gas': 3000000,
    #'gasPrice': w3.toWei(1,'gwei'),
    'value': w3.toWei(2,'finney'),
})

signed_tr = w3.eth.account.signTransaction(tr, private_key = private_key)
w3.eth.waitForTransactionReceipt(w3.eth.sendRawTransaction(signed_tr.rawTransaction))