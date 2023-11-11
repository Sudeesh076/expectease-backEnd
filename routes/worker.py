from flask import Blueprint, request, jsonify
from coredb.worker import add_worker, worker_exists, check_credentials_worker

worker_bp = Blueprint('worker', __name__)


@worker_bp.route('/worker', methods=['POST'])
def new_worker():
    try:
        data = request.json
        if 'email' in data and 'password' in data and 'first_name' in data and 'last_name' in data and 'ph_number' in data and 'address' in data and 'area' in data and 'work_exp' in data and 'age' in data and 'aadhar_number' in data and 'image' in data:
            if not worker_exists(data['email'], data['ph_number']):
                add_worker(data)
                return jsonify({"message": "Worker record created successfully"}), 201
            else:
                return jsonify({"error": "Worker with the same email or phone number already exists"}), 409
        else:
            return jsonify({"error": "Missing data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@worker_bp.route('/login/worker', methods=['POST'])
def loginWorker():
    try:
        data = request.get_json()

        if 'email' not in data or 'password' not in data:
            return jsonify({"error": "Email and password are required fields"}), 400

        email = data['email']
        password = data['password']

        authenticated, data = check_credentials_worker(email, password)

        if authenticated:
            return jsonify(data)
        else:
            return jsonify(data), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500
