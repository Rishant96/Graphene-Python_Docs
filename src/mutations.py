# Mutations is a special ObjectType that also defines an input
import graphene


class CreatePerson(graphene.Mutations):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    person = graphene.Field(lambda: Person)

    def mutate(self, info, name):
        person = Person(name=name)
        ok = True
        return CreatePerson(person=person, ok=ok)


class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()


class MyMutations(graphene.ObjectType):
    create_person = CreatePerson.Field()


# We must define a query for our schema
class Query(graphene.ObjectType):
    person = graphene.Field(Person)

schema = graphene.Schema(query=Query, mutation=MyMutations)
