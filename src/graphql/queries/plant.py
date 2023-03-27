import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

from src.graphql.types.plant import PlantType
from src.models.models import Plant as PlantModel

class PlantQuery(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_plants = SQLAlchemyConnectionField(PlantType)
    
    plant_by_name = graphene.Field(PlantType, plant_name=graphene.String())

    def resolve_plant_by_name(self, info, plant_name):
        query = PlantType.get_query(info)
        return query.filter(PlantModel.plant_name == plant_name).first()