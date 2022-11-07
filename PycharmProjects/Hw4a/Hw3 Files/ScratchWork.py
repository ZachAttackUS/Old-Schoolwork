import math

import collisions
import data
import vector_math


def distance(point1, point2):
    return math.sqrt(((point2.x - point1.x) ** 2) + ((point2.y - point1.y) ** 2) + ((point2.z - point1.z) ** 2))


def color_finish(color, finish):
    return data.Color((color.r * finish), (color.g * finish), (color.b * finish))


def cast_ray(ray, sphere_list, color, light):
    color1 = color
    if collisions.find_intersection_points(sphere_list, ray):
        a = collisions.find_intersection_points(sphere_list, ray)
        closest = math.inf
        for t in a:
            b = distance(t[1], ray.pt)
            if b < closest:
                closest = b
                N = data.Vector(t[1].x, t[1].y, t[1].z)
                N = vector_math.scale_vector(N, .99)
                pe = vector_math.translate_point(t[1], N)
                Ldir = vector_math.normalize_vector(vector_math.vector_from_to(pe, light.point))
                dot_prod = vector_math.dot_vector(N, Ldir)
                if dot_prod > 0:
                    ray3 = data.Ray(pe, vector_math.vector_from_to(pe, light.point))
                    g = collisions.find_intersection_points(sphere_list, ray3)
                    if g is not None:
                        for f in g:
                            if distance(f[0], pe) < distance(pe, light.point):
                                color1 = color_finish(t[0].color, t[0].finish.ambient * t[0].finish.diffuse)
                            else:
                                final_finish = dot_prod * t[0].finish.diffuse
                                final_color = color_prod(t[0].color, light.color)
                                color1 = color.finish(final_color, final_finish)
                    else:
                        final_finish = dot_prod * t[0].finish.diffuse
                        final_color = color_prod(t[0].color, light.color)
                        color1 = color_finish(final_color, final_finish)
                else:
                    color1 = color_finish(t[0].color, t[0].finish.ambient * t[0].finish.diffuse)
    return color1


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light):
    image = open("image.ppm", "w")
    image.write('P3\n')
    image.write(f'{width} {height}\n')
    image.write('255\n')

    step_x = (max_x - min_x) / width
    step_y = (max_y - min_y) / height

    for j in range(height):
        for i in range(width):
            x = min_x + i * step_x
            y = max_y - j * step_y
            pt = data.Point(x, y, 0)
            ray = data.Ray(eye_point, vector_math.vector_from_to(eye_point, pt))
            color = cast_ray(ray, sphere_list, color, light)
            image.write(f'{int(color.r * 255)} {int(color.g * 255)} {int(color.b * 255)}\n')

    image.close()

class Light:
    def __init__(self, point, color):
        self.point = point
        self.color = color

    def __eq__(self, other):
        return utility.epsilon_equal(self.point, other.point) and utility.epsilon_equal(self.color, other.color)


self.diffuse = diffuse

data.Light(data.Point(-100, 100, -100), data.Color(1.5,1.5,1.5))