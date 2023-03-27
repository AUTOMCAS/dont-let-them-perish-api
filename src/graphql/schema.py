import graphene

from src.graphql.queries.room import RoomQuery
from src.graphql.queries.plant import PlantQuery

from src.graphql.mutations.room import AddRoom, DeleteRoomByName
from src.graphql.mutations.plant import AddPlant, DeletePlantByName



class Query(RoomQuery, PlantQuery):
    pass
    
    # node = graphene.relay.Node.Field()
    # all_rooms = SQLAlchemyConnectionField(RoomObject)
    # all_plants = SQLAlchemyConnectionField(PlantObject)


class Mutation(graphene.ObjectType):
    add_room = AddRoom.Field()
    add_plant = AddPlant.Field()
    
    delete_room_by_name = DeleteRoomByName.Field()
    delete_plant_by_name = DeletePlantByName.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
