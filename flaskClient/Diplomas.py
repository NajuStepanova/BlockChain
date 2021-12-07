import flask
from web3 import Web3
import json


infura_url = 'https://ropsten.infura.io/v3/acb75898fa414832af2552933e15e3fc'
address = '0x575C9aCeDfED8F7D7fFa2Ce3cdf5BC41A919b7a0'
contract_address = '0x293FE9b90484474Ea13026b5D1514A3DF99e0eA9'
private_key = 'df026d5b64841afeeee757fc247e704c5cdcaf0d5110d544bf27983a97fad486'

app = flask.Flask(_name_)


@app.route('/')
def index():
    return flask.render_template("index.html")


@app.route('/getowner')
def getowner():
    owner = contract.functions.employeesGet().call()
    return flask.render_template("Owner.html", owner_address=owner)


@app.route('/getdiploma')
def get_diploma():
    #nonce = w3.eth.getTransactionCount(address)
    #tr = contract.functions.diplomGetByNumber('АБВ 123456').buildTransaction({
    #    'nonce': nonce,
    #    'from': address,
    #    'gas': 3000000,
    #    'gasPrice': w3.toWei(1000, 'gwei'),
    #    'value': w3.toWei(2, 'finney')
    #})

    #signed_tr = w3.eth.account.signTransaction(tr, private_key=private_key)
    #w3.eth.waitForTransactionReceipt(w3.eth.sendRawTransaction(signed_tr.rawTransaction))
    result = contract.functions.diplomGetByNumber('АБВ 123456').transact({'from': address, 'value': w3.toWei(2, 'finney')})
    return flask.render_template("diplomas.html", fio=result)


if (_name_ == '_main_'):
    w3 = Web3(Web3.HTTPProvider(infura_url))
    w3.eth.defaultAccount = address
    with open('diplomas.abi') as f:
        abi = json.load(f)
    contract = w3.eth.contract(address=contract_address, abi=abi)

    app.run(debug=True)