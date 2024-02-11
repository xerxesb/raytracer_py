from lib.color import Color
from lib.point3 import Point3
from lib.hittable import Hittables
from lib.material import Dielectric, Lambertain, Metal, Material
from lib.sphere import Sphere
from lib.camera import Camera

DEFINITION = (
    "LOW"
    # "MEDIUM"
    # "HIGH"
    # "ULTRA"
    # "4K"
)

ALL_WIDTHS = { "LOW": 400, "MEDIUM": 800, "HIGH": 1200, "ULTRA": 1600, "4K" : 3840 }
ALL_SAMPLES_PER_PIXEL = { "LOW": 20, "MEDIUM": 40, "HIGH": 60, "ULTRA": 100, "4K" : 400 }

if __name__ == "__main__":
    ASPECT_RATIO = 16.0 / 9.0
    WIDTH = ALL_WIDTHS[DEFINITION]
    SAMPLES_PER_PIXEL = ALL_SAMPLES_PER_PIXEL[DEFINITION]

    cam : Camera = Camera(ASPECT_RATIO, WIDTH, SAMPLES_PER_PIXEL)

    mat_ground : Material = Lambertain(Color(0.8, 0.8, 0.0))
    mat_ball_center : Material = Lambertain(Color(0.7, 0.3, 0.3))
    mat_ball_left : Material = Dielectric(1.5)
    mat_ball_right : Material = Metal(Color(0.8, 0.6, 0.2), 0.3)
    mat_ball_behind : Material = Metal(Color(0.1, 0.1, 1), 0.6)

    world : Hittables = Hittables([
        Sphere(Point3(0.0, -100.5, -1.0), 100.0, mat_ground),
        Sphere(Point3(0.0, 0.0, -1.0), 0.5, mat_ball_center),
        Sphere(Point3(-1.2, 0.0, -1.0), 0.5, mat_ball_left),
        Sphere(Point3(1.2, 0.0, -1.0), 0.5, mat_ball_right),
        Sphere(Point3(0.0, 0.0, 2.0), 0.5, mat_ball_behind)
    ])

    cam.render(world)
