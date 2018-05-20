import mysql.connector
from exchange import Exchange
from stock import Stock

import time


def print_cursor(cursor):
    row = cursor.fetchone()

    while row:
        print(row)
        row = cursor.fetchone()


def show_databases(cnx):
    c = cnx.cursor()
    c.execute('show databases')

    print_cursor(c)

    c.close()


cnx = mysql.connector.connect(user='root', password='password')


def setup(cnx):
    c = cnx.cursor()
    c.execute('create database exchange')
    c.execute('use exchange')

    c.execute("""create table stocks (
        symbol varchar(36),
        value float,
        delta float,
        volatility float,
        counter int,
        shares int,
        total_shares int,
    primary key (symbol)
    )"""
    )

    c.close()

#setup(cnx)

def insert_stock(stock, cnx):
    c = cnx.cursor()
    operation = ('insert into stocks '
                 '(symbol, value, volatility, shares, total_shares, delta, counter) '
                 'values( '
                 + "'" + str(stock.uuid) + "'" + ','
                 + str(stock.value) + ','
                 + str(stock.volatility) + ','
                 + str(stock.shares) + ','
                 + str(stock.total_shares) + ','
                 + str(stock.delta) + ','
                 + str(stock.counter) + ')'
                 ' on duplicate key update'
                 + ' value='+str(stock.value) + ','
                 + ' volatility='+str(stock.volatility) + ','
                 + ' shares='+str(stock.shares) + ','
                 + ' total_shares='+str(stock.total_shares) + ','
                 + ' delta='+str(stock.delta) + ','
                 + ' counter='+str(stock.counter)
    )

    
    print(operation)

    c.execute (operation)

def get_all_stocks(cnx, exchange):
    c = cnx.cursor()

    c.execute("select * from stocks")

    for res in c:
        key = res[0]

        if key in exchange.stocks:
            stock = exchange.stocks[key]
        else:
            stock = Stock()
            stock.uuid = key
            exchange.stocks[key] = stock

        stock.value = res[1]
        stock.delta = res[2]
        stock.volatility = res[3]
        stock.counter = res[4]
        stock.shares = res[5]
        stock.total_shares = res[6]




            
        

c = cnx.cursor()
e = c.execute

e('use exchange')


ex = Exchange(n=0)

while True:

    get_all_stocks(cnx, ex)

    ex.tick()

    for k,v in ex.stocks.items():
        insert_stock(v, cnx)

    cnx.commit()

    time.sleep(10)


c.close()
cnx.close()
