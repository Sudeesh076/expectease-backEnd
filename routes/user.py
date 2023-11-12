from flask import Blueprint, request, jsonify
from coredb.user import add_user, user_exists, check_credentials_user
from routes.worker import validate_area_type

user_bp = Blueprint('user', __name__)


@user_bp.route('/user', methods=['POST'])
def new_user():
    try:
        data = request.json
        if 'email' in data and 'password' in data and 'first_name' in data and 'last_name' in data and 'ph_number' in data and 'address' in data and 'area' in data:
            if not user_exists(data['email'], data['ph_number']):
                validate_area_type(data['area'])
                add_user(data)
                return jsonify({"message": "User record created successfully"}), 201
            else:
                return jsonify({"error": "User with the same email or phone number already exists"}), 409
        else:
            return jsonify({"error": "Missing data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@user_bp.route('/login/user', methods=['POST'])
def loginUser():
    try:
        data = request.get_json()

        if 'email' not in data or 'password' not in data:
            return jsonify({"error": "Email and password are required fields"}), 400

        email = data['email']
        password = data['password']

        authenticated, data = check_credentials_user(email, password)

        if authenticated:
            return jsonify(data)
        else:
            return jsonify(data), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500
