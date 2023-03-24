import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from db import db
from models import Room, Plant

class RoomObject(SQLAlchemyObjectType):
   class Meta:
       model = Room
       interfaces = (graphene.relay.Node, )

class PlantObject(SQLAlchemyObjectType):
   class Meta:
       model = Plant
       interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_rooms = SQLAlchemyConnectionField(RoomObject)
    all_plants = SQLAlchemyConnectionField(PlantObject)

class AddPlant(graphene.Mutation):
    class Arguments:
        plant_name = graphene.String(required=True)
        date_watered = graphene.String(required=True) 
        room_name = graphene.String(required=True)
    
    plant = graphene.Field(lambda: PlantObject)

    def mutate(self, info, plant_name, date_watered, room_name):
        room = Room.query.filter_by(room_name=room_name).first()
        plant = Plant(plant_name=plant_name, date_watered=date_watered)
        if room is not None:
            plant.location = room
        db.session.add(plant)
        db.session.commit()
        return AddPlant(plant=plant)

class Mutation(graphene.ObjectType):
    add_plant = AddPlant.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)