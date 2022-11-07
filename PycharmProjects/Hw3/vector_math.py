import data
import math

def scale_vector(vector, scalar):
    return data.Vector((vector.x*scalar) ,(vector.y*scalar),(vector.z*scalar))

def dot_vector(vector1, vector2):
    return (vector1.x * vector2.x) + (vector1.y * vector2.y) + (vector1.z * vector2.z)

def length_vector(vector):
    return(vector.z == math.sqrt((vector.x ** 2) + (vector.y) ** 2))

def normalize_vector(vector):
    return data.Vector((vector.x * (-1)), (vector.y * (-1)), (vector.z * (-1)))

def difference_point(point1,point2):
    return data.Vector((point1.x - point2.x),(point1.y - point2.y), (point1.z - point2.z))

def difference_vector(vector1,vector2):
    x = vector1.x - vector2.x
    y = vector1.y - vector2.y
    z = vector1.z - vector2.z
    return data.Vector(x,y,z)

def translate_point(point,vector):
    return data.Point((point.x + vector.x),(point.y + vector.y), (point.z + vector.z))

def vector_from_to(from_point, to_point):
    return difference_point(to_point, from_point)
