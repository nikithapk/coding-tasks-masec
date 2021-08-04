def abra_kadabra(num):
    """Function to check if a given number is multiple of 4, 5 or both

    Args:
        num: int, number to be checked

    Returns: str, result of the operation
    """
    result = ''
    if not num % 4:
        result += 'Abra'
    if not num % 5:
        result += 'Kadabra'
    return result or str(num)


# Test cases
print(abra_kadabra(4))

print(abra_kadabra(5))

print(abra_kadabra(20))

print(abra_kadabra(6))

print(type(abra_kadabra(6)))
