if __name__ == "__main__":
    import sys
    sys.path.append("..")

from lib.ray import Ray
from lib.point3 import Point3
from lib.vec3 import Vec3

class HitRecord:
    def __init__(self, p : Point3, normal : Vec3, t : float, front_face : bool = True):
        self.p = p
        self.normal = normal
        self.t = t
        self.front_face = front_face

    def set_face_normal(self, r : Ray, outward_normal : Vec3) -> None:
        # Sets the hit record normal vector
        # Note: The outward_normal is assumed to be a unit vector
        self.front_face = Vec3.dot(r.direction, outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal

    def __str__(self):
        return f"p: {self.p}, normal: {self.normal}, t: {self.t}, front_face: {self.front_face}"

class Hittable:
    def hit(self, r : Ray, ray_tmin : float, ray_tmax : float, rec : HitRecord) -> bool:
        raise NotImplementedError

# Test
if __name__ == "__main__":
  h : Hittable = Hittable()
  hr : HitRecord = HitRecord(Point3(1, 2, 3), Vec3(1, 2, 3), 4)
  print(f"Test 1:		{h}")
  print(f"Test 2:		{hr}")
  print(f"Test 3:		{hr.set_face_normal(Ray(Point3(0, 0, 0), Vec3(1, 1, 1)), Vec3(0, 0, 0))}")
  print(f"Test 4:		{hr}")
