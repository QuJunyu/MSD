from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

from ..api.login_api import login           
from ..api.register_api import register     
from ..api.book_api import publish_book     
from ..api.book_api import get_all_books    
from ..api.user_api import change_password  # already exists
from ..api.user_api import forgot_password  # newly added
