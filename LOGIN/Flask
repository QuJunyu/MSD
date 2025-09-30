from flask import Flask, render_template, request, redirect, url_for, flash, session

# Initialize Flask application
app = Flask(__name__)
# Secret key for session and flash messages (replace with a complex key in production)
app.secret_key = 'dev_secret_key_12345'

# Mock database (replace with real database in actual project)
# Structure: {username: password}
users_db = {
    "student1": "book123",
    "teacher": "teach456"
}

# Home page route
@app.route('/')
def home():
    # If logged in, show home page; otherwise redirect to login page
    if 'username' in session:
        return f"""
        <h1>Welcome to Campus Second-hand Book Trading Platform</h1>
        <p>Logged in as: {session['username']}</p>
        <a href="/logout">Logout</a>
        """
    return redirect(url_for('login'))

# Login route (supports GET and POST methods)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        # Validation logic
        if not username or not password:
            flash('Username and password cannot be empty!')
            return redirect(url_for('login'))
        
        if username in users_db and users_db[username] == password:
            # Login successful, save to session
            session['username'] = username
            flash('Login successful!')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password!')
            return redirect(url_for('login'))
    
    # GET request: show login page
    return render_template('login.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not password:
            flash('Username and password cannot be empty!')
            return redirect(url_for('register'))
        
        if username in users_db:
            flash('Username already exists!')
            return redirect(url_for('register'))
        
        # Registration successful (in actual project, store encrypted password)
        users_db[username] = password
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    
    # GET request: show registration page
    return render_template('register.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)  # Clear session
    flash('Logged out successfully!')
    return redirect(url_for('login'))

# Start the application
if __name__ == '__main__':
    app.run(debug=True)  # Development mode (disable debug in production)
