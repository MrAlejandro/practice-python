import sqlite3

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')

def insert_row(item, quantity, price):
    cursor.execute('INSERT INTO store VALUES (?, ?, ?)', (item, quantity, price))

def get_all_records():
    cursor.execute('SELECT * FROM store')
    return cursor.fetchall()

connection = sqlite3.connect('lite.db')
cursor = connection.cursor()

create_table()

items = [
    {'item':'Test1', 'quantity':8, 'price':10.5},
    {'item':'Test2', 'quantity':7, 'price':9.5},
    {'item':'Test3', 'quantity':6, 'price':8.5},
    {'item':'Test4', 'quantity':5, 'price':7.5},
    {'item':'Test5', 'quantity':4, 'price':6.5},
    {'item':'Test6', 'quantity':3, 'price':5.5},
    {'item':'Test7', 'quantity':2, 'price':6.5},
    {'item':'Test8', 'quantity':1, 'price':5.5},
    {'item':'Test9', 'quantity':0, 'price':4.5},
]

# for item in items:
#     insert_row(item['item'], item['quantity'], item['price'])

print(get_all_records())

connection.commit()
connection.close()
