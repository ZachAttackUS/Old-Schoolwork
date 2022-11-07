import math
import objects

def f(x):
    y = 7 * x ** 2 + 2 * x
    print(y)
    return y


def g(x, y):
    z = x ** 2 + y ** 2
    print(z)
    return z


def hypotenuse(Point1, Point2):
    c = math.sqrt((Point2.x - Point1.x) ** 2 + (Point2.y - Point1.y) ** 2)
    print(c)
    return c


def is_positive(x):
    return(x >= 0)

def distance(Point1, Point2):
    return (hypotenuse(Point1,Point2))

def circle_overlap(circle1, circle2):
    d = distance(circle1.center, circle2.center)
    radius_total = circle1.r + circle2.r
    return d<radius_total
