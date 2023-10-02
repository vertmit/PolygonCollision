class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y
    def subtract(self, other):
        return Vector(self.x - other.x, self.y - other.y)
class Shape:
    def __init__(self, vertices=None, radius=None):
        self.vertices = [Vector(x, y) for x, y in vertices] if vertices else []
        self.radius = radius
    def _check_circle_edge_collision(self, circle_center, circle_radius, edge_start, edge_end):
        closest_point_on_edge = self._closest_point_on_edge(circle_center, edge_start, edge_end)
        distance_squared = circle_center.subtract(closest_point_on_edge).dot_product(circle_center.subtract(closest_point_on_edge))
        return distance_squared <= circle_radius ** 2
    def _closest_point_on_edge(self, point, edge_start, edge_end):
        edge = edge_end.subtract(edge_start)
        point_to_edge_start = point.subtract(edge_start)
        t = point_to_edge_start.dot_product(edge) / edge.dot_product(edge)
        if t < 0:
            return edge_start
        elif t > 1:
            return edge_end
        else:
            return Vector(edge_start.x + t * edge.x, edge_start.y + t * edge.y)
    def collide(self, other_shape):
        if self.radius is not None and other_shape.radius is not None:
            distance_squared = self.vertices[0].subtract(other_shape.vertices[0]).dot_product(self.vertices[0].subtract(other_shape.vertices[0]))
            sum_radii = self.radius + other_shape.radius
            return distance_squared <= sum_radii ** 2
        if self.radius is None and other_shape.radius is None:
            for i in range(len(self.vertices) - 1):
                for j in range(len(other_shape.vertices) - 1):
                    if self._check_edge_collision(self.vertices[i], self.vertices[i + 1], other_shape.vertices[j], other_shape.vertices[j + 1]):
                        return True
            return False
        if self.radius is not None:
            circle = self
            polygon = other_shape
        else:
            circle = other_shape
            polygon = self

        for i in range(len(polygon.vertices) - 1):
            if self._check_circle_edge_collision(circle.vertices[0], circle.radius, polygon.vertices[i], polygon.vertices[i + 1]):
                return True
        return False
    def _check_edge_collision(self, edge1_start, edge1_end, edge2_start, edge2_end):
            def projection(axis, points):
                min_proj = float('inf')
                max_proj = float('-inf')
                for point in points:
                    dot_product = point.dot_product(axis)
                    min_proj = min(min_proj, dot_product)
                    max_proj = max(max_proj, dot_product)
                return min_proj, max_proj
            def overlap(axis, points1, points2):
                min_proj1, max_proj1 = projection(axis, points1)
                min_proj2, max_proj2 = projection(axis, points2)
                return max_proj1 >= min_proj2 and max_proj2 >= min_proj1
            edge1_points = [edge1_start, edge1_end]
            edge2_points = [edge2_start, edge2_end]
            axes = [Vector(edge1_points[1].y - edge1_points[0].y, edge1_points[0].x - edge1_points[1].x),
                    Vector(edge2_points[1].y - edge2_points[0].y, edge2_points[0].x - edge2_points[1].x)]
            for axis in axes:
                if not overlap(axis, edge1_points, edge2_points):
                    return False

            return True