from flask import request, jsonify
from backend.app import app
import mysql.connector  # 连接MySQL

# 数据库配置（本地开发环境）
db_config = {
  'host': 'localhost',
  'user': 'root',
  'password': 'your_password',  # 替换为本地MySQL密码
  'database': 'campus_book_trade'
}

# 登录接口（POST /api/login）
@app.route('/api/login', methods=['POST'])
def login():
  data = request.get_json()
  username = data.get('username')
  password = data.get('password')
  
  # 验证参数
  if not username or not password:
    return jsonify({'success': False, 'message': '用户名和密码不能为空'})
  
  # 查询数据库
  try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    
    if user and user['password'] == password:  # 简化验证（实际需加密）
      return jsonify({'success': True, 'message': '登录成功', 'token': 'dummy_token'})
    else:
      return jsonify({'success': False, 'message': '用户名或密码错误'})
  except Exception as e:
    return jsonify({'success': False, 'message': f'数据库错误：{str(e)}'})
  finally:
    if conn:
      conn.close()
