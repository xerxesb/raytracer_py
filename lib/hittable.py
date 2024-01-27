if __name__ == "__main__":
    import sys
    sys.path.append("..")

from lib.ray import Ray
from lib.point3 import Point3
from lib.vec3 import Vec3

class HitRecord:
    def __init__(self, p : Point3, normal : Vec3, t : float):
        self.p = p
        self.normal = normal
        self.t = t

    def __str__(self):
        return f"p: {self.p}, normal: {self.normal}, t: {self.t}"

class Hittable:
    def hit(self, r : Ray, ray_tmin : float, ray_tmax : float, rec : HitRecord) -> bool:
        raise NotImplementedError

# Test
if __name__ == "__main__":
  hr : HitRecord = HitRecord(Point3(1, 2, 3), Vec3(4, 5, 6), 7)
  print(f"Test 1:		{hr}")

  h : Hittable = Hittable()
  print(f"Test 2:		{h}")