import mysql.connector
from mysql.connector import Error
from flask import request, jsonify
from ..db.config import db_config  # 统一从db/config导入数据库配置（与login保持一致）

# 延迟导入app，解决循环依赖（和login_api.py风格一致）
def get_app():
    from ..app import app  # 相对路径：从上层目录的app导入实例
    return app

# 获取app实例并注册路由
app = get_app()

# 注册接口路由（路径与前端匹配）
@app.route('/api/register', methods=['POST'])
def register():
    try:
        # 1. 获取前端传入的用户名和密码
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()

        # 2. 前端参数校验（非空检查）
        if not username:
            return jsonify({"success": False, "message": "Please enter username"})
        if not password:
            return jsonify({"success": False, "message": "Please enter password"})

        # 3. 连接数据库，检查用户名是否已存在
        connection = mysql.connector.connect(** db_config)
        cursor = connection.cursor()

        # 检查用户名是否已注册
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():  # 若查询到结果，说明用户名已存在
            return jsonify({"success": False, "message": "Username already exists"})

        # 4. 插入新用户到数据库
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password)  # 注意：实际项目需加密密码，此处为演示用明文
        )
        connection.commit()  # 提交事务

        # 5. 注册成功返回
        return jsonify({"success": True, "message": "Registration successful, please login"})

    # 捕获数据库错误（如连接失败、SQL错误）
    except Error as e:
        return jsonify({"success": False, "message": f"Database error: {str(e)}"})
    # 捕获其他未知错误
    except Exception as e:
        return jsonify({"success": False, "message": f"Server error: {str(e)}"})
    # 无论成功失败，最终关闭数据库连接
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
