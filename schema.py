import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
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
    rooms = SQLAlchemyConnectionField(RoomObject)
    all_plants = SQLAlchemyConnectionField(PlantObject)

schema = graphene.Schema(query=Query)