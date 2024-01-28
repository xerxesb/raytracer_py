if __name__ == "__main__":
    import sys
    sys.path.append("..")

from lib.vec3 import Vec3
from lib.interval import Interval

# Forward declaration of Vec3 class to allow for operator overloading
class Color:
    pass

# Color class is an alias for Vec3
class Color(Vec3):
    def __init__(self, x, y=0, z=0):
        if isinstance(x, Vec3):
            super().__init__(x.x, x.y, x.z)
        else:
            super().__init__(x, y, z)

    def __str__(self):
        return f"{int(256 * self.x)} {int(256 * self.y)} {int(256 * self.z)}"

    def __add__(self, other : Color):
        return Color(super().__add__(other))
    
    def __sub__(self, other : Color):
        return Color(super().__sub__(other))

    def __mul__(self, other : Color):
        return Color(super().__mul__(other))
    
    def __rmul__(self, other : Color):
        return Color(super().__rmul__(other))
    
    def __truediv__(self, other : Color):
        return Color(super().__truediv__(other))
    
    def __rtruediv__(self, other : Color):
        return Color(super().__rtruediv__(other))
    
    # undefine length method
    def length_squared(self):
        raise NotImplementedError

    def length(self):
        raise NotImplementedError

    def get_aliased_color(self, samples_per_pixel : int):
        scale = 1 / samples_per_pixel
        r = self.x * scale
        g = self.y * scale
        b = self.z * scale

        intensity : Interval = Interval(0.0, 0.999)
        return Color(intensity.clamp(r), intensity.clamp(g), intensity.clamp(b))



# Test
if __name__ == "__main__":
    p = Color(0.1, 0.2, 1)
    print(f"Test 1:		{p}")
    print(f"Test 2:		{p + p}")
    print(f"Test 3:		{p - p}")
    print(f"Test 4:		{p * 2}")
    print(f"Test 5:		{2 * p}")
    print(f"Test 6:		{p / 2}")
    print(f"Test 7:		{p / p}")
    print(f"Test 8:		{p.get_aliased_color(1)}")
    print(f"Test 9:		{p.get_aliased_color(100)}")
