"""Point usage test."""
__author__ = "730704898"
from point import Point

test_point: Point = Point(5, 4)
test_point.scale_by(5)
print(test_point.x, test_point.y)
print(test_point.scale(5).x, test_point.scale(5).y)