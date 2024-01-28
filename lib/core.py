# module consisting of core functions and constants

import math

infinity : float = math.inf
pi : float = 3.1415926535897932385

def deg_to_rad(degrees : float) -> float:
    return degrees * pi / 180.0