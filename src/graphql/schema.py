import graphene

from src.graphql.queries.room import RoomQuery

from src.graphql.mutations.plant import AddPlant


class Query(RoomQuery):
    pass
    
    # node = graphene.relay.Node.Field()
    # all_rooms = SQLAlchemyConnectionField(RoomObject)
    # all_plants = SQLAlchemyConnectionField(PlantObject)


class Mutation(graphene.ObjectType):
    add_plant = AddPlant.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

# schema = graphene.Schema(query=Query)