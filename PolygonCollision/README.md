Collision Detection Library
This Python library provides a simple and efficient way to detect collisions between 2D polygons. It utilizes the Separating Axis Theorem (SAT) for collision detection. The library defines two main classes: Vector and Shape.

Classes
Vector
A class representing a 2D vector with x and y components.

Methods:
__init__(self, x, y): Initializes a Vector object with the given x and y components.
Shape
A class representing a 2D polygon.

Methods:
__init__(self, vertices): Initializes a Shape object with a list of Vector objects representing its vertices.
collide(self, other_shape): Checks if the current Shape collides with another Shape object. Returns True if there is a collision, otherwise False.
Usage
python
Copy code
# Example usage of the Collision Detection Library

from collision_detection import Shape, Vector

# Create shapes
shape1 = Shape([Vector(0, 0), Vector(50, 0), Vector(50, 50), Vector(0, 50)])
shape2 = Shape([Vector(25, 25), Vector(30, 25), Vector(30, 30), Vector(25, 30)])

# Check for collision
if shape1.collide(shape2):
    print("Shapes collide!")
else:
    print("No collision detected.")
How It Works
The library checks for collisions by projecting the shapes onto various axes and checking if the projections overlap. If there is no axis along which the projections of the two shapes do not overlap, they are colliding.

Contributing
Feel free to contribute by opening issues or pull requests. Bug reports, suggestions, and improvements are welcome!

License
This Collision Detection Library is licensed under the MIT License - see the LICENSE file for details.