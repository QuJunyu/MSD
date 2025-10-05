import mysql.connector
from mysql.connector import Error
from flask import request, jsonify
from ..db.config import db_config  # Import database configuration

# Lazy import app (solve circular import: import initialized app inside the function)
def get_app():
    from ..app import app
    return app

# Get app and register login route
app = get_app()

@app.route('/api/login', methods=['POST'])
def login():
    try:
        # 1. Get username and password passed from frontend
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()

        # 2. Frontend parameter validation (non-empty check)
        if not username:
            return jsonify({"success": False, "message": "Please enter your username"})
        if not password:
            return jsonify({"success": False, "message": "Please enter the password"})

        # 3. Connect to database to query user
        connection = mysql.connector.connect(** db_config)
        cursor = connection.cursor(dictionary=True)  # Return dictionary format (easy to get values)
        cursor.execute(
            "SELECT id, username, password FROM users WHERE username = %s",
            (username,)  # Parameters must be passed in tuple format
        )
        user = cursor.fetchone()  # Get query result (None means user does not exist)

        # 4. Verify if user exists and password is correct
        if not user:
            return jsonify({"success": False, "message": "Username does not exist"})
        if user['password'] != password:  # Simplified: encryption is required in actual projects, plain text is used temporarily here
            return jsonify({"success": False, "message": "Password incorrect"})

        # 5. Login successful: return user ID as token (for subsequent expansion)
        return jsonify({
            "success": True,
            "message": "Login successful",
            "token": str(user['id'])  # Store user ID for subsequent login status identification
        })

    # Catch database errors (e.g., connection failure, SQL errors)
    except Error as e:
        return jsonify({"success": False, "message": f"Database error：{str(e)}"})
    # Catch other unknown errors
    except Exception as e:
        return jsonify({"success": False, "message": f"Server Error：{str(e)}"})
    # Finally close database connection regardless of success or failure
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
