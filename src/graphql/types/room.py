import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from src.models.models import Room as RoomModel

class RoomType(SQLAlchemyObjectType):
   class Meta:
       model = RoomModel
       interfaces = (graphene.relay.Node, )