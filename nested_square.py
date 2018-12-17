import turtle

turtle.shape("turtle")
turtle.speed(1)

for sideLength in range(50,100,10):
    for i in range(4):
        turtle.forward(sideLength)
        turtle.left(90)
turtle.exitonclick()

