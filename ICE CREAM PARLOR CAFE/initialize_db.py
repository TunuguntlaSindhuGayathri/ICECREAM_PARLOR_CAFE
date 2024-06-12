import sqlite3

def create_connection():
    conn = sqlite3.connect('icecream_parlor_cafe.db')
    return conn

def initialize_database():
    conn = create_connection()
    cursor = conn.cursor()

    # Create tables if they do not exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavor_offerings (
                      id INTEGER PRIMARY KEY, 
                      name TEXT NOT NULL, 
                      is_seasonal BOOLEAN NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredient_inventory (
                      id INTEGER PRIMARY KEY, 
                      name TEXT NOT NULL, 
                      quantity INTEGER NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS customer_flavor_suggestions (
                      id INTEGER PRIMARY KEY, 
                      flavor_id INTEGER NOT NULL, 
                      suggestion TEXT NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS allergy_concerns (
                      id INTEGER PRIMARY KEY, 
                      concern TEXT NOT NULL)''')

    # Insert initial data into seasonal_flavor_offerings
    cursor.executemany("INSERT INTO seasonal_flavor_offerings (name, is_seasonal) VALUES (?, ?)", [
        ('Vanilla', 1),
        ('Chocolate', 0),
        ('Strawberry', 1)
    ])

    # Insert initial data into ingredient_inventory
    cursor.executemany("INSERT INTO ingredient_inventory (name, quantity) VALUES (?, ?)", [
        ('Milk', 20),
        ('Sugar', 15),
        ('Vanilla Extract', 5)
    ])

    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_database()
