# Custom Scalars
import datetime
import graphene
from graphene.types import Scalar
from graphql.language import ast


class DateTime(Scalar):
    '''DateTime Scalar Description'''

    @staticmethod
    def serialize(dt):
        return dt.isoformat()

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            return datetime.datetime.strptime(
                node.value, "%Y-%m-%dT%H:%M:%S.%f")


# Mounting Scalars
class Person(graphene.ObjectType):
    # Shortcut
    name_1 = graphene.String()
    # Equivalent verbose
    name_2 = graphene.Field(graphene.String)

    # ARGUMENTS: 'to' is a random argument
    field_1 = graphene.Field(graphene.String, to=graphene.String())
    # is equivalent to,
    field_2 = graphene.Field(graphene.String,
                             to=graphene.Argument(graphene.String))

    # Testing custom Scalar type
    date_test_field = DateTime
