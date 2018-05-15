from flask import Flask
from flask import request

from exchange import Exchange

import time


app = Flask(__name__)


@app.route('/buy', methods=['POST'])
def buy():
    return request.data


@app.route('/sell', methods=['POST'])
def sell():
    return request.data


@app.route('/stocks', methods=['GET'])
def stocks():
    return request.data


@app.route('/register', methods=['POST'])
def register():
    return request.data


@app.route('/deregister', methods=['POST'])
def deregister():
    return request.data


ex = Exchange()

# while True:
#     ex.tick()
#     time.sleep(1)
