def poly_add2(list1,list2):
    return(list1[0] + list2[0], list1[1] + list2[1], list1[2] + list2[2])

def poly_multi2(l1, l2):
    x4 = l1[2] * l2[2]
    x3 = (l1[2] * l2[1]) + (l1[1] * l2[2])
    x2 = (l1[2] * l2[0]) + (l1[1] * l2[1]) + (l1[0] * l2[2])
    x1 = (l1[1] * l2[0]) + (l1[0] * l2[1])
    base = (l1[0] * l2[0])

    return (base,x1,x2,x3,x4)
