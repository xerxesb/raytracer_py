if __name__ == "__main__":
    import sys
    sys.path.append("..")

from lib.vec3 import Vec3
from lib.point3 import Point3

# Forward declaration of Ray class to allow for circular reference
class Ray:
    pass

class Ray:
    def __init__(self, origin : Point3, direction : Vec3):
        self.origin = origin
        self.direction = direction

    def at(self, t : float):
        return self.origin + t * self.direction

    def replace(self, other : Ray):
        self.origin = other.origin
        self.direction = other.direction

    def __str__(self):
        return f"origin: {self.origin}, direction: {self.direction}"

# Test
if __name__ == "__main__":
    r = Ray(Point3(1, 2, 3), Vec3(1, 2, 3))
    print(f"Test 1:		{r}")
    print(f"Test 2:		{r.at(0)}")
    print(f"Test 3:		{r.at(1)}")
    print(f"Test 4:		{r.at(2)}")
    print(f"Test 5:		{r.at(-2)}")
    print(f"Test 6:		{r.at(2) - r.at(1)}")

    r.replace(Ray(Point3(4, 5, 6), Vec3(4, 5, 6)))
    print(f"Test 7:		{r}")