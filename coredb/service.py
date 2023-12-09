import sqlite3
import uuid


def add_service(data):
    db = sqlite3.connect("expect-ease.db")
    cursor = db.cursor()
    service_id = str(uuid.uuid4())

    cursor.execute('''INSERT INTO service (id, problem, type, time_slot, date, user_id, worker_id, status, feedback)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (service_id, data['problem'], data['type'], data['time_slot'], data['date'], data['user_id'], None,
                    "Pending", None))
    db.commit()
    db.close()
    from coredb.serviceRequest import add_service_request
    add_service_request(service_id, data['type'])


def update_service(id, status=None, worker_id=None, feedback=None):
    db = sqlite3.connect("expect-ease.db")
    cursor = db.cursor()

    if status == "Confirmed":
        from coredb.serviceRequest import update_service_request
        update_service_request(id, worker_id)

    if status is not None:
        cursor.execute('''UPDATE service SET status = ? WHERE id = ?''', (status, id))

    if worker_id is not None:
        cursor.execute('''UPDATE service SET worker_id = ? WHERE id = ?''', (worker_id, id))

    if feedback is not None:
        cursor.execute('''UPDATE service SET feedback = ? WHERE id = ?''', (feedback, id))

    db.commit()
    db.close()


class RecordNotFoundException(Exception):
    pass


def fetch_service_by_id(service_id):
    db = sqlite3.connect("expect-ease.db")
    cursor = db.cursor()

    cursor.execute('''SELECT * FROM service WHERE id = ?''', (service_id,))
    service_record = cursor.fetchone()

    db.close()

    if service_record is None:
        raise RecordNotFoundException(f"Service record with ID {service_id} not found")

    service_dict = {
        "id": service_record[0],
        "problem": service_record[1],
        "type": service_record[2],
        "time_slot": service_record[3],
        "date": service_record[4],
        "user_id": service_record[5],
        "worker_id": service_record[6],
        "status": service_record[7],
        "feedback": service_record[8],
    }

    return service_dict


def fetch_services_by_user_id(user_id):
    db = sqlite3.connect("expect-ease.db")
    cursor = db.cursor()

    cursor.execute('''SELECT * FROM service WHERE user_id = ?''', (user_id,))
    service_records = cursor.fetchall()

    db.close()
    services_list = []
    if service_records:
        for service_record in service_records:
            service_dict = {
                "id": service_record[0],
                "problem": service_record[1],
                "type": service_record[2],
                "time_slot": service_record[3],
                "date": service_record[4],
                "user_id": service_record[5],
                "worker_id": service_record[6],
                "status": service_record[7],
                "feedback": service_record[8],
            }
            services_list.append(service_dict)

    return services_list
