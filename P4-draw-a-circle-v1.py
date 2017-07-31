#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    ================================================================
    Exercise Udacity course "Programming Foundations with Python"
    Lesson 3: Use classes - P3: draw turtles
    -------------------------------------------------------------

    In this exercise, we will start to use classes to draw forms
    First, we need to list the steps to draw a square:
    * repeat 4 times:
    (1) move x pixels forward
    (2) turn 90 degrees to the left

    -----------------------------------------------------------------

    Modules that we use in this program:
    - turtle: graphic module to make draws. Is very popular to teach
    programming to kids.

    Functions used in this program:
    - turtle.forward = make a draw moving forward x pixels
        syntax: turtle.forward(pixels)
    - turtle.right = make a draw moving to the right "x" degrees
        syntax: turtle.right(degrees)
    =================================================================
"""

import turtle

def draw_square(some_turtle):

    for i in range(1,5):
        some_turtle.forward(150)
        some_turtle.right(90)

def draw_art():

    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle()

    # faz o quadrado
    for h in range(1, 37):
        brad.color("white")
        brad.pensize(1)
        brad.shape("circle")
        brad.speed(30)
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

draw_art()



