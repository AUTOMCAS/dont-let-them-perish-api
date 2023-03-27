from flask import Blueprint, jsonify

from src.models.models import Room

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