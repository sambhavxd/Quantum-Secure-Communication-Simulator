import random

def apply_noise(bit, noise_probability=0.05):

    if random.random() < noise_probability:

        bit = 1 - bit

    return bit