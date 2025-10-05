import mysql.connector
from mysql.connector import Error
from flask import request, jsonify
from ..db.config import db_config

def get_app():
    from ..app import app
    return app

app = get_app()

# 1. Book Publishing API: POST /api/book/publish
@app.route('/api/book/publish', methods=['POST'])
def publish_book():
    try:
        # Verify login status (token = user ID)
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not token or not token.isdigit():
            return jsonify({"success": False, "message": "Please log in first"})
        user_id = int(token)

        # Get book information
        data = request.get_json()
        title = data.get('title', '').strip()
        author = data.get('author', '').strip()
        price = data.get('price', 0)
        message_div = {"success": False, "message": ""}

        # Validate book information (enhanced price validation)
        if not title:
            message_div["message"] = "Please enter the book title"
            return jsonify(message_div)
        if not author:
            message_div["message"] = "Please enter the author"
            return jsonify(message_div)
        # New: Check if price is a number and non-negative
        try:
            price_num = float(price)
            if price_num < 0:
                message_div["message"] = "Price cannot be negative"
                return jsonify(message_div)
        except (ValueError, TypeError):
            message_div["message"] = "Price must be a valid number"
            return jsonify(message_div)

        # Store in database
        connection = mysql.connector.connect(** db_config)
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO books (title, author, price, user_id) VALUES (%s, %s, %s, %s)",
            (title, author, price_num, user_id)  # Use the converted number
        )
        connection.commit()
        message_div["success"] = True
        message_div["message"] = "Book published successfully"
        return jsonify(message_div)

    except Error as e:
        return jsonify({"success": False, "message": f"Database error: {str(e)}"})
    except Exception as e:
        return jsonify({"success": False, "message": f"Server error: {str(e)}"})
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# 2. Get All Published Books API: GET /api/book/all
@app.route('/api/book/all', methods=['GET'])
def get_all_books():
    try:
        # Query all books (associate publisher's username)
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT b.id, b.title, b.author, b.price, b.publish_time, u.username 
            FROM books b
            JOIN users u ON b.user_id = u.id
            ORDER BY b.publish_time DESC  # Sort by publication time in descending order (newest first)
        """)
        books = cursor.fetchall()  # Get all book data

        return jsonify({
            "success": True,
            "message": "Query successful",
            "books": books  # Book list (including publisher's username)
        })

    except Error as e:
        return jsonify({"success": False, "message": f"Database error: {str(e)}"})
    except Exception as e:
        return jsonify({"success": False, "message": f"Server error: {str(e)}"})
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
