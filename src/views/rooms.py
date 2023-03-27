from flask import Blueprint, jsonify, request
from db import db

from src.models.models import Room, Plant

bp = Blueprint('rooms', __name__, url_prefix='/rooms')

@bp.route('/', methods=['GET'])
def get_rooms():
    rooms = Room.query.all()
    return jsonify({'rooms': [room.to_dict() for room in rooms]})

@bp.route('/<int:id>', methods=['GET'])
def get_room_by_id(id):
    room = Room.query.get(id)
    if not room:
        return jsonify({'error': 'Room not found'}), 404
    return jsonify({'room': room.to_dict()})

@bp.route('/<room_name>', methods=['GET'])
def get_room_by_name(room_name):
    room = Room.query.filter_by(room_name=room_name).first()
    if not room:
        return jsonify({'error': 'Room not found'}), 404
    return jsonify({'room': room.to_dict()})

@bp.route('/', methods=['POST'])
def create_room():
    data = request.get_json()
    room = Room(room_name=data['room_name'], plant_count=0)
    db.session.add(room)
    db.session.commit()
    return jsonify({'message': 'Room created successfully'})

@bp.route('/<int:id>', methods=['PUT'])
def update_room(id):
    room = Room.query.get(id)
    if not room:
        return jsonify({'error': 'Room not found'}), 404
    data = request.get_json()
    room.room_name = data.get('room_name', room.room_name)
    db.session.commit()
    return jsonify({'message': 'Room updated successfully'})

@bp.route('/<int:id>', methods=['DELETE'])
def delete_room(id):
    room = Room.query.get(id)
    if not room:
        return jsonify({'error': 'Room not found'}), 404
   
    for plant in room.plants:
            db.session.delete(plant)

    db.session.delete(room)
    db.session.commit()
    return jsonify({'message': 'Room deleted successfully'})
