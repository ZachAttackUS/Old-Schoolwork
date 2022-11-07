import point

def are_positive(list):
    list1 = [i for i in list if i > 0]
    return list1

def are_greater_than(list, n):
    list1 = []
    for i in list:
        if n < i:
            list1.append(i)
    return list1

def are_in_first_quadrant(list):
    list1 = []
    for point.Point in list:
        if point.Point.x > 0 and point.Point.y > 0:
            list1.append(point.Point)
    return list1