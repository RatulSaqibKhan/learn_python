def draw_triangle(x):
    import turtle

    turtle.speed(2)

    for i in range(3):
        turtle.forward(x)
        turtle.left(120)
    turtle.exitonclick()

x = input("Write an Integer and press enter ")
y = int(x)
draw_triangle(y)