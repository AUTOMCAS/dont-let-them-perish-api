import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

from src.graphql.types.room import RoomType

class RoomQuery(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_rooms = SQLAlchemyConnectionField(RoomType)


