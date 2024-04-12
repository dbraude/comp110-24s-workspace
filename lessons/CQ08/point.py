"""Class for point."""
from __future__ import annotations
__author__ = "730704898"


class Point:
    """The point class."""
    x: float
    y: float
    
    def __init__(self, x: float, y: float):
        """Initializes the point."""
        self.x = x
        self.y = y
    
    def scale_by(self, factor: int) -> None:
        """Scales the point by mutating it."""
        self.x *= factor
        self.y *= factor 

    def scale(self, factor: int) -> Point:
        """Scales the point by returning a new point."""
        this_point: Point = Point(self.x * factor, self.y * factor)
        return this_point