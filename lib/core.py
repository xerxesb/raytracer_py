# module consisting of core functions and constants

import random
import math

infinity : float = math.inf
pi : float = 3.1415926535897932385

def deg_to_rad(degrees : float) -> float:
    return degrees * pi / 180.0

def random_float(min : float = None, max : float = None) -> float:
    if min is None and max is None:
        return random.random()
    return min + (max - min) * random_float()