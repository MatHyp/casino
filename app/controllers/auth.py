from app import db, bcrypt
from app.models.User import User
from flask import flash


def register_user(username, email, password):
    if User.query.filter_by(email=email).first():
        return (False, "Email already exists", None)
    if User.query.filter_by(username=username).first():
        return (False, "Username already exists", None)
    
    try:
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return (True, "Registration successful", user)
    except Exception as e:
        db.session.rollback()
        return (False, f"Registration failed: {str(e)}", None)
