# app/controllers/sockets.py
from flask_socketio import join_room, leave_room, emit
from flask_login import current_user
from app import db
from app.models.Message import Message

def register_socket_events(socketio):
    @socketio.on('connect')
    def handle_connect():
        if current_user.is_authenticated:
            join_room('general_chat')
            emit('system_message', {'message': f'{current_user.username} has joined the chat'}, room='general_chat')
        else:
            return False  # Reject the connection

    @socketio.on('disconnect')
    def handle_disconnect():
        if current_user.is_authenticated:
            emit('system_message', {'message': f'{current_user.username} has left the chat'}, room='general_chat')
            leave_room('general_chat')

    @socketio.on('send_message')
    def handle_send_message(data):
        if not current_user.is_authenticated:
            return
        
        content = data.get('message')
        if content and len(content.strip()) > 0:
            # Save message to database
            message = Message(content=content, user_id=current_user.id)
            db.session.add(message)
            db.session.commit()
            
            # Broadcast to all in room
            emit('new_message', message.to_dict(), room='general_chat')