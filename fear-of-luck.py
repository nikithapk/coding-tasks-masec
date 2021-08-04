import datetime


def has_saturday_eight(month, year):
    """Function to check if 8th day of a given month and year is Friday

    Args:
        month: int, month number
        year: int, year

    Returns: Boolean
    """

    return True if datetime.date(year, month, 8).weekday() == 5 else False


# Test cases
print(has_saturday_eight(5, 2021))

print(has_saturday_eight(9, 2017))

print(has_saturday_eight(1, 1985))
