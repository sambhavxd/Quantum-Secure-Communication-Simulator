import random

def generate_bits(n):
    """
    Generate n random bits
    """
    return [random.randint(0, 1) for _ in range(n)]


def generate_bases(n):
    """
    Generate n random bases

    0 = Rectilinear (+)
    1 = Diagonal (×)
    """
    return [random.randint(0, 1) for _ in range(n)]