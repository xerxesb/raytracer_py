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

class Lambertain(Material):
    def __init__(self, albedo : Color):
        self.albedo = albedo

    def scatter(self, r_in : Ray, rec : HitRecord, attenuation : Color, scattered : Ray) -> bool:
        scatter_direction : Vec3 = rec.normal + Vec3.random_unit_vector()

        # Catch degenerate scatter direction
        if scatter_direction.near_zero():
            scatter_direction = rec.normal

        scattered.replace(Ray(rec.p, scatter_direction))
        attenuation.replace(self.albedo)
        return True
    
    def __str__(self) -> str:
        return f"Lambertain: {self.albedo}"

class Metal(Material):
    def __init__(self, albedo : Color):
        self.albedo = albedo

    def scatter(self, r_in : Ray, rec : HitRecord, attenuation : Color, scattered : Ray) -> bool:
        reflected : Vec3 = Vec3.reflect(Vec3.unit_vector(r_in.direction), rec.normal)
        scattered.replace(Ray(rec.p, reflected))
        attenuation.replace(self.albedo)
        return True

# Tests
if __name__ == "__main__":
    print(f"Test 1:		{Lambertain(Color(0.5, 0.5, 0.5))}")
    print(f"Test 2:		{Lambertain(Color(0.5, 0.5, 0.5)).albedo}")
    print(f"Test 3:		{Lambertain(Color(0.5, 0.5, 0.5)).scatter(Ray(Vec3(0, 0, 0), Vec3(1, 1, 1)), HitRecord(Vec3(0, 0, 0), Vec3(0, 0, 0), 0), Color(0, 0, 0), Ray(Vec3(0, 0, 0), Vec3(0, 0, 0)))}")
    print(f"Test 4:		{Metal(Color(0.5, 0.5, 0.5))}")
    print(f"Test 5:		{Metal(Color(0.5, 0.5, 0.5)).albedo}")
    print(f"Test 6:		{Metal(Color(0.5, 0.5, 0.5)).scatter(Ray(Vec3(0, 0, 0), Vec3(1, 1, 1)), HitRecord(Vec3(0, 0, 0), Vec3(0, 0, 0), 0), Color(0, 0, 0), Ray(Vec3(0, 0, 0), Vec3(0, 0, 0)))}")