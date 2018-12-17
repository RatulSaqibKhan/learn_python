import turtle

turtle.color("red")
turtle.speed(15)

counter = 0
while counter < 37:
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.right(10)
    counter += 1

turtle.exitonclick()