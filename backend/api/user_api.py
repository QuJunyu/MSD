import mysql.connector
from mysql.connector import Error
from flask import request, jsonify
from ..db.config import db_config

def get_app():
    from ..app import app
    return app

app = get_app()

# Change password endpoint: POST /api/user/change-password
@app.route('/api/user/change-password', methods=['POST'])
def change_password():
    try:
        # Verify login status (token=user ID)
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not token or not token.isdigit():
            return jsonify({"success": False, "message": "Please log in first"})
        user_id = int(token)

        # Get password information
        data = request.get_json()
        old_password = data.get('old_password', '').strip()
        new_password = data.get('new_password', '').strip()
        message_div = {"success": False, "message": ""}

        # Verify passwords
        if not old_password:
            message_div["message"] = "Please enter old password"
            return jsonify(message_div)
        if not new_password:
            message_div["message"] = "Please enter new password"
            return jsonify(message_div)
        if old_password == new_password:
            message_div["message"] = "New password cannot be the same as old password"
            return jsonify(message_div)

        # Database verification of old password and update
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        # Check if old password is correct
        cursor.execute("SELECT password FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        if not user or user['password'] != old_password:
            message_div["message"] = "Incorrect old password"
            return jsonify(message_div)

        # Update to new password
        cursor.execute("UPDATE users SET password = %s WHERE id = %s", (new_password, user_id))
        connection.commit()
        message_div["success"] = True
        message_div["message"] = "Password changed successfully, please log in again"
        return jsonify(message_div)

    except Error as e:
        return jsonify({"success": False, "message": f"Database error: {str(e)}"})
    except Exception as e:
        return jsonify({"success": False, "message": f"Server error: {str(e)}"})
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
