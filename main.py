import os
import sys
import math

from lib.color import Color
from lib.ray import Ray
from lib.point3 import Point3
from lib.vec3 import Vec3
from lib.hittable import Hittable, Hittables, HitRecord
from lib.sphere import Sphere

from lib.core import *

# Helper functions
def ray_color(r : Ray, world : Hittable) -> Color:
  rec : HitRecord = HitRecord(Point3(0, 0, 0), Vec3(0, 0, 0), 0)

  if world.hit(r, 0, infinity, rec):
    return 0.5 * (Color(rec.normal.x, rec.normal.y, rec.normal.z) + Color(1, 1, 1))

  unit_direction : Vec3 = Vec3.unit_vector(r.direction)
  t : float = 0.5 * (unit_direction.y + 1.0)
  return (1.0 - t) * Color(1.0, 1.0, 1.0) + t * Color(0.5, 0.7, 1.0)


# Image dimensions
width : int = 400
aspect_ratio : float = 16.0 / 9.0
height : int = (int) (width / aspect_ratio) if (int) (width / aspect_ratio) >= 1 else 1

# World
world : Hittables = Hittables([
  Sphere(Point3(0, 0, -1), 0.5),
  Sphere(Point3(0, -100.5, -1), 100)
])

# Camera
focal_length : float = 1.0
viewport_height : float = 2.0
viewport_width : float = viewport_height * aspect_ratio
camera_center : Point3 = Point3(0, 0, 0)

# Viewport vectors
viewport_u : Vec3 = Vec3(viewport_width, 0, 0)
viewport_v : Vec3 = Vec3(0, -viewport_height, 0)

# Viewport horizontal and vertical deltas
pixel_delta_u : Vec3 = viewport_u / width
pixel_delta_v : Vec3 = viewport_v / height

# Viewport upper left corner
viewport_upper_left : Point3 = camera_center - Vec3(0, 0, focal_length) - viewport_u / 2 - viewport_v / 2 
pixel00_loc : Point3 = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v)

if __name__ == "__main__":
  print(f"P3\n{width} {height}\n255\n")

  for j in range(height):
    print(f"\rScanlines remaining: {height - j}", file=sys.stderr, end="\n")
    for i in range(width):
      pixel_center : Point3 = pixel00_loc + (i * pixel_delta_u) + (j * pixel_delta_v)
      ray_direction : Vec3 = pixel_center - camera_center
      r : Ray = Ray(camera_center, ray_direction)

      pixel_color = ray_color(r, world)
      print(f"{pixel_color}")

  print(f"\nDone", file=sys.stderr, end="\n")