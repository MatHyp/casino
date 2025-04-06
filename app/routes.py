from flask import Flask, Blueprint, render_template, request
from flask_bcrypt import Bcrypt

# Import user and db
from . import db
from .models import User

main = Blueprint("main", __name__)

app = Flask(__name__)
bcrypt = Bcrypt(app)


@main.route("/")
def home():
    return "Hello from Flask + Postgres! 🚀"


@main.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')
