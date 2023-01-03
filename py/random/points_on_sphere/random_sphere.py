"""
    uniform distribution
    http://mathworld.wolfram.com/SpherePointPicking.html
"""

import math
import random


def get_onsphere_point(r: float):
    theta = random.uniform(0, math.pi*2)
    u = random.uniform(-1., 1.)
    a = math.sqrt(1. - u*u)

    point = (
        r * math.cos(theta) * a,
        r * math.sin(theta) * a,
        r * u
    )

    return point


def get_sphere_points_population(n: int, radius: float):
    for _ in range(n):
        yield get_onsphere_point(radius)
