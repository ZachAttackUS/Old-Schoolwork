import math
import collisions
import data
import vector_math


def distance(point1, point2):
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2 + (point2.z - point1.z) **2)

def color_finish(color, finish):
    return data.Color((color.r * finish),(color.g * finish), (color.b * finish))

def color_product(color1, color2):
    return data.Color((color1.r * color2.r),(color1.g * color2.g), (color1.b * color2.b))

def color_add(color1, diffuse):
    return data.Color((color1.r + diffuse.r), (color1.g + diffuse.g), (color1.b + diffuse.b))

def cast_ray(ray, sphere_list, color, light):
    color_final = color
    intersectionpt = 0
    mainsphere = 0
    if collisions.find_intersection_points(sphere_list, ray):
        fip = collisions.find_intersection_points(sphere_list,ray)
        closest = math.inf
        for t in fip:
            b = distance(t[1], ray.pt)
            if b < closest:
                closest = b
                intersectionpt = t[1]
                mainsphere = t[0]

        #N = vector_math.vector_from_to(mainsphere.center, intersectionpt)
        N = collisions.sphere_normal_at_point(mainsphere, intersectionpt)
        N1 = vector_math.scale_vector(N, 0.01)
        pe = vector_math.translate_point(intersectionpt,N1)
        Ldir = vector_math.normalize_vector(vector_math.vector_from_to(pe, light.point))
        dotproduct = vector_math.dot_vector(N, Ldir)
        if dotproduct > 0:
            ray_pe_lightpoint = data.Ray(pe, vector_math.vector_from_to(pe,light.point))
            checkintersection = collisions.find_intersection_points(sphere_list, ray_pe_lightpoint)
            if checkintersection:
                smallest_length = distance(pe, light.point)
                for i in checkintersection:
                    length = distance(pe, i[1])
                    if length < smallest_length:
                        color_final = color_finish(mainsphere.color, mainsphere.finish.ambient)
            else:
                final_finish = dotproduct * mainsphere.finish.diffuse
                final_color = color_product(mainsphere.color, light.color)
                diffuse = color_finish(final_color,final_finish)
                color2 = color_finish(mainsphere.color, mainsphere.finish.ambient)
                color_final = color_add(color2, diffuse)
        else:
            color_final = color_finish(mainsphere.color, mainsphere.finish.ambient)

    if color_final.r > 1:
        r = 1
    else:
        r = color_final.r

    if color_final.g > 1:
        g = 1
    else:
        g = color_final.g

    if color_final.b > 1:
        b = 1
    else:
        b = color_final
    return color_final



def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light):
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
            Color = cast_ray(ray, sphere_list, color, light)



            image.write(f'{int(Color.r * 255)} {int(Color.g * 255)} {int(Color.b * 255)}\n')

    image.close()


