import graphene

from db import db

from src.models.models import Room, Plant

from src.graphql.types.plant import PlantType

class AddPlant(graphene.Mutation):
    class Arguments:
        plant_name = graphene.String(required=True)
        date_watered = graphene.String(required=True) 
        room_name = graphene.String(required=True)

    plant = graphene.Field(lambda: PlantType)

    def mutate(self, info, plant_name, date_watered, room_name):
        room = Room.query.filter_by(room_name=room_name).first()
        plant = Plant(plant_name=plant_name, date_watered=date_watered)
        if room is not None:
            plant.location = room
        db.session.add(plant)
        db.session.commit()
        return AddPlant(plant=plant)


