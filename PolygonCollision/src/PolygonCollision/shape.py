from vector import Vector
from polygon_collision import get_axes, project_polygon

class Shape:
    def __init__(self, vertices):
        try:
            self.vertices = [Vector(x, y) for x, y in vertices]
        except TypeError:
            raise TypeError

    def collide(self, other_shape):
        axes = get_axes(self.vertices) + get_axes(other_shape.vertices)

        for axis in axes:
            min_p1, max_p1 = project_polygon(axis, self.vertices)
            min_p2, max_p2 = project_polygon(axis, other_shape.vertices)

            if max_p1 < min_p2 or max_p2 < min_p1:
                return False

        return True
