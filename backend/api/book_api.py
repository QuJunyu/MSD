import mysql.connector
from mysql.connector import Error
from flask import request, jsonify
from ..db.config import db_config

def get_app():
    from ..app import app
    return app

app = get_app()

# 1. 发布书籍接口：POST /api/book/publish
@app.route('/api/book/publish', methods=['POST'])
def publish_book():
    try:
        # 验证登录态（token=用户ID）
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not token or not token.isdigit():
            return jsonify({"success": False, "message": "请先登录"})
        user_id = int(token)

        # 获取书籍信息
        data = request.get_json()
        title = data.get('title', '').strip()
        author = data.get('author', '').strip()
        price = data.get('price', 0)
        condition = data.get('condition', '').strip()  # 获取书籍状态
        message_div = {"success": False, "message": ""}

        # 验证书籍信息
        if not title:
            message_div["message"] = "请输入书名"
            return jsonify(message_div)
        if not author:
            message_div["message"] = "请输入作者"
            return jsonify(message_div)
        if not condition:
            message_div["message"] = "请选择书籍状态"
            return jsonify(message_div)
        # 价格验证
        try:
            price_num = float(price)
            if price_num < 0:
                message_div["message"] = "价格不能为负数"
                return jsonify(message_div)
        except (ValueError, TypeError):
            message_div["message"] = "价格必须是有效的数字"
            return jsonify(message_div)

        # 存入数据库（用反引号包裹condition字段）
        connection = mysql.connector.connect(** db_config)
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO books (title, author, price, `condition`, user_id) VALUES (%s, %s, %s, %s, %s)",
            (title, author, price_num, condition, user_id)
        )
        connection.commit()
        message_div["success"] = True
        message_div["message"] = "书籍发布成功"
        return jsonify(message_div)

    except Error as e:
        return jsonify({"success": False, "message": f"数据库错误：{str(e)}"})
    except Exception as e:
        return jsonify({"success": False, "message": f"服务器错误：{str(e)}"})
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# 2. 查看所有已发布书籍接口：GET /api/book/all
@app.route('/api/book/all', methods=['GET'])
def get_all_books():
    try:
        # 查询所有书籍（关联发布者用户名，包含状态字段）
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT b.id, b.title, b.author, b.price, b.`condition`, b.publish_time, u.username 
            FROM books b
            JOIN users u ON b.user_id = u.id
            ORDER BY b.publish_time DESC
        """)
        books = cursor.fetchall()

        return jsonify({
            "success": True,
            "message": "查询成功",
            "books": books
        })

    except Error as e:
        return jsonify({"success": False, "message": f"数据库错误：{str(e)}"})
    except Exception as e:
        return jsonify({"success": False, "message": f"服务器错误：{str(e)}"})
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
