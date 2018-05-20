from flask import Flask
from flask import request
from flask import jsonify

from exchange import Exchange

import mysql.connector

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
    return jsonify(get_all_stocks(cnx))


@app.route('/register', methods=['POST'])
def register():
    pass

@app.route('/deregister', methods=['POST'])
def deregister():
    return request.data

cnx = mysql.connector.connect(user='root', password='password', database='exchange')

def get_all_stocks(cnx):
    c = cnx.cursor()

    c.execute("select * from stocks")

    stocks = []

    for res in c:
        stocks.append(res)


    return stocks
