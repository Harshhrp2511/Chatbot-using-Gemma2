from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import gemma_2b_model 

# Initialize Flask app and configurations
app = Flask(__name__)
app.secret_key = 'secret-key'  # Change this to a more secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

# Import Gemma 2B model or API (make sure to install any necessary libraries to interact with Gemma 2B)
# For this example, we'll assume Gemma is a local Python function or module
# from gemma import Gemma2B  # Uncomment this line if Gemma 2B is an importable Python module

# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Route for login page and handling login functionality
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('chatbot'))
        flash('Invalid credentials, please try again!', 'danger')
    return render_template('login.html')

# Route for signup page and handling user registration
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose another.', 'danger')
            return render_template('signup.html')
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Signup successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

# Function for getting chatbot response using Gemma 2B model (or your custom logic here)
def get_chatbot_response(user_input):
    try:
        # Replace this with the actual interaction with the Gemma 2B model
        # If Gemma 2B is a callable function, you can use that here. For example:
        response = gemma_2b_model.chat(user_input)  # Hypothetical function call for Gemma 2B
        return response  # Return the chatbot's response

    except Exception as e:
        print(f"Error with Gemma 2B model: {e}")
        return "Sorry, I couldn't process your request at the moment."

# Route for the chatbot interface
@app.route('/chatbot')
def chatbot():
    return render_template('chat.html')

# Route for getting bot's response via AJAX request (using POST method)
@app.route('/get_bot_response', methods=['POST'])
def get_bot_response():
    user_input = request.json.get('message')  # Get the user input from the request
    bot_response = get_chatbot_response(user_input)  # Get chatbot's response
    return jsonify({'response': bot_response})  # Return the response as JSON

# Route for logging out user
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

def get_chatbot_response(user_input):
    try:
        # Replace this with actual logic for getting response from your local Gemma 2B model
        response = gemma_2b_model.chat(user_input)  # Hypothetical method call to interact with Gemma 2B
        return response
    except Exception as e:
        print(f"Error with Gemma 2B model: {e}")
        return "Sorry, I couldn't process your request at the moment."

# Create database tables if they don't exist
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create all tables if they don't exist
    app.run(debug=True)
