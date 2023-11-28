import sqlite3

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

sql_to_create_flowers_table = '''
CREATE TABLE flowers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT NOT NULL DEFAULT 0.0,
    quantity FLOAT NOT NULL DEFAULT 0.0
) 
'''

def insert_flowers(conn, flower):
    sql = '''INSERT INTO flowers (product_title, price, quantity)
    VALUES (?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, flower)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_quantity_by_id(conn, product_id, new_quantity):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE flowers SET quantity = ? WHERE id = ?
        ''', (new_quantity, product_id))
        conn.commit()
        print(f"Updated quantity for product with id {product_id}")
    except sqlite3.Error as e:
        print(e)

def update_price_by_id(conn, product_id, new_price):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE flowers SET price = ? WHERE id = ?
        ''', (new_price, product_id))
        conn.commit()
        print(f"Updated price for product with id {product_id}")
    except sqlite3.Error as e:
        print(e)


def delete_product_by_id(conn, product_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM flowers WHERE id = ?
        ''', (product_id,))
        conn.commit()
        print(f"Deleted product with id {product_id}")
    except sqlite3.Error as e:
        print(e)

def select_all_products(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM flowers')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_conditions(conn, price_limit, quantity_limit):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM flowers WHERE price < ? AND quantity > ?
        ''', (price_limit, quantity_limit))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def search_products_by_title(conn, keyword):
    try:
        sursor = conn.cursor()
        sursor.execute('''
            SELECT * FROM flowers WHERE product_title LIKE ?
        ''',('%' + keyword + '%'))
        rows= cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)
connection = create_connection('flowers.db')
if connection is not None:
    print('Succesfully connected to DB!')
    create_table(connection, sql_to_create_flowers_table)
    insert_flowers(connection, ('white peony', 100, 15))
    insert_flowers(connection, ('pink peony', 150, 45))
    insert_flowers(connection, ('red peony', 120, 45))
    insert_flowers(connection, ('red rose', 70, 10))
    insert_flowers(connection, ('white rose', 40, 35))
    insert_flowers(connection, ('pink rose', 70, 20))
    insert_flowers(connection, ('white hydrangea', 150, 30))
    insert_flowers(connection, ('blue hydrangea', 70, 15))
    insert_flowers(connection, ('red hydrangea', 200, 50))
    insert_flowers(connection, ('pink gardenia', 50, 20))
    insert_flowers(connection, ('white gardenia', 50, 10))
    insert_flowers(connection, ('yellow gardenia', 70, 25))
    insert_flowers(connection, ('white tulip', 250, 30))
    insert_flowers(connection, ('pink tulip', 40, 20))
    insert_flowers(connection, ('dark red tulip', 90, 20))
    insert_flowers(connection, ('orange tulip', 20, 20))

    update_quantity_by_id(connection, 1, 20)
    update_price_by_id(connection, 1, 800)
    delete_product_by_id(connection, 2)

    select_all_products(connection)

    select_products_by_conditions(connection, 100, 5)

    search_products_by_title(connection, 'peony')
    connection.close()
