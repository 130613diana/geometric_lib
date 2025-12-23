def area(a, b):
    if a < 0 or b < 0:
        raise ValueError("Sides must be non-negative")
    return a * b


def perimeter(a, b):
    if a < 0 or b < 0:
        raise ValueError("Sides must be non-negative")
    return 2 * (a + b)
