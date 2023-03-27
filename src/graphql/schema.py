import graphene

from src.graphql.queries.room import RoomQuery
from src.graphql.queries.plant import PlantQuery

from src.graphql.mutations.room import AddRoom, DeleteRoomByName, UpdateRoom
from src.graphql.mutations.plant import AddPlant, DeletePlantByName, UpdatePlant



class Query(RoomQuery, PlantQuery):
    pass

class Mutation(graphene.ObjectType):
    add_room = AddRoom.Field()
    add_plant = AddPlant.Field()
    
    delete_room_by_name = DeleteRoomByName.Field()
    delete_plant_by_name = DeletePlantByName.Field()

    update_room = UpdateRoom.Field()
    update_plant = UpdatePlant.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
