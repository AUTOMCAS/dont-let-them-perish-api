import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

from src.graphql.types.plant import PlantType

class PlantQuery(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_plants = SQLAlchemyConnectionField(PlantType)
