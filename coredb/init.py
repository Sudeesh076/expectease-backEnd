import sqlite3


def startDb():
    db = sqlite3.connect("expect-ease.db")
    cursor = db.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    create_users_table(cursor)
    db.commit()
    db.close()


def create_users_table(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table_exists = cursor.fetchone()

    if table_exists:
        cursor.execute("DROP TABLE users")

    cursor.execute('''CREATE TABLE users (
        id TEXT PRIMARY KEY,
        email TEXT UNIQUE,
        password TEXT,
        first_name TEXT,
        last_name TEXT,
        ph_number TEXT,
        address TEXT
    )''')
