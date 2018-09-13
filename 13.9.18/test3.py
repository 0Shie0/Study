import turtle
turtle.shape("turtle")
turtle.hideturtle()
turtle.setpos(0,0)
turtle.showturtle()
for i in range(11):
    turtle.forward(i*20)
    turtle.left(90)
    turtle.forward(i*20)
    turtle.left(90)
    turtle.forward(i*20)
    turtle.left(90)
    turtle.forward(i*20)
    turtle.left(90)
    turtle.forward(i)
    turtle.up()
    turtle.setpos(-i*10,-i*10)
    turtle.down()

