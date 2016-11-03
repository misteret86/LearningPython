import math
import turtle
import fibonacci
import Trafo





def main():

    
    print("hello world")


    a = 9
    b = 10
    c = 1

    print (a * b * c)


    staedte = ["Mainz", "Frankfurt", "Wiesbaden", "Darmstadt"]
    for stadt in staedte:
      print(stadt)
      
      
    print (math.sin(math.pi/2))
    print (math.cos(0))
    
    print(turtle.position())
    #turtle.circle(5)
    
    print (fibonacci.fib(10))
    
    Trafo.ZeichneTrafo(50,5,5)
    
    #turtle.circle(8)

main()
  
