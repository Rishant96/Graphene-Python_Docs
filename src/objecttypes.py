import graphene


class Person(graphene.ObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    full_name = graphene.String()

    def resolve_full_name(self, info):
        return f'{self.first_name} {self.last_name}'


class Query(graphene.ObjectType):
    reverse = graphene.String(word=graphene.String())

    def resolve_reverse(self, info, word):
        return word[::-1]


# Resolvers outside the ObjectType class
def reverse(root, info, word):
    return word[::-1]


class Query_2(graphene.ObjectType):
    reverse = graphene.String(word=graphene.String(), resolver=reverse)
