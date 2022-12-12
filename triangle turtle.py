import turtle
turtle.speed("normal")

def draw_triangle(location_x, location_y):
    turtle.penup()
    turtle.goto(location_x, location_y)
    turtle.pendown()

    turtle.right(60)
    turtle.forward(130)
    turtle.left(60)
    turtle.backward(130)
    turtle.left(60)
    turtle.forward(130)

    turtle.penup()
    turtle.home()
    turtle.pendown()

turtle.onscreenclick(draw_triangle, 1)

turtle.done()


