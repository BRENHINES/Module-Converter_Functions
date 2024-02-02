def celcius_to_far(celcius_value: float) -> float:
    """Celcius to fahrenheit

    This function helps us to calculate the heat in fahrenheit by celcius.

    :param celcius_value: the value of the heat in celcius.
    :return: the value of the heat in farhenheit.
    """
    return (celcius_value - 32) * (5 / 9)


def celcius_to_kelvin(celcius_value: float) -> float:
    """Celcius to kelvin

    This function helps us to calculate the heat in kelvin by celcius.

    :param celcius_value: the value of the heat in celcius.
    :return: the value of the heat in kelvin.
    """
    return celcius_value + 273.15


def far_to_celcius(far_value: float) -> float:
    """Farhenheit to celcius

    This function helps us to calculate the heat in celcius by farhenheit.

    :param far_value: the farhenheit heat value.
    :return: the value of the heat in celcius.
    """
    return (far_value * (9 / 5)) + 32


def kelvin_to_celcius(kelvin_value: float) -> float:
    """Kelvin to celcius

    This function helps us to calculate the heat in celcius by kelvin.

    :param kelvin_value: the kelvin heat value.
    :return: the value of the heat in celcius.
    """
    return kelvin_value - 273.15
