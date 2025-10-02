# From the __init__.py in the current directory, import app (Flask application object)
from . import app

# Entry point for starting the service: when main.py is run directly, start the service
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
