from flask import Blueprint, jsonify, request
from db import db

from src.models.models import Plant

bp = Blueprint('plants', __name__, url_prefix='/plants')

@bp.route('/', methods=['GET'])
def get_plants():
    plants = Plant.query.all()
    return jsonify({'plants': [plant.to_dict() for plant in plants]})

@bp.route('/<int:id>', methods=['GET'])
def get_plant_by_id(id):
    plant = Plant.query.get(id)
    if not plant:
        return jsonify({'error': 'Plant not found'}), 404
    return jsonify({'plant': plant.to_dict()})

@bp.route('/<plant_name>', methods=['GET'])
def get_plant_by_name(plant_name):
    plant = Plant.query.filter_by(plant_name=plant_name).first()
    if not plant:
        return jsonify({'error': 'Plant not found'}), 404
    return jsonify({'plant': plant.to_dict()})

@bp.route('/', methods=['POST'])
def create_plant():
    data = request.get_json()
    plant = Plant(plant_name=data['plant_name'], date_watered=data['date_watered'], room_id=data['room_id'])
    db.session.add(plant)
    db.session.commit()
    return jsonify({'message': 'Plant created successfully'})