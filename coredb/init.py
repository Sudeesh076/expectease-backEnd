import sqlite3


def startDb():
    db = sqlite3.connect("expect-ease.db")
    cursor = db.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    create_service_request_table(cursor)
    create_service_table(cursor)
    create_workers_table(cursor)
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
        address TEXT,
        area TEXT
    )''')


def create_workers_table(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='workers'")
    table_exists = cursor.fetchone()

    if table_exists:
        cursor.execute("DROP TABLE workers")

    cursor.execute('''CREATE TABLE workers (
        id TEXT PRIMARY KEY,
        email TEXT UNIQUE,
        password TEXT,
        first_name TEXT,
        last_name TEXT,
        ph_number TEXT,
        address TEXT,
        area TEXT,
        type TEXT,
        work_exp TEXT,
        age TEXT,
        aadhar_number TEXT,
        image TEXT
    )''')


def create_service_table(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='service'")
    table_exists = cursor.fetchone()

    if table_exists:
        cursor.execute("DROP TABLE service")

    cursor.execute('''CREATE TABLE service (
        id TEXT PRIMARY KEY,
        problem TEXT,
        type TEXT,
        time_slot TEXT,
        date TEXT,
        user_id TEXT,
        worker_id TEXT,
        status TEXT,
        feedback TEXT
    )''')


def create_service_request_table(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='service_request'")
    table_exists = cursor.fetchone()

    if table_exists:
        cursor.execute("DROP TABLE service_request")

    cursor.execute('''CREATE TABLE service_request (
        id TEXT PRIMARY KEY,
        service_id TEXT,
        worker_id TEXT,
        status TEXT
    )''')
