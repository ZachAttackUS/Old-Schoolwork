import math


def sum_of_values(list):
    return sum(list)

def index_of_smallest(list):
    final = -1
    smallest = math.inf
    if len(list) > 0:
        for i in range(len(list)):
            if list[i] <= smallest:
                smallest = list[i]
                final = i
    return final

def nearest_origin(list):
    final = -1
    closest = math.inf
    if len(list) > 0:
        for t in range(len(list)):
            distance = math.sqrt((list[t].x**2 + list[t].y**2))
            if distance <= closest:
                closest = distance
                final = t
    return final














