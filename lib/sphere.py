if __name__ == "__main__":
    import sys
    sys.path.append("..")

import math
from lib.hittable import Hittable, HitRecord
from lib.point3 import Point3
from lib.vec3 import Vec3
from lib.ray import Ray

class Sphere(Hittable):
    def __init__(self, center : Point3, radius : float):
        self.center = center
        self.radius = radius

    def hit(self, r : Ray, ray_tmin : float, ray_tmax : float, rec : HitRecord) -> bool:
        oc : Vec3 = r.origin - self.center
        a : float = r.direction.length_squared()
        half_b : Vec3 = Vec3.dot(oc, r.direction)
        c : float = oc.length_squared() - self.radius * self.radius

        discriminant : float = half_b * half_b - a * c
        if discriminant < 0:
            return False
        
        sqrtd : float = math.sqrt(discriminant)

        # Find the nearest root that lies in the acceptable range
        root : float = (-half_b - sqrtd) / a
        if root < ray_tmin or ray_tmax < root:
            root = (-half_b + sqrtd) / a
            if root < ray_tmin or ray_tmax < root:
                return False
        
        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal : Vec3 = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)
        return True

    def __str__(self):
        return f"center: {self.center}, radius: {self.radius}"



# Test
if __name__ == "__main__":
    sp : Sphere = Sphere(Point3(1, 2, 3), 4)
    print(f"Test 1:		{sp}")
    print(f"Test 2:		{sp.center}")
    print(f"Test 3:		{sp.radius}")
    print(f"Test 4:		{sp.hit(Ray(Point3(0, 0, 0), Vec3(1, 1, 1)), 0, 100, HitRecord(Point3(0, 0, 0), Vec3(0, 0, 0), 0))}")
    print(f"Test 5:		{sp.hit(Ray(Point3(0, 0, 0), Vec3(1, 1, 1)), 0, 1, HitRecord(Point3(0, 0, 0), Vec3(0, 0, 0), 0))}")
    print(f"Test 6:		{sp.hit(Ray(Point3(0, 0, 0), Vec3(1, 1, 1)), 0, 10, HitRecord(Point3(0, 0, 0), Vec3(0, 0, 0), 0))}")
