from flask import Blueprint, jsonify

from src.models.models import Room

bp = Blueprint('rooms', __name__, url_prefix='/rooms')

@bp.route('/', methods=['GET'])
def get_rooms():
    rooms = Room.query.all()
    return jsonify({'rooms': [room.to_dict() for room in rooms]})