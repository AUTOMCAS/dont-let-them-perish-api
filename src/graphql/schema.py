import graphene

from src.graphql.queries.room import RoomQuery
from src.graphql.queries.plant import PlantQuery

from src.graphql.mutations.plant import AddPlant
from src.graphql.mutations.room import AddRoom


class Query(RoomQuery, PlantQuery):
    pass
    
    # node = graphene.relay.Node.Field()
    # all_rooms = SQLAlchemyConnectionField(RoomObject)
    # all_plants = SQLAlchemyConnectionField(PlantObject)


class Mutation(graphene.ObjectType):
    add_plant = AddPlant.Field()
    add_room = AddRoom.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

# schema = graphene.Schema(query=Query)