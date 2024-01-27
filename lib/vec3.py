import math

class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    # Static methods
    def dot(u, v):
        return u.x * v.x + u.y * v.y + u.z * v.z
    
    def cross(u, v):
        return Vec3(u.y * v.z - u.z * v.y,
                    u.z * v.x - u.x * v.z,
                    u.x * v.y - u.y * v.x
                    )

    
    # Operator overloading

    def __add__(self, other):
        return Vec3(self.x + other.x, 
                    self.y + other.y, 
                    self.z + other.z
                    )
          
    def __sub__(self, other):
        return Vec3(self.x - other.x, 
                    self.y - other.y, 
                    self.z - other.z
                    )

    def __mul__(self, other):
        if isinstance(other, Vec3):
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
        if isinstance(other, Vec3):
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
        if isinstance(other, Vec3):
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
        if isinstance(other, Vec3):
            return Vec3(other.x / self.x, 
                        other.y / self.y, 
                        other.z / self.z
                        )
        else:
            return Vec3(other / self.x, 
                        other / self.y, 
                        other / self.z
                        )

    def length(self):
        return math.sqrt(self.length_squared())

    def length_squared(self):
        return self.x * self.x + self.y * self.y + self.z * self.z
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


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
    print(f"Test 12:	{v * Vec3(2, 3, 4)}")
    print(f"Test 13:	{Vec3(2, 3, 4) * v}")
    print(f"Test 14:	{Vec3.dot(v, Vec3(2, 3, 4))}")
    print(f"Test 15:	{Vec3.cross(v, Vec3(2, 3, 4))}")
    print(f"Test 16:	{v.cross(Vec3(2, 3, 4))}")
    print(f"Test 17:	{v.cross(v)}")