from flask import Blueprint, request, jsonify

from coredb.service import add_service, update_service, fetch_service_by_id
from coredb.user import fetch_user_by_id
from coredb.worker import fetch_worker_by_id
from routes.worker import validate_profession_type

service_bp = Blueprint('service', __name__)


@service_bp.route('/service', methods=['POST'])
def new_service():
    try:
        data = request.json
        if 'problem' in data and 'type' in data and 'time_slot' in data and 'date' in data and 'user_id':
            fetch_user_by_id(data["user_id"])
            validate_profession_type(data['type'])
            add_service(data)
            return jsonify({"message": "Service record created successfully"}), 201
        else:
            return jsonify({"error": "Missing data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@service_bp.route('/service', methods=['PUT'])
def update_services():
    try:
        data = request.json
        if 'id' not in data:
            return jsonify({"error": "Missing 'id' in the payload"}), 400

        previous_record = fetch_service_by_id(data['id'])

        if 'status' not in data and 'worker_id' not in data and 'feedback' not in data:
            return jsonify({"error": "Provide at least one field to update"}), 400

        if 'worker_id' in data:
            fetch_worker_by_id(data["worker_id"])

        if 'status' in data:
            check_status_transition(previous_record["status"], data["status"])

        update_service(
            data['id'],
            status=data.get('status'),
            worker_id=data.get('worker_id'),
            feedback=data.get('feedback')
        )

        return jsonify({"message": f"Service record with ID {data['id']} updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def check_status_transition(last_state, current_state):
    transitions = {
        'Pending': 'Confirmed',
        'Confirmed': 'Started',
        'Started': 'Completed',
        'Completed': 'Closed'
    }

    if last_state in transitions and transitions[last_state] == current_state:
        return f"Status transition from {last_state} to {current_state} is valid."
    else:
        raise ValueError(f"Invalid status transition from {last_state} to {current_state}.")

