import sqlite3
import uuid


def add_worker(data):
    db = sqlite3.connect("expect-ease.db")
    cursor = db.cursor()
    worker_id = str(uuid.uuid4())

    cursor.execute('''INSERT INTO workers (id, email, password, first_name, last_name, ph_number, address, area,
                      work_exp, age, aadhar_number, image)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (worker_id, data['email'], data['password'], data['first_name'], data['last_name'],
                    data['ph_number'], data['address'], data['area'], data['work_exp'], data['age'], data['aadhar_number'],data['image']))
    db.commit()
    db.close()


def worker_exists(email, ph_number):
    db = sqlite3.connect("expect-ease.db")
    cursor = db.cursor()

    cursor.execute('SELECT COUNT(*) FROM workers WHERE email = ? OR ph_number = ?', (email, ph_number))
    count = cursor.fetchone()[0]

    db.close()

    return count > 0


def check_credentials_worker(email, password):
    db = sqlite3.connect("expect-ease.db")
    cursor = db.cursor()

    cursor.execute("SELECT * FROM workers WHERE email = ? AND password = ?", (email, password))
    record = cursor.fetchone()

    if record and record[2] == password:
        db.close()
        return True, fetch_worker_by_id(record[0])
    else:
        db.close()
        return False, "invalid"


def fetch_worker_by_id(worker_id):
    db = sqlite3.connect("expect-ease.db")
    cursor = db.cursor()

    cursor.execute(
        "SELECT id, email, first_name, last_name, ph_number, address, area, work_exp, age, aadhar_number, image FROM workers WHERE id = ?",
        (worker_id,))
    worker = cursor.fetchone()

    if worker:
        worker_dict = {
            "id": worker[0],
            "email": worker[1],
            "first_name": worker[2],
            "last_name": worker[3],
            "ph_number": worker[4],
            "address": worker[5],
            "area": worker[6],
            "work_exp": worker[7],
            "age": worker[8],
            "aadhar_number": worker[9],
            "image": worker[10],
        }
        db.close()
        return worker_dict
    else:
        db.close()
        return None
