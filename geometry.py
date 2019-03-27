# Yash Mistri
import math


def cast_ray(p, obstacles):
    vertices = []
    for o in obstacles:
        for v in get_points(o):
            vertices.append(v)
    a = 2 * math.pi / 50
    for ray in range(50):
        print()


def intersects_line_rect(line, rect):
    points = []
    for seg in get_lines(rect):
        point = get_intersection(line[0], line[1], seg[0], seg[1])
        if point:
            points.append(point)

    return points


# returns the point where 2 lines intersect

def get_intersection(o1, e1, o2, e2):
    r = (e1[0] - o1[0], e1[1] - o1[1])
    s = (e2[0] - o2[0], e2[1] - o2[1])

    diff = [o2[0] - o1[0], o2[1] - o1[1]]

    numert = cross(diff, s)
    denomt = cross(r, s)
    numeru = cross(diff, r)
    denomu = cross(s, r)

    if numert != 0 and denomt == 0:
        return False
    try:
        t = numert / denomt
        u = numeru / denomu
    except ZeroDivisionError:
        return False

    if denomt != 0 and 0 <= t <= 1 and 0 <= -u <= 1:
        return o1[0] + t * r[0], o1[1] + t * r[1]
    return False


def cross(vec1, vec2):
    return vec1[0] * vec2[1] - vec1[1] * vec2[0]


# returns an end point that is (length) away from the original point and is rotated by (angle)
def generate_line(origin, angle, length):
    return


# extends an end point by the given length away from its current position
def extend(origin, end, length):
    angle = math.atan2((end[1] - origin[1]), (end[0], origin[0]))
    hyp = magnitude(origin, end) + length

    opp = math.sin(angle) * hyp
    adj = math.cos(angle) * hyp

    return adj, opp


def get_points(rect):
    return [rect.topleft, rect.bottomleft, rect.topright, rect.bottomright]


def get_lines(rect):
    return [[rect.topleft, rect.topright],
            [rect.topright, rect.bottomright],
            [rect.bottomright, rect.bottomleft],
            [rect.topleft, rect.bottomleft]]


def magnitude(p1, p2):
    return math.sqrt((p2[1] - p1[1]) ** 2 + (p2[0] - p2[0]) ** 2)
