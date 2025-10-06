import mysql.connector
from mysql.connector import Error
from flask import request, jsonify
from ..db.config import db_config  # Unified import of database configuration from db/config (consistent with login)

# Lazy import of app to resolve circular dependencies (consistent with login_api.py style)
def get_app():
    from ..app import app  # Relative path: import instance from app in the parent directory
    return app

# Get app instance and register routes
app = get_app()

# Register interface route (path matches frontend)
@app.route('/api/register', methods=['POST'])
def register():
    try:
        # 1. Get username and password passed from the frontend
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()

        # 2. Frontend parameter validation (non-empty check)
        if not username:
            return jsonify({"success": False, "message": "Please enter username"})
        if not password:
            return jsonify({"success": False, "message": "Please enter password"})

        # 3. Connect to the database and check if the username already exists
        connection = mysql.connector.connect(** db_config)
        cursor = connection.cursor()

        # Check if the username is already registered
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():  # If a result is found, it means the username already exists
            return jsonify({"success": False, "message": "Username already exists"})

        # 4. Insert new user into the database
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password)  # Note: In actual projects, passwords need to be encrypted; plain text is used here for demonstration
        )
        connection.commit()  # Commit the transaction

        # 5. Return on successful registration
        return jsonify({"success": True, "message": "Registration successful, please login"})

    # Catch database errors (e.g., connection failure, SQL errors)
    except Error as e:
        return jsonify({"success": False, "message": f"Database error: {str(e)}"})
    # Catch other unknown errors
    except Exception as e:
        return jsonify({"success": False, "message": f"Server error: {str(e)}"})
    # Finally, close the database connection regardless of success or failure
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
