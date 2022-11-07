import math
import point

def square_all(list):
    list1 = [i**2 for i in list]
    return list1

def add_n_all(list,n):
    list1 = []
    for i in range(len(list)):
        list1.append(list[i] + n)
    return list1

def distance_all(list): # Still need to work on it
    list1 = []
    for i in list:
        list1.append(math.sqrt(i.x**2 + i.y**2))
    return list1








