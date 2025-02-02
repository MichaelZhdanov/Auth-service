from flask import Flask, request, jsonify, send_from_directory
import hashlib
import os

app = Flask(__name__)

# Path to the frontend directory
FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "../frontend")

# Function to load users from users.txt
def load_users():
    users = {}
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, hashed_password = line.strip().split(":")
                users[username] = hashed_password
    except FileNotFoundError:
        print("users.txt not found.")
    return users

# Function to save users to users.txt
def save_user(username, hashed_password):
    with open("users.txt", "a") as file:
        file.write(f"{username}:{hashed_password}\n")

# Serve the login page
@app.route("/")
def serve_login():
    return send_from_directory(FRONTEND_DIR, "login.html")

# Serve the registration page
@app.route("/register")
def serve_register():
    return send_from_directory(FRONTEND_DIR, "register.html")

# Handle login requests
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password_hash = data.get('password')

    users = load_users()

    if username in users and users[username] == password_hash:
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Invalid username or password"}), 401

# Handle registration requests
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password_hash = data.get('password')

    users = load_users()

    if username in users:
        return jsonify({"success": False, "message": "Username already exists"}), 400

    save_user(username, password_hash)
    return jsonify({"success": True, "message": "Registration successful"})

if __name__ == '__main__':
    app.run(debug=True)