import math


def f(x):
    y = 7 * x ** 2 + 2 * x
    print(y)
    return y


def g(x, y):
    z = x ** 2 + y ** 2
    print(z)
    return z


def hypotenuse(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    print(c)
    return c


def is_positive(x):
    return(x >= 0)


