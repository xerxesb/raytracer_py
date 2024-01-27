if __name__ == "__main__":
    import sys
    sys.path.append("..")

from lib.vec3 import Vec3

# Point3 class is an alias for Vec3
Point3 = Vec3

# Test
if __name__ == "__main__":
    p = Point3(1, 2, 3)
    print(f"Test 1:		{p}")
    print(f"Test 2:		{p + p}")