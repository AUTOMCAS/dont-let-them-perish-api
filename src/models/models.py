from db import db

class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(120), unique=True, nullable=False)
    plant_count = db.Column(db.Integer, nullable=False)
    plants = db.relationship('Plant', backref='location')

    def __init__(self, room_name, plant_count):
      self.room_name = room_name
      self.plant_count = plant_count

    def __repr__(self):
        return '' % self.id
    

class Plant(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    plant_name = db.Column(db.String(120), index=True, unique=True, nullable=False)
    date_watered = db.Column(db.String(80), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))

    def __repr__(self):
        return '' % self.name % self.date_watered % self.room_id