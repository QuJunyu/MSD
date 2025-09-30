from flask import request, jsonify
from backend.app import app
import mysql.connector  

db_config = {
  'host': 'localhost',
  'user': 'root',
  'password': 'your_password',  
  'database': 'campus_book_trade'
}

@app.route('/api/login', methods=['POST'])
def login():
  data = request.get_json()
  username = data.get('username')
  password = data.get('password')
  
  if not username or not password:
    return jsonify({'success': False, 'message': 'The username and password cannot be left blank.'})
  
  try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    
    if user and user['password'] == password:  
      return jsonify({'success': True, 'message': 'Login successful', 'token': 'dummy_token'})
    else:
      return jsonify({'success': False, 'message': 'Username or password is incorrect.'})
  except Exception as e:
    return jsonify({'success': False, 'message': f'Database error：{str(e)}'})
  finally:
    if conn:
      conn.close()
