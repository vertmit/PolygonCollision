PolygonCollision is a Python module designed for efficient collision detection between 2D polygons. Using the Separating Axis Theorem (SAT), this library enables precise detection of intersections between polygons, making it an essential tool for game developers, simulations, and applications requiring accurate collision detection between shapes.

Features:
Polygon Collision Detection: Determine whether two 2D polygons overlap with accurate collision detection algorithms.
Customizable Shapes: Define custom 2D shapes by specifying their vertices as Vector objects.
Efficient Algorithm: Implementing the Separating Axis Theorem (SAT) ensures fast and reliable collision detection for complex polygons.

How It Works:
The library checks for collisions by projecting the shapes onto various axes and checking if the projections overlap. If there is no axis along which the projections of the two shapes do not overlap, they are colliding.

Code Examples:
from PolygonCollision import PolygonCollision

#Create 2 squares
polygon1=PolygonCollision.Shape(vertices=[(0,0),(0,20),(20,20),(20,0)]) #x:0 y:0, size 20
polygon2=PolygonCollision.Shape(vertices=[(10,10),(10,30),(30,30),(30,10)]) #x:10 y:10, size 20

#Create circle
circle=PolygonCollision.Shape(vertices=[(30,30)],radius=10) #x:30 y:30, radius 10

if polygon1.collide(polygon2): #Check if polygon2 is touching polygon1 (True)
    print("POLYGON COLLISION!!!")
else:
    print("no polygon collision")

if polygon1.collide(circle): #Check if circle is touching polygon1 (False)
    print("CIRCLE COLLISION!!!")
else:
    print("no circle collision")

License:
This Collision Detection Library is licensed under the MIT License - see the LICENSE file for details.