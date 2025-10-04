```python
import mysql.connector
from mysql.connector import Error
from flask import request, jsonify
from ..db.config import db_config

def get_app():
    from ..app import app
    return app

app = get_app()

# Registration endpoint: POST /api/register
@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()
        message_div = {"success": False, "message": ""}

        # Non-null validation
        if not username:
            message_div["message"] = "Please enter username"
            return jsonify(message_div)
        if not password:
            message_div["message"] = "Please enter password"
            return jsonify(message_div)

        # Database operation
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Check if username already exists
        cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            message_div["message"] = "Username already exists"
            return jsonify(message_div)

        # Insert new user
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        connection.commit()
        message_div["success"] = True
        message_div["message"] = "Registration successful, please log in"
        return jsonify(message_div)

    except Error as e:
        return jsonify({"success": False, "message": f"Database error: {str(e)}"})
    except Exception as e:
        return jsonify({"success": False, "message": f"Server error: {str(e)}"})
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
```
