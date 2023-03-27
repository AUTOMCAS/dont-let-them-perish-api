import graphene
from graphql_relay.node.node import from_global_id

from db import db

from src.models.models import Room, Plant
from src.graphql.types.plant import PlantType
from src.service.update_room_plant_count import UpdateRoomPlantCount

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
        UpdateRoomPlantCount().update_count(room.id)
        db.session.commit()

        return AddPlant(plant=plant)

class DeletePlantByName(graphene.Mutation):
    class Arguments:
        plant_name = graphene.String(required=True)

    success = graphene.Boolean()
    
    def mutate(self, info, plant_name):
        plant = Plant.query.filter_by(plant_name=plant_name).first()

        if not plant:
            raise Exception(f"Plant {plant_name} not found")
        db.session.delete(plant)
        UpdateRoomPlantCount().update_count(plant.room_id)
        db.session.commit()
        
        return DeletePlantByName(success=True)

class UpdatePlantInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    plant_name = graphene.String()
    date_watered = graphene.String()
    room_id = graphene.String()

class UpdatePlant(graphene.Mutation):
    class Arguments:
        plant_data = UpdatePlantInput(required=True)

    success = graphene.Boolean()

    def mutate(self, info, plant_data):
        plant_id = from_global_id(plant_data.id)[1]
        plant = Plant.query.get(plant_id)

        if not plant:
            raise Exception(f"Plant with ID: {plant_id} not found")

        if plant_data.plant_name:
            plant.plant_name = plant_data.plant_name

        if plant_data.date_watered:
            plant.date_watered = plant_data.date_watered

        if plant_data.room_id:
            plant.room_id = plant_data.room_id

        db.session.commit()

        return UpdatePlant(success=True)