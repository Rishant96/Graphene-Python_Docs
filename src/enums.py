import graphene
from enum import Enum


class Episode(graphene.Enum):
    NEWHOPE = 4
    EMPIRE = 5
    JEDI = 6

    @property
    def description(self):
        if self == Episode.NEWHOPE:
            return 'New Hope Episode'
        return 'Other episode'


Season = graphene.Enum('Season', [('SPRING', 3), ('SUMMER', 5), ('FALL', 8),
                                  ('WINTER', 11)])


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


def colordescription(value):
    return f'This is the color {value}.'


graphene.Enum.from_enum(Color, colordescription)

# Python style enum member access
assert Color(1) == Color.RED

# Same effect using graphene instead. NOTE: Cannot use python style
assert Episode.get(4) == Episode.NEWHOPE
