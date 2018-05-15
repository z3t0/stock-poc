import mysql.connector


def print_cursor(cursor):
    row = cursor.fetchone()

    while row:
        print(row)
        row = cursor.fetchone()


def show_databases(cnx):
    c = cnx.cursor()
    c.execute('show databases')

    print_cursor(show_databases)


cnx = mysql.connector.connect(user='root', password='password')
show_databases(cnx)

