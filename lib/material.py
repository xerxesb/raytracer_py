import math

if __name__ == "__main__":
    import sys
    sys.path.append("..")

from lib.color import Color
from lib.hittable import HitRecord
from lib.interval import Interval
from lib.ray import Ray
from lib.vec3 import Vec3

# Base class for materials
class Material:
    def scatter(self, r_in : Ray, rec : HitRecord, attenuation : Color, scattered : Ray) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        return "Material: XXX"


# Tests
if __name__ == "__main__":
    pass