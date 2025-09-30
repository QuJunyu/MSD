from flask import Flask
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)  

from backend.api import login_api, register_api, book_api

if __name__ == '__main__':
  app.run(debug=True)  
