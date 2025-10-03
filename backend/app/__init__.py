from flask import Flask
from flask_cors import CORS

# Initialize the Flask application (core object)
app = Flask(__name__)

# Configure CORS (allow the frontend to call the login API)
CORS(app, resources={r"/api/login": {"origins": "*"}})

# Import the login API (placed after app initialization to avoid circular imports)
from ..api.login_api import login
from ..api.register_api import register
