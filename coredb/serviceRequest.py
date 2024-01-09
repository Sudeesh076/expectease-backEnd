import sqlite3
import uuid

from coredb.service import fetch_service_by_id
from coredb.user import fetch_user_by_id
from coredb.worker import fetch_worker_ids_by_type, fetch_worker_by_id


def add_service_request(service_id, service_type):
    list_pf_workers = fetch_worker_ids_by_type(service_type)
    db = sqlite3.connect("expect-ease.db")
    cursor = db.cursor()
    for worker_id in list_pf_workers:
        request = str(uuid.uuid4())
        cursor.execute('''INSERT INTO service_request (id, service_id, worker_id, status)
                          VALUES (?, ?, ?, ?)''',
                       (request, service_id, worker_id, "pending"))
    db.commit()
    db.close()


def update_service_request(service_id, worker_id):
    db = sqlite3.connect("expect-ease.db")
    cursor = db.cursor()

    cursor.execute('''UPDATE service_request SET status = ? WHERE service_id = ?''', ("rejected", service_id))
    cursor.execute('''UPDATE service_request SET status = ? WHERE worker_id = ? and service_id = ?''',
                   ("approved", worker_id, service_id))

    db.commit()
    db.close()


def reject_service_request(service_id, worker_id):
    try:
        db = sqlite3.connect("expect-ease.db")
        cursor = db.cursor()

        cursor.execute('''UPDATE service_request SET status = ? WHERE worker_id = ? AND service_id = ?''',
                       ("reject", worker_id, service_id))

        if cursor.rowcount == 0:
            raise ValueError("Update failed. Service or worker ID not found.")

        db.commit()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    finally:
        db.close()


def fetch_service_ids_by_worker_id(worker_id):
    db = sqlite3.connect("expect-ease.db")
    cursor = db.cursor()
    cursor.execute('''SELECT service_id FROM service_request 
                      WHERE worker_id = ? AND status != ?''', (worker_id, "reject"))

    service_ids = [record[0] for record in cursor.fetchall()]
    db.close()

    service_records = []

    for service_id in service_ids:
        service_record = fetch_service_by_id(service_id)
        if service_record["worker_id"] is None:
            worker_id = None
        else:
            worker_id = fetch_worker_by_id(service_record["worker_id"])

        service_dict = {
            "id": service_record["id"],
            "problem": service_record["problem"],
            "type": service_record["type"],
            "time_slot": service_record["time_slot"],
            "date": service_record["date"],
            "user_id": fetch_user_by_id(service_record["user_id"]),
            "worker_id": worker_id,
            "status": service_record["status"],
            "feedback": service_record["feedback"], }
        service_records.append(service_dict)

    return service_records
