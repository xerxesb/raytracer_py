if __name__ == "__main__":
    import sys
    sys.path.append("..")

from lib.ray import Ray
from lib.point3 import Point3
from lib.vec3 import Vec3

class HitRecord:
  pass

class HitRecord:
    def __init__(self, p : Point3, normal : Vec3, t : float, front_face : bool = True):
        self.p = p
        self.normal = normal
        self.t = t
        self.front_face = front_face

    def replace(self, other : HitRecord) -> None:
        self.p = other.p
        self.normal = other.normal
        self.t = other.t
        self.front_face = other.front_face

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

class Hittables(Hittable):
    def __init__(self, objects : list):
        self.objects = objects

    def add(self, object : Hittable):
        self.objects.append(object)
      
    def clear(self):
        self.objects.clear()

    def hit(self, r : Ray, ray_tmin : float, ray_tmax : float, rec : HitRecord) -> bool:
        temp_rec : HitRecord = HitRecord(Point3(0, 0, 0), Vec3(0, 0, 0), 0)
        hit_anything : bool = False
        closest_so_far : float = ray_tmax

        for object in self.objects:
            if object.hit(r, ray_tmin, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec.replace(temp_rec)
        
        return hit_anything

# Test
if __name__ == "__main__":
  class TestHittable(Hittable):
    def __init__(self, is_hit : bool = True):
      self.is_hit = is_hit

    def hit(self, r : Ray, ray_tmin : float, ray_tmax : float, rec : HitRecord) -> bool:
      return self.is_hit


  h : Hittable = Hittable()
  hr : HitRecord = HitRecord(Point3(1, 2, 3), Vec3(1, 2, 3), 4)
  print(f"Test 1:		{h}")
  print(f"Test 2:		{hr}")

  hr.set_face_normal(Ray(Point3(0, 0, 0), Vec3(1, 1, 1)), Vec3(0, 0, 0))
  print(f"Test 3:		{hr}") 

  hr2 : HitRecord = HitRecord(Point3(4, 5, 6), Vec3(4, 5, 6), 7)
  hr.replace(hr2)
  print(f"Test 4:		{hr}")

  hs1 : Hittables = Hittables([TestHittable(False)])
  hs2 : Hittables = Hittables([TestHittable(False), TestHittable(False)])
  hs3 : Hittables = Hittables([TestHittable(False), TestHittable(False), TestHittable(True)])
  print(f"Test 5:		{hs1.hit(Ray(Point3(0, 0, 0), Vec3(1, 1, 1)), 0, 100, HitRecord(Point3(0, 0, 0), Vec3(0, 0, 0), 0))}")
  print(f"Test 6:		{hs2.hit(Ray(Point3(0, 0, 0), Vec3(1, 1, 1)), 0, 100, HitRecord(Point3(0, 0, 0), Vec3(0, 0, 0), 0))}")  
  print(f"Test 7:		{hs3.hit(Ray(Point3(0, 0, 0), Vec3(1, 1, 1)), 0, 100, HitRecord(Point3(0, 0, 0), Vec3(0, 0, 0), 0))}")
