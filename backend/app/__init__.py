from flask import Flask
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)

# Configure CORS (allow all APIs to be called by the frontend)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Import all interfaces (placed after app initialization to avoid circular imports)
from ..api.login_api import login
from ..api.register_api import register
from ..api.book_api import publish_book, get_all_books
from ..api.user_api import change_password
