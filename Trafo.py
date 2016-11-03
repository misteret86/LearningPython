""" Am übergebenen Startpunkt wird ein Trafo gezeichnet """

import tkinter
import turtle

def ZeichneTrafo(radius, startx, starty):
  turtle.penup()
  turtle.goto(startx, starty)
  turtle.pendown()
  turtle.circle(radius)
  mittelpunktKreis = (startx, starty+radius)
  turtle.penup()
  startKreis2 = (mittelpunktKreis[0], mittelpunktKreis[1]-2*radius)
  turtle.goto(startKreis2)
  turtle.pendown()
  turtle.circle(2*radius)
  turtle.penup()
  startKreis3 = (mittelpunktKreis[0], mittelpunktKreis[1]-3*radius)
  turtle.goto(startKreis3)
  turtle.pendown()
  turtle.circle(3*radius)
  
  ts = turtle.getscreen()
  ts.getcanvas().postscript(file="duck.jpg")
  return 0
  
  


