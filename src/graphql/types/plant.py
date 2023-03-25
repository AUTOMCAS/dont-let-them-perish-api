import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from src.models.models import Plant as PlantModel

class PlantType(SQLAlchemyObjectType):
   class Meta:
       model = PlantModel
       interfaces = (graphene.relay.Node, )