# -------------------------------------------------------------
# Name: Alvin Midgette
# Assignment: P4LAB1 - Turtle Graphics (Square and Triangle House)
# Description: This program uses the turtle graphics library, 
#              incorporating both a for loop and a while loop 
#              to draw a house (a square base with a triangle roof).
# -------------------------------------------------------------

# PSEUDOCODE:
# 1. Import the turtle module.
# 2. Initialize the screen and set a background color (e.g., lightblue).
# 3. Create a turtle object, set its color, pen size, and shape.
# 4. Use a FOR loop to draw the 4 sides of the square base.
# 5. Lift the pen and reposition the turtle to the top-left corner of the square.
# 6. Put the pen down and use a WHILE loop to draw the 3 sides of the triangle roof.
# 7. Hide the turtle and keep the graphics window open until closed.

import turtle

# Set up the screen background color
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("P4LAB1 - House Drawing by Alvin Midgette")

# Create and configure the turtle object
house_turtle = turtle.Turtle()
house_turtle.color("purple")
house_turtle.pensize(4)
house_turtle.shape("turtle")
house_turtle.speed(3)

# -------------------------------------------------------------
# DRAWING THE SQUARE BASE (Using a FOR Loop)
# -------------------------------------------------------------
for _ in range(4):
    house_turtle.forward(100)
    house_turtle.right(90)

# -------------------------------------------------------------
# REPOSITIONING FOR THE TRIANGLE ROOF
# -------------------------------------------------------------
house_turtle.penup()
house_turtle.left(90)    # Face upward
house_turtle.forward(100)  # Move up to the top of the square
house_turtle.right(90)    # Face right along the top edge
house_turtle.pendown()

# -------------------------------------------------------------
# DRAWING THE TRIANGLE ROOF (Using a WHILE Loop)
# -------------------------------------------------------------
sides = 0
while sides < 3:
    house_turtle.forward(100)
    house_turtle.left(120)  # 120-degree turn for an equilateral triangle
    sides += 1

# Finish up
house_turtle.hideturtle()
turtle.done()
