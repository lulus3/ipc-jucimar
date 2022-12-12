import turtle
fibonacci = [0, 1]
last_element = fibonacci[0]
current_element = fibonacci[1]
turtle_line = turtle.clone()
turtle_line.left(90)
turtle_line.circle(10, 90)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(10)
for a in range(10):
    add = last_element+current_element
    fibonacci.append(add)
    last_element = current_element
    current_element = add
    add = add * 10
    turtle.forward(add)
    turtle.left(90)
    turtle.forward(add)
    turtle.left(90)
    turtle.forward(add)
    turtle.left(90)
    turtle.forward(add)
    turtle.left(90)
    turtle.forward(add)
    turtle.left(90)
    turtle.forward(add)
    turtle_line.circle(add, 90)









