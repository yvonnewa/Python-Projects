# CMPT 120
# Yvonne Wang 301388181
# Winnie Shen 301390796
# Assignment 3 - Turtle
# Oct. 30, 2019

import turtle

import random
colorlis = ["red", "blue", "green", "pink", "yellow", "purple"]

wn = turtle.Screen()
wn.bgcolor("lightblue")
bob = turtle.Turtle()
bob.color("green")
bob.shape("turtle")
bob.pensize(4)

wen = turtle.Turtle() 
wen.shape("turtle")
Col = random.choice(colorlis)
wen.color(Col)
wen.pensize(5)

Lay = turtle.Turtle()
Lay.color(random.choice(colorlis))
Lay.pensize(10)

def love():
  wen.right(90)
  wen.forward(150)
  wen.left(90)
  wen.forward(150)
  wen.up()
  wen.forward(50)
  wen.down()

  for i in range(4):
    wen.forward(150)
    wen.left(90)

  wen.up()
  wen.backward(-200)
  wen.left(90)
  wen.backward(-150)
  wen.down()

  wen.up
  wen.right(135)
  wen.forward(168)
  wen.left(90)
  wen.forward(168)
  wen.down

  wen.up()
  wen.left(315)
  wen.forward(50)
  wen.down()

  wen.forward(150)
  wen.up()
  wen.backward(150)
  wen.down()
  wen.right(90)
  wen.forward(150)
  wen.backward(75)
  wen.left(90)
  wen.forward(150)
  wen.backward(150)
  wen.right(90)
  wen.forward(75)
  wen.left(90)
  wen.forward(150)

  for size in range(3, 30, 2):
    wen.speed(5)
    wen.backward(size)
    wen.left(25)

def hexagon(size):
  Lay.penup()
  Lay.backward(500)
  Lay.pendown()
  for i in range(6):
    Lay.forward(size)
    Lay.left(60)

def shapefill(size):
  t = turtle.Turtle()
  t.penup()
  t.backward(700)
  t.pendown()
  t.fillcolor('blue')
  t.begin_fill()
  for i in range(9):
    t.forward(size)
    t.right(40)
  t.end_fill()

for i in [0, 1, 2]:      
    bob.forward(100)
    bob.left(90)

for aColor in ["red", "pink", "brown", "blue"]:
   bob.color(aColor)
   bob.forward(40)
   bob.left(90)

bob.up()  
                  
for size in range(7, 70, 2):
    bob.speed(10)    
    bob.stamp()               
    bob.forward(size)          
    bob.right(24) 

love()

hexagon(100)

shapefill(60)


  


