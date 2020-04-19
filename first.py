#!/usr/bin/env python3

import os
import sys
import turtle as a
import random

scr = a.Screen()
scr.bgcolor('dark blue')
print ("My name is Arjun")

def draw_rectangle(length, width, color, a):
 a.pensize(1)
 a.color(color)
 a.begin_fill() 
 for i in range(1,3):
  a.forward(length)
  a.right(90)
  a.forward(width)
  a.right(90)
 a.end_fill()

a.goto(0,200)
draw_rectangle(525,200,"gold",a)
draw_rectangle(200,525,"gold",a)
a.goto(-400,200)
draw_rectangle(525,200,"gold",a)
a.penup()
a.goto(200,400)
a.pendown()
draw_rectangle(200,525,"gold",a)
 
def draw_star(points, size, angle, color,a):
 a.color(color)
 a.begin_fill()
 for i in range (points):
     a.forward(size)
     a.right(angle);
 a.end_fill()
a.speed(0)
starsize=30
distance = starsize +15;

for y in range(1,distance*5,distance):
 y = y + 111;
 for x in range(1,distance*10, distance):
  a.penup()
  x = x - 666;
  a.goto(x,y);
  a.pendown()
  size=starsize
  points=5
  angle=180- (180 /points)
  draw_star(points, size, angle, "white", a);

 
for y in range(1,distance*5,distance):
 y = y + 111;
 for x in range(200,200+distance*10, distance):
  a.penup()
 
  a.goto(x,y);
  a.pendown()
  size=starsize
  points=5
  angle=180- (180 /points)
  draw_star(points, size, angle, "white", a);

 
for y in range(-290,-290+distance*5,distance):
 for x in range(200,200+distance*10, distance):
  a.penup()
  a.goto(x,y);
  a.pendown()
  size=starsize
  points=5
  angle=180- (180 /points)
  draw_star(points, size, angle, "white", a);
 
 
for y in range(-290,-290+distance*5,distance):
 for x in range(-666,-666+distance*10, distance):
  a.penup()
  a.goto(x,y);
  a.pendown()
  size=starsize
  points=5
  angle=180- (180 /points)
  draw_star(points, size, angle, "white", a);









 
