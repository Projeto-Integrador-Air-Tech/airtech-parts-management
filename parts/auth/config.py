import jwt
from flask import request, jsonify

def verify_jwt(func):
    def wrapper(*args, **kwargs):
        authorization_header = request.headers.get('Authorization')

        if not authorization_header:
            return jsonify({'error': 'Authorization header missing'}), 401

        token = authorization_header.split(' ')[1]  # Assuming format: "Bearer <token>"

        try:
            with open('parts/resources/public_key.pem', 'rb') as public_key_file:
                public_key = public_key_file.read()
                decoded_payload = jwt.decode(token, public_key, algorithms=['RS256'])
                # You can use decoded_payload in your view function if needed
                return func(*args, **kwargs)
        except jwt.exceptions.DecodeError:
            return jsonify({'error': 'Invalid token'}), 401
        except jwt.PyJWTError as e:
            return jsonify({'error': str(e)}), 500

    return wrapper
