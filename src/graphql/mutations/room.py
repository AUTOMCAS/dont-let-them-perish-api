import graphene
from graphql_relay.node.node import from_global_id

from db import db

from src.models.models import Room, Plant
from src.graphql.types.room import RoomType

class AddRoom(graphene.Mutation):
    class Arguments:
        room_name = graphene.String(required=True)

    room = graphene.Field(lambda: RoomType)

    def mutate(self, info, room_name):
        initial_plant_count = 0
        room = Room(room_name=room_name, plant_count=initial_plant_count)
        db.session.add(room)
        db.session.commit()
        return AddRoom(room=room)


class DeleteRoomByName(graphene.Mutation):
    class Arguments:
        room_name = graphene.String(required=True)

    success = graphene.Boolean()
    
    def mutate(self, info, room_name):
        room = Room.query.filter_by(room_name=room_name).first()

        if not room:
            raise Exception(f"Room {room_name} not found")
        
        for plant in room.plants:
            db.session.delete(plant)

        db.session.delete(room)
        db.session.commit()
        return DeleteRoomByName(success=True)
    
class UpdateRoomInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    room_name = graphene.String()
    plant_count = graphene.Int()

class UpdateRoom(graphene.Mutation):
    class Arguments:
        room_data = UpdateRoomInput(required=True)

    success = graphene.Boolean()

    def mutate(self, info, room_data):
        room_id = from_global_id(room_data.id)[1]
        room = Room.query.get(room_id)

        if not room:
            raise Exception(f"Room with ID: {room_id} not found")

        if room_data.room_name:
            room.room_name = room_data.room_name

        if room_data.plant_count:
            room.plant_count = room_data.plant_count

        db.session.commit()

        return UpdateRoom(success=True)


class UpdateRoomPlantCount:
    def update_count(self, room_id):
        updated_plant_count = Plant.query.filter_by(room_id=room_id).count()
        room = Room.query.get(room_id)
        room.plant_count = updated_plant_count

        db.session.commit()

        return updated_plant_count