import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

from src.graphql.types.room import RoomType
from src.models.models import Room as RoomModel

class RoomQuery(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    
    all_rooms = SQLAlchemyConnectionField(RoomType)
    room_by_name = graphene.Field(RoomType, room_name=graphene.String())

    def resolve_room_by_name(self, info, room_name):
        query = RoomType.get_query(info)
        return query.filter(RoomModel.room_name == room_name).first()

