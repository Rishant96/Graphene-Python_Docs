# These are type modifiers
import graphene


# Non-Null
class Character(graphene.ObjectType):
    name = graphene.NonNull(graphene.String)

    # Equivalent alternative
    name_alt = graphene.String(required=True)


# List
class Character_2(graphene.ObjectType):
    appears_in = graphene.List(graphene.String)


# Non-null and List (experiments)
class Character_3(graphene.ObjectType):
    # Non-null lists
    appears_in_1 = graphene.NonNull(graphene.List(graphene.String))
    appears_in_1_alt = graphene.List(graphene.String, required=True)

    # List of non-nulls
    appears_in_2 = graphene.List(graphene.NonNull(graphene.String))
    # appears_in_2_alt = graphene.List(graphene.String(required=True))

    # Non-null lists
    appears_in_3 = graphene.List(graphene.NonNull(graphene.String))
