from db import db

from src.models.models import Plant, Room

class UpdateRoomPlantCount:
    def update_count(self, room_id):
        updated_plant_count = Plant.query.filter_by(room_id=room_id).count()
        room = Room.query.get(room_id)
        room.plant_count = updated_plant_count

        db.session.commit()

        return updated_plant_count