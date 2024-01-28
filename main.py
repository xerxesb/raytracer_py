from lib.point3 import Point3
from lib.hittable import Hittables
from lib.sphere import Sphere
from lib.camera import Camera

if __name__ == "__main__":
    WIDTH = 400
    ASPECT_RATIO = 16.0 / 9.0

    cam : Camera = Camera(ASPECT_RATIO, WIDTH)

    world : Hittables = Hittables([
      Sphere(Point3(0, 0, -1), 0.5),
      Sphere(Point3(0, -100.5, -1), 100)
    ])

    cam.render(world)
