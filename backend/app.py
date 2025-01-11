import os
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import json
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "your_secret_key"
CORS(app)

# Check if users.json exists, if not, create it with an empty dictionary
if not os.path.exists("users.json"):
    with open("users.json", "w") as file:
        json.dump({}, file)

# Load users
with open("users.json", "r") as file:
    users = json.load(file)

# Initialize chatbot (Gemma2 placeholder)
class Gemma2Chatbot:
    def get_response(self, user_message):
        # Placeholder for the Gemma2 model logic
        return "This is a response from Gemma2."

# Initialize chatbot
chatbot = Gemma2Chatbot()

@app.route('/')
def index():
    if "username" in session:
        return redirect(url_for("chatbot_page"))
    return render_template("index.html")

@app.route('/signup', methods=["POST"])
def signup():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users:
        return jsonify({"status": "fail", "message": "Username already exists"})
    
    users[username] = password
    with open("users.json", "w") as file:
        json.dump(users, file)
    return jsonify({"status": "success", "message": "Signup successful!"})

@app.route('/login', methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username in users and users[username] == password:
        session["username"] = username
        return jsonify({"status": "success"})
    return jsonify({"status": "fail", "message": "Invalid credentials"})

@app.route('/logout')
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

@app.route('/chatbot')
def chatbot_page():
    if "username" in session:
        return render_template("chatbot.html")
    return redirect(url_for("index"))

@app.route('/chat', methods=["POST"])
def chat():
    if "username" not in session:
        return jsonify({"status": "fail", "message": "Unauthorized"})
    user_message = request.json.get("message")
    response = chatbot.get_response(user_message)
    return jsonify({"status": "success", "response": response})

if __name__ == "__main__":
    app.run(debug=True)
