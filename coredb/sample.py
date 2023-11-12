from coredb.user import add_user
from coredb.worker import add_worker


def sampleData():
    add_default_users()
    add_default_worker()


def add_default_users():
    user_data_list = [
        {
            "email": "sarthakkondhekar7@gmail.com",
            "password": "sarthak@123",
            "first_name": "Sarthak",
            "last_name": "Kondhekar",
            "ph_number": "8600722970",
            "address": "Muktai Residency, Near TKIET, Warnanagar",
            "area": "WARNANAGAR"
        },
        {
            "email": "naikganesh0021@gmail.com",
            "password": "ganesh@123",
            "first_name": "Ganesh",
            "last_name": "Naik",
            "ph_number": "9022798890",
            "address": "Reu Residency, Front of Super Hero Cafe, Kodoli",
            "area": "KODOLI"
        },
        {
            "email": "patilprathmesh@gmail.com",
            "password": "prathmesh@123",
            "first_name": "Prathmesh",
            "last_name": "Patil",
            "ph_number": "7841075108",
            "address": "Gandharva Appartment, Near Vathar BusStand ,Vathar",
            "area": "VATHAR"
        },
        {
            "email": "abhijaymore1042@gmail.com",
            "password": "abhijay@123",
            "first_name": "Abhijay",
            "last_name": "More",
            "ph_number": "8433871425",
            "address": "More appartments, Near Warnabazar , Warnanagar",
            "area": "WARNANAGAR"
        }
    ]

    for user_data in user_data_list:
        add_user(user_data)


def add_default_worker():
    worker_data_list = [
        {
            'email': 'electrician11@gamil.com',
            'password': 'ELECTRICIAN1',
            "first_name": "Sarthak",
            "last_name": "Kondhekar",
            "ph_number": "8600722970",
            "address": "Muktai Residency, Near TKIET, Warnanagar",
            "area": "WARNANAGAR",
            'type': 'ELECTRICIAN',
            'work_exp': '8 years',
            'age': 30,
            'aadhar_number': '1234-5678-9012',
            'image': 'worker1.jpg'
        },
        {
            'email': 'plumber1@gmail.com',
            'password': 'PLUMBER1',
            "first_name": "Ganesh",
            "last_name": "Naik",
            "ph_number": "9022798890",
            "address": "Reu Residency, Front of Super Hero Cafe, Kodoli",
            "area": "KODOLI",
            'type': 'PLUMBER',
            'work_exp': '7 years',
            'age': 30,
            'aadhar_number': '1234-5678-9012',
            'image': 'worker2.jpg',
        },
        {
            'email': 'carpenter1@gamil.com',
            'password': 'CARPENTER1',
            "first_name": "Prathmesh",
            "last_name": "Patil",
            "ph_number": "7841075108",
            "address": "Gandharva Appartment, Near Vathar BusStand ,Vathar",
            "area": "VATHAR",
            'type': 'CARPENTER',
            'work_exp': '3 years',
            'age': 30,
            'aadhar_number': '1234-5678-9012',
            'image': 'worker3.jpg',
        },
        {
            'email': 'painter1@gamil.com',
            'password': 'PAINTER1',
            "first_name": "Abhijay",
            "last_name": "More",
            "ph_number": "8433871425",
            "address": "More appartments, Near Warnabazar , Warnanagar",
            "area": "WARNANAGAR",
            'type': 'PAINTER',
            'work_exp': '4 years',
            'age': 30,
            'aadhar_number': '1234-5678-9012',
            'image': 'worker4.jpg',
        }

    ]
    for worker_data in worker_data_list:
        add_worker(worker_data)
