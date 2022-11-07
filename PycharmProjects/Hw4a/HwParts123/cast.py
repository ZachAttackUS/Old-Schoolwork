import math

import collisions
import data
import vector_math


def distance(point1, point2):
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) **2 + (point2.z - point1.z) **2)

def color_finish(color, finish):
    return data.Color((color.r * finish),(color.g * finish), (color.b * finish))


def cast_ray(ray, sphere_list):
    c = data.Color(1.0,1.0,1.0)
    if collisions.find_intersection_points(sphere_list, ray):
        fip = collisions.find_intersection_points(sphere_list,ray)
        closest = math.inf
        for t in fip:
            b = distance(t[1], ray.pt)
            if b < closest:
                closest = b
                c = color_finish(t[0].color, t[0].finish.ambient)
    return c



def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color):
    image = open("../image.ppm", "w")
    image.write('P3\n')
    image.write(f'{width} {height}\n')
    image.write('255\n')
    #print('P3')
    #print(width,height)
    #print('255')

    step_x = (max_x - min_x) / width
    step_y = (max_y - min_y) / height

    for j in range(height):
        for i in range(width):
            x = min_x + i * step_x
            y = max_y - j * step_y
            pt = data.Point(x,y,0)
            ray = data.Ray(eye_point, vector_math.vector_from_to(eye_point, pt))
            color = cast_ray(ray, sphere_list, color)
            #print(int(color.r * 255), int(color.g * 255), int(color.b * 255))

            image.write(f'{int(color.r * 255)} {int(color.g * 255)} {int(color.b * 255)}\n')

    image.close()


