from math import floor


def mango(quantity: int, price: int) -> int:
    return (quantity - floor(quantity / 3)) * price
