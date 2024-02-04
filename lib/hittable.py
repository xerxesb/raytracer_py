if __name__ == "__main__":
    import sys
    sys.path.append("..")

from lib.color import Color
from lib.interval import Interval
from lib.hitrecord import HitRecord
from lib.point3 import Point3
from lib.ray import Ray
from lib.vec3 import Vec3

class Hittable:
    def hit(self, r : Ray, ray_t : Interval, rec : HitRecord) -> bool:
        raise NotImplementedError

class Hittables(Hittable):
    def __init__(self, objects : list):
        self.objects = objects

    def add(self, object : Hittable):
        self.objects.append(object)

    def clear(self):
        self.objects.clear()

    def hit(self, r : Ray, ray_t : Interval, rec : HitRecord) -> bool:
        temp_rec : HitRecord = HitRecord(Point3(0, 0, 0), Vec3(0, 0, 0), 0)
        hit_anything : bool = False
        closest_so_far : float = ray_t.max

        for object in self.objects:
            if object.hit(r, Interval(ray_t.min, closest_so_far), temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec.replace(temp_rec)
        
        return hit_anything

class TestMaterial():
    def scatter(self, r_in : Ray, rec : HitRecord, attenuation : Color, scattered : Ray) -> bool:
        return False


class TestHittable(Hittable):
    def __init__(self, is_hit : bool = True):
        self.is_hit = is_hit
        self.material = TestMaterial()

    def hit(self, r : Ray, ray_t : Interval, rec : HitRecord) -> bool:
        rec.set_material(self.material)
        return self.is_hit


# Test
if __name__ == "__main__":
    hs1 : Hittables = Hittables([TestHittable(False)])
    hs2 : Hittables = Hittables([TestHittable(False), TestHittable(False)])
    hs3 : Hittables = Hittables([TestHittable(False), TestHittable(False), TestHittable(True)])
    print(f"Test 5:		{hs1.hit(Ray(Point3(0, 0, 0), Vec3(1, 1, 1)), Interval(0, 100), HitRecord(Point3(0, 0, 0), Vec3(0, 0, 0), 0))}")
    print(f"Test 6:		{hs2.hit(Ray(Point3(0, 0, 0), Vec3(1, 1, 1)), Interval(0, 100), HitRecord(Point3(0, 0, 0), Vec3(0, 0, 0), 0))}")  
    print(f"Test 7:		{hs3.hit(Ray(Point3(0, 0, 0), Vec3(1, 1, 1)), Interval(0, 100), HitRecord(Point3(0, 0, 0), Vec3(0, 0, 0), 0))}")
