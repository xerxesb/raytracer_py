if __name__ == "__main__":
    import sys
    sys.path.append("..")

from lib.ray import Ray
from lib.point3 import Point3
from lib.vec3 import Vec3

class HitRecord:
    pass

# Local definition of Material to avoid circular reference
class Material:
    def __init__(self) -> None:
        raise NotImplementedError
    pass

class HitRecord:
    def __init__(self, p : Point3 = Point3(0, 0, 0), normal : Vec3 = Vec3(0, 0, 0), t : float = 0, front_face : bool = True):
        self.p = p
        self.normal = normal
        self.t = t
        self.front_face = front_face
        self.material = None

    def replace(self, other : HitRecord) -> None:
        self.p = other.p
        self.normal = other.normal
        self.t = other.t
        self.front_face = other.front_face
        self.material = other.material

    def set_face_normal(self, r : Ray, outward_normal : Vec3) -> None:
        # Sets the hit record normal vector
        # Note: The outward_normal is assumed to be a unit vector
        self.front_face = Vec3.dot(r.direction, outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal

    def set_material(self, material : Material) -> None:
        self.material = material

    def __str__(self):
        return f"p: {self.p}, normal: {self.normal}, t: {self.t}, front_face: {self.front_face}, material: {self.material}"


# Test
if __name__ == "__main__":
    hr : HitRecord = HitRecord()
    print(f"Test 1:		{hr}")

    hr.set_face_normal(Ray(Point3(0, 0, 0), Vec3(1, 1, 1)), Vec3(0, 0, 0))
    print(f"Test 2:		{hr}") 

    hr2 : HitRecord = HitRecord(Point3(4, 5, 6), Vec3(4, 5, 6), 7)
    hr.replace(hr2)
    print(f"Test 3:		{hr}")

    # hr.set_material(Material())
    # print(f"Test 4:		{hr}")

    hr.set_face_normal(Ray(Point3(0, 0, 0), Vec3(1, 1, 1)), Vec3(1, 1, 1))
    print(f"Test 5:		{hr}")

