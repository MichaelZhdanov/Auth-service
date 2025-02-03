from flask import Flask, request, jsonify, send_from_directory, abort
import hashlib
import os

app = Flask(__name__)

# Path to the frontend directory
FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "frontend")

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
    try:
        return send_from_directory(FRONTEND_DIR, "login.html")
    except FileNotFoundError:
        app.logger.error("login.html not found in %s", FRONTEND_DIR)
        abort(404)

# Serve the registration page
@app.route("/register")
def serve_register():
    try:
        return send_from_directory(FRONTEND_DIR, "register.html")
    except FileNotFoundError:
        app.logger.error("register.html not found in %s", FRONTEND_DIR)
        abort(404)

# Handle login requests

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)