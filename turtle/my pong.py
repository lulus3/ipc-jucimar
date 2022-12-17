import turtle

# draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=900, height=600)
screen.tracer(0)


# draw object
def draw_object(element, x, y):
    element.speed(0)
    element.shape("square")
    element.color("white")
    element.penup()
    element.goto(x, y)


# draw paddle 1
paddle_1 = turtle.Turtle()
draw_object(paddle_1, -440, 0)
paddle_1.shapesize(stretch_wid=5, stretch_len=1)


# draw paddle 2
paddle_2 = turtle.Turtle()
draw_object(paddle_2, 440, 0)
paddle_2.shapesize(stretch_wid=5, stretch_len=1)


# draw ball
ball = turtle.Turtle()
draw_object(ball, 0, 0)
ball.dx = 0.2
ball.dy = 0.2

# score
score_1 = 0
score_2 = 0


def score_point():
    hud.clear()
    hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
    ball.goto(0, 0)
    ball.dx *= -1


# head-up display
hud = turtle.Turtle()
draw_object(hud, 0, 260)
hud.hideturtle()
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))


def paddle_up(paddle):
    y = paddle.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    return paddle.sety(y)


def paddle_down(paddle):
    y = paddle.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    return paddle.sety(y)


# keyboard
screen.listen()
screen.onkeypress(lambda: paddle_up(paddle_1), "w")
screen.onkeypress(lambda: paddle_down(paddle_1), "s")
screen.onkeypress(lambda: paddle_up(paddle_2), "Up")
screen.onkeypress(lambda: paddle_down(paddle_2), "Down")

while True:
    screen.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # collision with the upper wall
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # collision with lower wall
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # collision with left wall
    if ball.xcor() < -440:
        score_2 += 1
        score_point()

    # collision with right wall
    if ball.xcor() > 440:
        score_1 += 1
        score_point()

    # collision with the paddle 1
    if ball.xcor() < -430 and paddle_1.ycor() + 55 > ball.ycor() > paddle_1.ycor() - 55:
        if ball.xcor() <= -435:
            ball.goto(0, 0)
        ball.dx *= -1

    # collision with the paddle 2
    if ball.xcor() > 430 and paddle_2.ycor() + 55 > ball.ycor() > paddle_2.ycor() - 55:
        if ball.xcor() >= 435:
            ball.goto(0, 0)
        ball.dx *= -1
