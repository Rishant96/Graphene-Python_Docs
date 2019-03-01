# An AbstractType contains fields that can be shared among
# 'graphene.ObjectType', 'graphene.Interface',
# 'graphene.InputObjectType' or other 'graphene.AbstractType'.

"""
The basics:

    1. Each AbstractType is a python class that inherits from
        'graphene.AbstractType'.

    2. Each attribute of the 'AbstractType' represents a field
        (a 'graphene.Field' or 'graphene.InputField' depending on
        where it is mouted)
"""

# Example: In this example 'UserFields' is an 'AbstractType' with a name.
#           'User' and 'UserInput' are two types that have their own fields
#           plus the ones defined in 'UserFields'.

import graphene


class UserFields(graphene.AbstractType):
    name = graphene.String()


class User(graphene.ObjectType, UserFields):
    pass


class UserInput(graphene.ObjectType, UserFields):
    pass


"""
type User {
    name: String
}

inputtype UserInput {
    name: String
}
"""
