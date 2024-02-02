import math


def degree_to_rad(degree_value: float) -> float:
    """Degree to rad

    Degree to rad helps us to transform a degree angle value to a radiant angle value.

    :param degree_value: the value of your angle in degree
    :return: the value of your angle in radiant
    """
    return math.radians(degree_value)


def rad_to_degree(rad_value: float) -> float:
    """Rad to degree

    Rad to degree helps us to transform a radiant angle value to a degree angle value.

    :param rad_value: the value of your angle in radiant
    :return: te value of your angle in degree
    """
    return math.degrees(rad_value)
