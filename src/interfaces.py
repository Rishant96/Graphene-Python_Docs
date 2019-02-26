import graphene


# An interface is an abstract data type that defines a certain set of fields
# that a type must include to implement the interface.
class Character(graphene.Interface):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    friends = graphene.List(lambda: Character)

    @classmethod
    def resolve_type(cls, instance, info):
        if instance.type == 'DROID':
            return Droid
        return Human


class Human(graphene.ObjectType):
    class Meta:
        interfaces = (Character, )

    starships = graphene.List(Starship)
    home_planet = graphene.String()


class Droid(graphene.ObjectType):
    class Meta:
        interfaces = (Character, )

    primary_function = graphene.String()


class Query(graphene.ObjectType):
    hero = graphene.Field(
            Character,
            required=True,
            episode=graphene.Int(required=True)
        )

    def resolve_hero(self, info, episode):
        # Luke is the hero of Episode V
        if episode == 5:
            return get_human(name='Luke Skywalker')
        return get_droid(name='R2-D2')


schema = graphene.Schema(query=Query, types=[Human, Droid])
