import sys

if __name__ == "__main__":
    sys.path.append("..")

from lib.color import Color
from lib.hittable import Hittable, HitRecord, TestHittable
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
    '''
    def __init__(self, aspect_ratio : float, width : int):
        self.aspect_ratio : float = aspect_ratio
        self.width : int = width
        self.height : int = (int) (width / aspect_ratio) if (int) (width / aspect_ratio) >= 1 else 1

        self.camera_center : Point3 = Point3(0, 0, 0)
        self.pixel_delta_u : Vec3 = Vec3(0, 0, 0)
        self.pixel_delta_v : Vec3 = Vec3(0, 0, 0)
        self.pixel00_loc : Point3 = Point3(0, 0, 0)

    def render(self, world : Hittable):
        self.__initialize() # TODO: Note to future self - the exercise made me do this. I think we can initialize in the ctor
        print(f"P3\n{self.width} {self.height}\n255\n")

        for j in range(self.height):
            print(f"\rScanlines remaining: {self.height - j}", file=sys.stderr, end="\n")
            for i in range(self.width):
                pixel_center : Point3 = self.pixel00_loc + (i * self.pixel_delta_u) + (j * self.pixel_delta_v)
                ray_direction : Vec3 = pixel_center - self.camera_center
                r : Ray = Ray(self.camera_center, ray_direction)
                pixel_color = self.ray_color(r, world)
                print(f"{pixel_color}")

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

        if world.hit(r, Interval(0, infinity), rec):
            return 0.5 * (Color(rec.normal.x, rec.normal.y, rec.normal.z) + Color(1, 1, 1))

        unit_direction : Vec3 = Vec3.unit_vector(r.direction)
        t : float = 0.5 * (unit_direction.y + 1.0)
        return (1.0 - t) * Color(1.0, 1.0, 1.0) + t * Color(0.5, 0.7, 1.0)

# Test
if __name__ == "__main__":
    print(f"Test 1:		{Camera(16.0 / 9.0, 400)}")
    print(f"Test 2:		{Camera(16.0 / 9.0, 400).aspect_ratio}")
    print(f"Test 3:		{Camera(16.0 / 9.0, 400).width}")
    print(f"Test 4:		{Camera(16.0 / 9.0, 400).height}")
    print(f"Test 5:		{Camera(16.0 / 9.0, 400).camera_center}")
    print(f"Test 6:		{Camera(16.0 / 9.0, 400).pixel_delta_u}")
    print(f"Test 7:		{Camera(16.0 / 9.0, 400).pixel_delta_v}")
    print(f"Test 8:		{Camera(16.0 / 9.0, 400).pixel00_loc}")
    print(f"Test 9:		{Camera(16.0 / 9.0, 400).ray_color(Ray(Point3(0, 0, 0), Vec3(1, 1, 1)), TestHittable())}")
