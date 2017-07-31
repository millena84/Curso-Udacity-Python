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

def draw_square():

    i = 1
    j = 1

    window = turtle.Screen()
    window.bgcolor("black")
    brad = turtle.Turtle()

# primeira parte: fazer um quadrado usando o turtle, de forma personalizada:

    while i <= 4:
        brad.color("violet")
        brad.pensize(1)
        brad.shape("triangle")
        brad.speed(2)
        brad.forward(100)
        brad.right(90)
        i = i + 1

# segunda parte: usar o turtle instanciando uma nova classe e fazendo um circulo

    angie = turtle.Turtle()
    angie.color("white")
    angie.pensize(1)
    angie.shape("arrow")
    angie.speed(2)
    angie.circle(30)

# terceira parte: usar o turtle instanciando uma nova classe e fazendo um triangulo

    mark = turtle.Turtle()
    mark.color("yellow")
    mark.pensize(1)
    mark.shape("arrow")
    mark.speed(2)

    while j <= 3:
        mark.forward(50)
        mark.left(120)
        j = j + 1

    window.exitonclick()


draw_square()
