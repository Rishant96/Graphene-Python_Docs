import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(argument=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, argument):
        return 'hello ' + argument


schema = graphene.Schema(query=Query)

result = schema.execute('{ hello }')
print(result.data['hello'])

result = schema.execute('{ hello(argument: "rishant") }')
print(result.data['hello'])
