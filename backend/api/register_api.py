from flask import request, jsonify
from ..app import app  # 修正：相对路径导入 app 实例
import mysql.connector
from .login_api import db_config

# Registration interface (POST /api/register)
@app.route('/api/register', methods=['POST'])
def register():
  data = request.get_json()
  username = data.get('username')
  password = data.get('password')
  
  if not username or not password:
    return jsonify({'success': False, 'message': 'Username and password cannot be empty'})
  
  try:
    conn = mysql.connector.connect(** db_config)
    cursor = conn.cursor()
    
    # Check if username already exists
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    if cursor.fetchone():
      return jsonify({'success': False, 'message': 'Username already exists'})
    
    # Insert new user
    cursor.execute(
      "INSERT INTO users (username, password) VALUES (%s, %s)",
      (username, password)
    )
    conn.commit()  # Commit transaction
    return jsonify({'success': True, 'message': 'Registration successful'})
  except Exception as e:
    return jsonify({'success': False, 'message': f'Registration failed: {str(e)}'})
  finally:
    if conn:
      conn.close()
