"""An eclipse scene drawn with a python turtle with randomly generated trees."""
__author__ = "730704898"

from turtle import Turtle, setup, done, tracer, update
from math import pi
from random import randint
turters: Turtle = Turtle()

MAX_SPEED: int = 0


def main() -> None:
    """The main function."""
    tracer(0, 0)
    setup(500, 500, 0, 0)
    turters.speed(MAX_SPEED)
    turters.hideturtle()
    turters.screen.colormode(1)
    turters.penup() 
    turters.goto(-250, 250)
    turters.pendown()
    draw_gradient(500, 30, 10, (0.01176470588, 0.01960784313, 0.14901960784))
    draw_gradient(500, 20, 10, (0.02734375, 0.21875, 0.078125))

    spawn_random_trees()
    turters.setheading(0)
    turters.penup() 
    turters.goto(-30, 125)
    spawn_sun()
    update()
    done() 


def draw_gradient(width: int, block_height: int, degrees: int, base_color: tuple[float]) -> None:
    """Draws a gradient background based on a certain color from light to dark over a certain distance."""
    turters.color(base_color)
    turters.setheading(0)
    turters.fillcolor(base_color)
    turters.begin_fill()

    if degrees == 0:
        return
    
    for x in range(2):
        turters.forward(width)
        turters.right(90)
        turters.forward(block_height)
        turters.right(90)
    turters.goto(turters.pos() - (0, block_height))

    turters.end_fill()

    new_color: tuple[float] = (base_color[0] + 0.025, base_color[1] + 0.025, base_color[2] + 0.025)

    draw_gradient(width, block_height, degrees - 1, new_color)


def draw_tree(width: float, max_height: int, angle: int, branches_per_branch: int) -> None:
    """Draws a tree using branching recursion."""
    turters.pensize(width)
    turters.setheading(angle)
    if max_height == 0: 
        return
    turters.forward(30 * max_height**0.5)
    current_position: tuple = turters.pos()

    for x in range(branches_per_branch):
        turters.left(randint(-90, 90))
        draw_tree(width, max_height - 1, angle + randint(-90, 90), branches_per_branch)
        turters.goto(current_position)


def draw_sun(radius: int, resolution: int, original_pos: tuple[int]) -> None:
    """Draws the sun, eclipsed."""
    if resolution == 0:
        turters.setheading(0)
        turters.penup()
        turters.goto(original_pos + (radius * 0.75, -radius * 0.3))
        turters.pendown
        turters.color("black")
        turters.begin_fill()
        turters.circle(radius - 3)
        turters.end_fill()
        return
    turters.color("white")

    turters.begin_fill()
    for x in range(4):
        turters.forward(2 * pi * radius * 0.25)
        turters.left(90 + resolution)
    turters.end_fill()
    draw_sun(radius, resolution - 1, original_pos)


def spawn_random_trees() -> None:
    """Spawns a semi-random array of trees in the bottom half of the screen."""
    turters.color("black")
    j: int = randint(5, 10)
    for x in range(0, j):
        tree_position: tuple[int] = (randint(-200, 200), randint(-220, -50))
        turters.penup()
        turters.goto(tree_position)
        turters.pendown()
        draw_tree(3, 3, 90, 3)


def spawn_sun():
    """Sloppy solution to make sure that the moon is drawn in the middle of the sun."""
    current_pos: tuple[int] = turters.pos()
    draw_sun(50, 10, current_pos)


if __name__ == "__main__":
    main()