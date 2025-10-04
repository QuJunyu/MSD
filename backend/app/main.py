# From the __init__.py in the current directory, import app
from . import app

# Start the service (run with python -m backend.app.main in the project root directory)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
