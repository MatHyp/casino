from app import db, bcrypt
from app.models.User import User

def register_user(username, email, password):
    existing_user = User.query.filter(
        (User.username == username) | (User.email == email)
    ).first()

    if existing_user:
        return None  

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(username=username, email=email, password=hashed_password)

    db.session.add(user)
    db.session.commit()

    return user