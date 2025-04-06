from flask import Blueprint, render_template, request
from app.controllers.auth import register_user

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "Hello world with Postgres! 🚀"

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user = register_user(username, email, password)

        if user:
            return render_template('register.html', 
                                 message="Registration successful! Please log in.")
        else:
            return render_template('register.html', 
                                 message="Username or Email already exists.")
    
    return render_template('register.html')