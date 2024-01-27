import os
import sys
import math

from lib.color import Color
from lib.ray import Ray
from lib.point3 import Point3
from lib.vec3 import Vec3

# Helper functions

def hit_sphere(center : Point3, radius : float, r : Ray) -> float:
  oc : Vec3 = r.origin - center
  a : Vec3 = Vec3.dot(r.direction, r.direction)
  b : Vec3 = 2.0 * Vec3.dot(oc, r.direction)
  c : Vec3 = Vec3.dot(oc, oc) - radius * radius
  discriminant : float = b * b - 4 * a * c
  return -1.0 if discriminant < 0 else (-b - math.sqrt(discriminant)) / (2.0 * a)

def ray_color(r : Ray) -> Color:
  t : float = hit_sphere(Point3(0, 0, -1), 0.5, r)
  if (t > 0.0):
    n : Vec3 = Vec3.unit_vector(r.at(t) - Vec3(0, 0, -1))
    return 0.5 * Color(n.x + 1, n.y + 1, n.z + 1)

  unit_direction : Vec3 = Vec3.unit_vector(r.direction)
  t : float = 0.5 * (unit_direction.y + 1.0)
  return (1.0 - t) * Color(1.0, 1.0, 1.0) + t * Color(0.5, 0.7, 1.0)


# Image dimensions
width : int = 400
aspect_ratio : float = 16.0 / 9.0
height : int = (int) (width / aspect_ratio) if (int) (width / aspect_ratio) >= 1 else 1

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

      pixel_color = ray_color(r)
      print(f"{pixel_color}")

  print(f"\nDone", file=sys.stderr, end="\n")