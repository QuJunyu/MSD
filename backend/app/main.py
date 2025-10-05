# Import app (Flask application object) from __init__.py in the current directory
from . import app

# Entry point for starting: start the service when running main.py directly
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
