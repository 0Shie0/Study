import turtle
import math
turtle.shape("turtle")
x = 2
z = 4
a = 0
b = 100
while a == 0:
    x = x + 1
    turtle.up()
    if z > 1:
        z = z - 1
    if z ==3:
        turtle.sety(-(b*3**0.5)/6)
    elif z ==2:
        turtle.sety(-b/2)
    else:
        turtle.sety(-b/(2*math.tan(3.14/x))) 
    turtle.setx(b/2)
    turtle.down()
    a = 1
    while a != 0:
        a = a + 1
        turtle.left(360/x)
        turtle.forward(b)
        if a > x:
            a = 0
    turtle.left(180/x)
    if z ==3:
        turtle.circle((b*3**0.5)/z)
    elif z ==2:
        turtle.circle((b*2**0.5)/z)
    else:
        turtle.circle((b/(2*math.sin(3.14/x))))        
    turtle.right(180/x)
    turtle.up()
    turtle.setpos(0.00,0.00)
    turtle.home
    turtle.down

