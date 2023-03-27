from flask import Blueprint, jsonify, request
from db import db

from src.models.models import Plant, Room
from src.service.update_room_plant_count import UpdateRoomPlantCount

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
   
    room = Room.query.filter_by(room_name=data['room_name']).first()
    plant = Plant(plant_name=data['plant_name'], date_watered=data['date_watered'])
    
    if room is not None:
        plant.location = room

    db.session.add(plant)
    UpdateRoomPlantCount().update_count(room.id)
    db.session.commit()
    
    return jsonify({'message': 'Plant created successfully'})

@bp.route('/<int:id>', methods=['PUT'])
def update_plant(id):
    plant = Plant.query.get(id)
    if not plant:
        return jsonify({'error': 'Plant not found'}), 404
    data = request.get_json()
    plant.plant_name = data.get('plant_name', plant.plant_name)
    plant.date_watered = data.get('date_watered', plant.date_watered)
    plant.room_id = data.get('room_id', plant.room_id)
    db.session.commit()
    
    return jsonify({'message': 'Plant updated successfully'})

@bp.route('/<int:id>', methods=['DELETE'])
def delete_plant(id):
    plant = Plant.query.get(id)
    if not plant:
        return jsonify({'error': 'Plant not found'}), 404
   
    db.session.delete(plant)
    UpdateRoomPlantCount().update_count(plant.room_id)
    db.session.commit()
    
    return jsonify({'message': 'Plant deleted successfully'})
