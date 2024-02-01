from lib.point3 import Point3
from lib.hittable import Hittables
from lib.sphere import Sphere
from lib.camera import Camera

DEFINITION = (
    "LOW"
    # "MEDIUM"
    # "HIGH"
    # "ULTRA"
)

ALL_WIDTHS = { "LOW": 400, "MEDIUM": 800, "HIGH": 1200, "ULTRA": 1600}
ALL_SAMPLES_PER_PIXEL = { "LOW": 20, "MEDIUM": 40, "HIGH": 60, "ULTRA": 100 }

if __name__ == "__main__":
    ASPECT_RATIO = 16.0 / 9.0
    WIDTH = ALL_WIDTHS[DEFINITION]
    SAMPLES_PER_PIXEL = ALL_SAMPLES_PER_PIXEL[DEFINITION]

    cam : Camera = Camera(ASPECT_RATIO, WIDTH, SAMPLES_PER_PIXEL)

    world : Hittables = Hittables([
      Sphere(Point3(0, 0, -1), 0.5),
      Sphere(Point3(0, -100.5, -1), 100)
    ])

    cam.render(world)
