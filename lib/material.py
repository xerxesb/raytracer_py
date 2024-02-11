import math

if __name__ == "__main__":
    import sys
    sys.path.append("..")

from lib.core import *
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
    def __init__(self, albedo : Color, fuzz : float = 0):
        self.albedo = albedo
        self.fuzz = min(fuzz, 1)

    def scatter(self, r_in : Ray, rec : HitRecord, attenuation : Color, scattered : Ray) -> bool:
        reflected : Vec3 = Vec3.reflect(Vec3.unit_vector(r_in.direction), rec.normal)
        scattered.replace(Ray(rec.p, reflected + self.fuzz * Vec3.random_in_unit_sphere()))
        attenuation.replace(self.albedo)
        return Vec3.dot(scattered.direction, rec.normal) > 0
    
    def __str__(self) -> str:
        return f"Metal: {self.albedo} {self.fuzz}"

class Dielectric(Material):
    def __init__(self, index_of_refraction : float):
        self.index_of_refraction = index_of_refraction

    def scatter(self, r_in : Ray, rec : HitRecord, attenuation : Color, scattered : Ray) -> bool:
        attenuation.replace(Color(1.0, 1.0, 1.0))
        refraction_ratio : float = (1.0/self.index_of_refraction) if rec.front_face else self.index_of_refraction

        unit_direction : Vec3 = Vec3.unit_vector(r_in.direction)
        cos_theta : float = min(Vec3.dot(-unit_direction, rec.normal), 1.0)
        sin_theta: float = math.sqrt(1.0 - cos_theta**2)

        cannot_refract : bool = refraction_ratio * sin_theta > 1.0
        direction : Vec3 = (Vec3.reflect(unit_direction, rec.normal) 
                            if cannot_refract or self.reflectance(cos_theta, refraction_ratio) > random_float()
                            else Vec3.refract(unit_direction, rec.normal, refraction_ratio)
        )

        scattered.replace(Ray(rec.p, direction))
        return True

    def reflectance(self, cosine : float, ref_idx : float) -> float:
        # Use Schlick's approximation for reflectance
        r0 : float = (1 - ref_idx) / (1 + ref_idx)
        r0 *= r0
        return r0 + (1 - r0) * (1 - cosine)**5

    def __str__(self) -> str:
        return f"Dielectric: {self.index_of_refraction}"


# Tests
if __name__ == "__main__":
    print(f"Test 1:		{Lambertain(Color(0.5, 0.5, 0.5))}")
    print(f"Test 2:		{Lambertain(Color(0.5, 0.5, 0.5)).albedo}")
    print(f"Test 3:		{Lambertain(Color(0.5, 0.5, 0.5)).scatter(Ray(Vec3(0, 0, 0), Vec3(1, 1, 1)), HitRecord(Vec3(0, 0, 0), Vec3(0, 0, 0), 0), Color(0, 0, 0), Ray(Vec3(0, 0, 0), Vec3(0, 0, 0)))}")
    print(f"Test 4:		{Metal(Color(0.5, 0.5, 0.5))}")
    print(f"Test 5:		{Metal(Color(0.5, 0.5, 0.5)).albedo}")
    print(f"Test 6:		{Metal(Color(0.5, 0.5, 0.5), 1).scatter(Ray(Vec3(0, 0, 0), Vec3(1, 1, 1)), HitRecord(Vec3(0, 0, 0), Vec3(0, 0, 0), 0), Color(0, 0, 0), Ray(Vec3(0, 0, 0), Vec3(0, 0, 0)))}")
    print(f"Test 7:		{Dielectric(1.5)}")