import math
import sys

if __name__ == "__main__":
    sys.path.append("..")

from lib.core import *

# Forward declaration of Vec3 class to allow for operator overloading
class Vec3:
    pass

class Vec3:
    def __init__(self, x : float, y : float, z : float):
        self.x = x
        self.y = y
        self.z = z
    
    # Operator overloads
    def __add__(self, other : Vec3):
        return Vec3(self.x + other.x, 
                    self.y + other.y, 
                    self.z + other.z
                    )

    def __sub__(self, other : Vec3):
        return Vec3(self.x - other.x, 
                    self.y - other.y, 
                    self.z - other.z
                    )

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return Vec3(self.x * other.x, 
                        self.y * other.y, 
                        self.z * other.z
                        )
        else:
            return Vec3(self.x * other, 
                        self.y * other, 
                        self.z * other
                        )
    
    def __rmul__(self, other):
        if isinstance(other, self.__class__):
            return Vec3(other.x * self.x, 
                        other.y * self.y, 
                        other.z * self.z
                        )
        else:
            return Vec3(other * self.x, 
                        other * self.y, 
                        other * self.z
                        )
    
    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return Vec3(self.x / other.x, 
                        self.y / other.y, 
                        self.z / other.z
                        )
        else:
            return Vec3(self.x / other, 
                        self.y / other, 
                        self.z / other
                        )

    def __rtruediv__(self, other):
        if isinstance(other, self.__class__):
            return Vec3(other.x / self.x, 
                        other.y / self.y, 
                        other.z / self.z
                        )
        else:
            return Vec3(other / self.x, 
                        other / self.y, 
                        other / self.z
                        )

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def replace(self, other : Vec3) -> None:
        self.x = other.x
        self.y = other.y
        self.z = other.z

    def length(self):
        return math.sqrt(self.length_squared())

    def length_squared(self):
        return self.x * self.x + self.y * self.y + self.z * self.z
    
    def near_zero(self) -> bool:
        # Return true if the vector is close to zero in all dimensions
        s : float = 1e-8
        return (abs(self.x) < s) and (abs(self.y) < s) and (abs(self.z) < s)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    # Static class methods

    @staticmethod
    def dot(u : Vec3, v : Vec3) -> float:
        return u.x * v.x + u.y * v.y + u.z * v.z


    @staticmethod
    def cross(u : Vec3, v : Vec3) -> Vec3:
        return Vec3(u.y * v.z - u.z * v.y,
                    u.z * v.x - u.x * v.z,
                    u.x * v.y - u.y * v.x
                    )

    @staticmethod
    def unit_vector(v : Vec3) -> Vec3:
        return v / v.length()

    @staticmethod
    def random(min : float = None, max : float = None) -> Vec3:
        if min is None and max is None:
            return Vec3(random_float(), random_float(), random_float())
        else:
            return Vec3(random_float(min, max), random_float(min, max), random_float(min, max))

    @staticmethod
    def random_in_unit_sphere() -> Vec3:
        while True:
            p : Vec3 = Vec3.random(-1, 1)
            if p.length_squared() >= 1:
                continue
            return p
    
    @staticmethod
    def random_unit_vector() -> Vec3:
        return Vec3.unit_vector(Vec3.random_in_unit_sphere())

    @staticmethod
    def random_on_hemisphere(normal : Vec3) -> Vec3:
        on_unit_sphere : Vec3 = Vec3.random_unit_vector()
        return on_unit_sphere if Vec3.dot(on_unit_sphere, normal) > 0 else -on_unit_sphere

    @staticmethod
    def reflect(v : Vec3, n : Vec3) -> Vec3:
        return v - 2 * Vec3.dot(v, n) * n


# Test
if __name__ == "__main__":
    v = Vec3(1.1, 2.2, 3)
    print(f"Test 1:		{v}")
    print(f"Test 2:		{v.x}, {v.y}, {v.z}")
    print(f"Test 3:		{v.length_squared()}")
    print(f"Test 4:		{v + v}")
    print(f"Test 5:		{v - v}")
    print(f"Test 6:		{v * v}")
    print(f"Test 7:		{v / 2}")
    print(f"Test 8:		{2 / v}")
    print(f"Test 9:		{v * 2}")
    print(f"Test 10:	{2 * v}")
    print(f"Test 11:	{v / v}")
    print(f"Test 12:	{-v}")
    print(f"Test 13:	{v * Vec3(2, 3, 4)}")
    print(f"Test 14:	{Vec3(2, 3, 4) * v}")
    print(f"Test 15:	{Vec3.dot(v, Vec3(2, 3, 4))}")
    print(f"Test 16:	{Vec3.cross(v, Vec3(2, 3, 4))}")
    print(f"Test 17:	{Vec3.unit_vector(v)}")
    print(f"Test 18:	{Vec3.random()}")
    print(f"Test 19:	{Vec3.random(1, 2)}")
    print(f"Test 20:	{Vec3.random_in_unit_sphere()}")
    print(f"Test 21:	{Vec3.random_unit_vector()}")
    print(f"Test 22:	{Vec3.random_on_hemisphere(Vec3(1, 1, 1))}")

    v.replace(Vec3(4, 5, 6))
    print(f"Test 23:	{v}")

    v = Vec3(0, 0, 0)
    print(f"Test 24:	{v.near_zero()}")

    v = Vec3(0.00000001, 0.00000001, 0.00000001)
    print(f"Test 25:	{v.near_zero()}")
    print(f"Test 26:	{Vec3.reflect(Vec3(1, 1, 1), Vec3(1, 1, 1))}")
