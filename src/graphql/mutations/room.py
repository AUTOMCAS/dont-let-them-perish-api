import graphene

from db import db

from src.models.models import Room, Plant

from src.graphql.types.room import RoomType

class AddRoom(graphene.Mutation):
    class Arguments:
        room_name = graphene.String(required=True)
        plant_count = graphene.String(required=True) 

    room = graphene.Field(lambda: RoomType)

    def mutate(self, info, room_name, plant_count):
        room = Room(room_name=room_name, plant_count=plant_count)
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