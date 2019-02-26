from graphene import Schema

# A Schema is created by supplying the root types for each type of operation,
# query, mutation (optional).
# A schema definition is then supplied to the validator and executor.
# Eg.,
my_schema = Schema(
    query=MyRootSchema,
    mutation=MyRootMutation,
    # Some times the schema cannot access all the types that we plan to have.
    # For example, when a field returns an 'Interface', the schema doesn't
    # know about any of the implementations.
    # (In this case we need to use the 'types' argument
    # when creating the Schema)
    types=[SomeExtraObjectType, ]
)

# QUERYING: to query a schema, call the 'execute' method on it.
my_schema.execute('{ lastName }')


# Auto 'camelCase' field names (from 'snake_case')
class Person(graphene.ObjectType):
    last_name = graphene.String()
    other_name = graphene.String(name='_other_Name')
    """
        Your query should look like:

        {
            lastName
            _other_Name
        }
    """
# To disable this behaviour, set the 'auto_camelcase' to 'False' upon
# schema instantiation.
my_schema_no_auto = Schema(
    query=MyRootQuery,
    auto_camelcase=False,
)
