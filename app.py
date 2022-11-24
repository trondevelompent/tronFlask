from flask import Flask, request
import tronapi
from tronapi import Tron

full_node = 'https://api.trongrid.io'
solidity_node = 'https://api.trongrid.io'
event_server = 'https://api.trongrid.io'

private_key = "5decdf9cf72f5fd2e3a25543143f49b08f5064233da711a523012541c5b71477"

tron = Tron(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)


def setTronPK(pk):
    tron.private_key = pk
    tron.default_address = tron.address.from_private_key(pk).base58


setTronPK(PK)

app = Flask(__name__)


def myfunc(add):
    txn = tron.trx.send_token(PA, 10 * 100000 * 6, "1003134");
    return "ok"


app.route('/')


def getHandler():
    return "ok"


@app.route('/post', methods=['POST'])
def getHandler():
    r = request.json
    PA = r["address"]
    PS = r["amount"]
    PR = r["tokenid"]
    txn = tron.trx.send_token(PA, 10 * 100000 * PS, PR);
    return txn["transaction"]["txID"]


if __name__ == '__main__':
    app.run()
