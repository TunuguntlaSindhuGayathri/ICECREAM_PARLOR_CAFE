import sqlite3

def connect_db():
    return sqlite3.connect('icecream_parlor_cafe.db')

def fetch_all(query, params=()):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

def execute_query(query, params=()):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def fetch_one(query, params=()):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchone()
    conn.close()
    return result
