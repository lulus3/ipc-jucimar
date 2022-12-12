import turtle
turtle.left(90)

def create_branches(length, branche):
    if branche > 0:

        turtle.forward(length)
        turtle.right(24)

        create_branches(length*0.8, branche-1)

        turtle.left(24)
        turtle.left(24)

        create_branches(length*0.8, branche-1)

        turtle.right(24)
        turtle.backward(length)


create_branches(70, 6)

