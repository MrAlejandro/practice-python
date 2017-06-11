import sqlite3

def connect():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS book (" \
            "id INTEGER PRIMARY KEY AUTOINCREMENT," \
            "title VARCHAR(255) DEFAULT ''," \
            "author VARCHAR(255) DEFAULT ''," \
            "year INTEGER UNSIGNED DEFAULT 0," \
            "isbn INTEGER UNSIGNED DEFAULT 0" \
        ")"
    )
    connection.commit()
    cursor.close()

connect()

def add_book(title, author, year, isbn):
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO book VALUES(NULL,?,?,?,?)', (title, author, year, isbn))
    connection.commit()
    cursor.close()

def view_all_books():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM book')
    rows = cursor.fetchall()
    cursor.close()
    return rows

def search_books(title='', author='', year=0, isbn=0):
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM book WHERE 1=1" \
            " OR title = ?" \
            " OR author = ?" \
            " OR year = ?" \
            " OR isbn = ?",
        (title, author, year, isbn)
    )
    rows = cursor.fetchall()
    cursor.close()
    return rows

def delete_book(book_id):
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM book WHERE id = ?', (book_id,))
    connection.commit()
    cursor.close()

def update_book(book_id, title, author, year, isbn):
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    cursor.execute(
        'UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id = ?',
        (title, author, year, isbn, book_id)
    )
    connection.commit()
    cursor.close()

