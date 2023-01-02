"""
    T: O(nlogn)
    S: O(n)
    поиск полигона, содержащего все точки. 2D.
    Точки уникальны.
"""

def cross(o, a, b):
    """
        2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
        Returns a positive value, if OAB makes a counter-clockwise turn,
        negative for clockwise turn, and zero if the points are collinear.
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def monotonic_chain(points: list[list[float]]) -> list[list[float]]:
    points.sort()

    u, l = [], []
    for p in points:
        if len(l) > 1 and cross(l[-2], l[-1], p) <= 0:
            # нужны только точки, делающие поворот по часовой стрелке
            l.pop()
        l.append(p)

    for p in reversed(points):
        if len(u) > 1 and cross(u[-2], u[-1], p) <= 0:
            u.pop()
        u.append(p)

    # первая и последняя точки - одно и то же
    return l[:-1] + u[:-1]
