import sqlite3

def create_connection():
    conn = sqlite3.connect('icecream_parlor_cafe.db')
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
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
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
