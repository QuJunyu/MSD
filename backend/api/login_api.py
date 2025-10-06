import mysql.connector
from mysql.connector import Error
from flask import request, jsonify
from ..db.config import db_config  # 导入数据库配置

# 延迟导入app（解决循环导入：在函数内部导入已初始化的app）
def get_app():
    from ..app import app
    return app

# 获取app并注册登录路由
app = get_app()

@app.route('/api/login', methods=['POST'])
def login():
    try:
        # 1. 获取前端传递的用户名和密码
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()

        # 2. 前端参数验证（非空检查）
        if not username:
            return jsonify({"success": False, "message": "Please enter your username"})
        if not password:
            return jsonify({"success": False, "message": "Please enter the password"})

        # 3. 连接数据库查询用户
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)  # 返回字典格式（方便取值）
        cursor.execute(
            "SELECT id, username, password FROM users WHERE username = %s",
            (username,)  # 必须用元组格式传递参数
        )
        user = cursor.fetchone()  # 获取查询结果（None表示用户不存在）

        # 4. 验证用户是否存在及密码是否正确
        if not user:
            return jsonify({"success": False, "message": "Username does not exist"})
        if user['password'] != password:  # 简化：实际项目需加密，此处暂用明文
            return jsonify({"success": False, "message": "Password incorrect"})

        # 5. 登录成功：返回用户ID作为token（用于后续扩展）
        return jsonify({
            "success": True,
            "message": "Login successful",
            "token": str(user['id'])  # 存储用户ID，便于后续识别登录状态
        })

    # 捕获数据库错误（如连接失败、SQL错误）
    except Error as e:
        return jsonify({"success": False, "message": f"Database error：{str(e)}"})
    # 捕获其他未知错误
    except Exception as e:
        return jsonify({"success": False, "message": f"Server Error：{str(e)}"})
    # 无论成功失败，最终关闭数据库连接
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
