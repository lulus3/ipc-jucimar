import turtle
import random

score_red = 0
score_green = 0

circle_one = turtle.clone()
circle_two = turtle

circle_one.color("red")
circle_two.color("green")

circle_one.penup()
circle_two.penup()

circle_one.left(90)
circle_two.right(90)

circle_one.forward(100)
circle_two.forward(100)

circle_one.right(90)
circle_two.left(90)

circle_one.forward(300)
circle_two.forward(300)

circle_one.pendown()
circle_two.pendown()

circle_one.right(90)
circle_two.right(90)

circle_one.circle(20)
circle_two.circle(20)

circle_one.penup()
circle_two.penup()

player_one = circle_one
player_two = circle_two

player_one.left(90)
player_two.left(90)

player_one.backward(600)
player_two.backward(600)

player_one.shape("turtle")
player_two.shape("turtle")

player_one.pendown()
player_two.pendown()

while score_red<600 and score_green<600:
    play = input("press enter to continue")
    number = random.randint(1, 6)
    distance = number * 20
    player_one.forward(distancia)
    score_red += distancia
    if score_red>=600:
        print("red wiins")
        break
    play = input("press enter to continue")
    number = random.randint(1, 6)
    distance = number * 20
    player_two.forward(distancia)
    score_green+=distancia
    if score_green >= 600:
        print("green wins")
        break

turtle.done()
