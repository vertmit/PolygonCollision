from vector import Vector, dot_product

def project_polygon(axis, polygon):
    dots = [dot_product(Vector(p.x, p.y), axis) for p in polygon]
    return min(dots), max(dots)

def get_axes(polygon):
    edges = [Vector(polygon[i].x - polygon[i - 1].x, polygon[i].y - polygon[i - 1].y) 
             for i in range(len(polygon))]
    normals = [Vector(-edge.y, edge.x) for edge in edges]
    return normals

def collision(polygon1, polygon2):
    axes = get_axes(polygon1) + get_axes(polygon2)

    for axis in axes:
        min_p1, max_p1 = project_polygon(axis, polygon1)
        min_p2, max_p2 = project_polygon(axis, polygon2)

        if max_p1 < min_p2 or max_p2 < min_p1:
            return False

    return True
