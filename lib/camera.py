import sys

if __name__ == "__main__":
    sys.path.append("..")

from lib.color import Color
from lib.hittable import Hittable, HitRecord, TestHittable, Hittables
from lib.interval import Interval
from lib.point3 import Point3
from lib.ray import Ray
from lib.vec3 import Vec3

from lib.core import *

class Camera:
    '''A camera class that renders a scene
    
    Attributes:
        aspect_ratio: The aspect ratio of the camera (width / height)
        width: The width of the screen
    
    Properties:
        height: The height of the screen (calculated from aspect_ratio and width)
        camera_center: The center of the camera in 3D space
        pixel_delta_u: The horizontal delta between pixels
        pixel_delta_v: The vertical delta between pixels
        samples_per_pixel: The number of samples per pixel
    '''
    def __init__(self, aspect_ratio : float, width : int):
        self.aspect_ratio : float = aspect_ratio
        self.width : int = width
        self.height : int = (int) (width / aspect_ratio) if (int) (width / aspect_ratio) >= 1 else 1

        self.camera_center : Point3 = Point3(0, 0, 0)
        self.pixel_delta_u : Vec3 = Vec3(0, 0, 0)
        self.pixel_delta_v : Vec3 = Vec3(0, 0, 0)
        self.pixel00_loc : Point3 = Point3(0, 0, 0)
        self.samples_per_pixel : int = 4

    def render(self, world : Hittable):
        self.__initialize() # TODO: Note to future self - the exercise made me do this. I think we can initialize in the ctor
        print(f"P3\n{self.width} {self.height}\n255\n")

        for j in range(self.height):
            print(f"\rScanlines remaining: {self.height - j}", file=sys.stderr, end="\n")
            for i in range(self.width):
                pixel_color : Color = Color(0, 0, 0)
                for _ in range(self.samples_per_pixel):
                    r : Ray = self.get_ray(i, j)
                    pixel_color += self.ray_color(r, world)

                print(f"{pixel_color.get_aliased_color(self.samples_per_pixel)}")

        print(f"\nDone", file=sys.stderr, end="\n")

    def __initialize(self):
        focal_length : float = 1.0
        viewport_height : float = 2.0
        viewport_width : float = viewport_height * self.aspect_ratio

        viewport_u : Vec3 = Vec3(viewport_width, 0, 0)
        viewport_v : Vec3 = Vec3(0, -viewport_height, 0)

        self.pixel_delta_u : Vec3 = viewport_u / self.width
        self.pixel_delta_v : Vec3 = viewport_v / self.height

        viewport_upper_left : Point3 = self.camera_center - Vec3(0, 0, focal_length) - viewport_u / 2 - viewport_v / 2 
        self.pixel00_loc : Point3 = viewport_upper_left + 0.5 * (self.pixel_delta_u + self.pixel_delta_v)

    def ray_color(self, r : Ray, world : Hittable) -> Color:
        rec : HitRecord = HitRecord()

        # If the ray hits an object, return the color of the object
        if world.hit(r, Interval(0, infinity), rec):
            return 0.5 * (Color(rec.normal.x, rec.normal.y, rec.normal.z) + Color(1, 1, 1))

        # Otherwise, return the background color
        unit_direction : Vec3 = Vec3.unit_vector(r.direction)
        t : float = 0.5 * (unit_direction.y + 1.0)
        return (1.0 - t) * Color(1.0, 1.0, 1.0) + t * Color(0.5, 0.7, 1.0)

    def get_ray(self, i : int, j : int) -> Ray:
        pixel_center : Point3 = self.pixel00_loc + (i * self.pixel_delta_u) + (j * self.pixel_delta_v)
        pixel_sample : Point3 = pixel_center + self.pixel_sample_square()
        
        ray_origin : Vec3 = self.camera_center
        ray_direction : Vec3 = pixel_sample - ray_origin
        return Ray(ray_origin, ray_direction)

    def pixel_sample_square(self) -> Vec3:
        px : float = -0.5 + random_float()
        py : float = -0.5 + random_float()
        return (px * self.pixel_delta_u) + (py * self.pixel_delta_v)

# Test
if __name__ == "__main__":
    c : Camera = Camera(16.0 / 9.0, 1)
    c.render(Hittables([TestHittable()]))
    print(f"Test 1:		{c}")
    print(f"Test 2:		{c.aspect_ratio}")
    print(f"Test 3:		{c.width}")
    print(f"Test 4:		{c.height}")
    print(f"Test 5:		{c.camera_center}")
    print(f"Test 6:		{c.pixel_delta_u}")
    print(f"Test 7:		{c.pixel_delta_v}")
    print(f"Test 8:		{c.pixel00_loc}")
    print(f"Test 9:		{c.ray_color(Ray(Point3(0, 0, 0), Vec3(1, 1, 1)), TestHittable())}")
    print(f"Test 10:	{c.get_ray(10, 10)}")
    print(f"Test 11:	{c.pixel_sample_square()}")