def min_to_s(num_minute: int) -> int:
    """ Minute to seconde

    Minute to seconde helps us to convert minute to seconde.

    :param num_minute: number of minute which you want to convert.
    :return: the number of second you have.
    """
    return num_minute * 60


def hour_to_min(num_hour: float) -> float:
    """Hour to minutes

    Hour to minute helps us to convert hour to minute.

    :param num_hour: number of minute which you want to convert.
    :return: the number of minute you have.
    """
    return num_hour * 60


def day_to_hour(num_day: float) -> float:
    """ Day to hour

    Day to hour helps us to convert day to hour.

    :param num_day: number of minute which you want to convert.
    :return: the number of hour you have.
    """
    return num_day * 24


def week_to_day(num_week: float) -> float:
    """Week to day

    Week to day helps us to convert week to day.

    :param num_week: number of week which you want to convert.
    :return: the number of day you have.
    """
    return num_week * 7


def month_to_day(num_month: float, name_month: int, year: int) -> float:
    """Month to day

    Month to day helps us to convert Month to day.

    :param num_month: number of month which you want to convert.
    :param name_month: the name of the month you want to convert.
    :param year: give the year in which you want to convert.
    :return: the number of day you have.
    """
    if num_month == 1:
        if name_month == 1:
            return 31
        elif name_month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return 29
            return 28
        elif name_month == 3:
            return 30

    return num_month * 30


def year_to_day(year: int) -> int:
    """Year to day

    convert year to day.

    :param year: the year you have to convert
    :return: numbre of day of your year
    """
    return 366 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 365


def small_to_big_convertion(small_unit: int, const_divider: int) -> tuple:
    """Small to big converter

    Helps us to convert the small units to the big one. Like day to year or day to month.

    :param small_unit: the small unit which is concern.
    :param const_divider: the big one constante which is concern like 7 for weeks, or 30 for month
    :return: number of big unit concern by the conversion and the rest of the conversion
    """
    num_big_unit = small_unit // const_divider
    rest_big_unit = small_unit - (num_big_unit * const_divider)
    return num_big_unit, rest_big_unit


def s_to_min(num_seconde: int) -> tuple:
    """ Seconde to minutes

    convert seconde to minute

    :param num_seconde: number of seconde you want to convert.
    :return: number of minutes after convertion.
    """
    return small_to_big_convertion(num_seconde, 60)


def min_to_hour(num_minute: int) -> tuple:
    """ Minutes to hours

    :param num_minute: number of minutes we want to convert.
    :return: number of hour after conversion.
    """
    return small_to_big_convertion(num_minute, 60)


def hour_to_day(num_hour: int) -> tuple:
    """ Hours to day

    :param num_hour: number of hours we want to convert.
    :return: number of day after conversion.
    """
    return small_to_big_convertion(num_hour, 24)


def day_to_week(num_day: int) -> tuple:
    """ Days to week

    :param num_day: number of day we want to convert.
    :return: number of week after conversion.
    """
    return small_to_big_convertion(num_day, 7)


def day_to_month(num_day: int) -> tuple:
    """ Days to month

    :param num_day: number of day we want to convert.
    :return: number of month after conversion.
    """
    return small_to_big_convertion(num_day, 30)


def day_to_year(num_day: int) -> tuple:
    """ Days to year

    :param num_day: number of day we want to convert.
    :return: number of year after conversion.
    """
    return small_to_big_convertion(num_day, 365)
