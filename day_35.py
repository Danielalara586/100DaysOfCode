# Day 35: Ping Pong Game!

import turtle

player1_score = 0
player2_score = 0

# Creating the screen
window = turtle.Screen()
window.title("Ping Pong Game!")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Creating the left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Creating the right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Creating ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5, 5)
ball_in_x = 0.2
ball_in_y = 0.2

# Creating scorecard
score_card = turtle.Turtle()
score_card.speed(0)
score_card.color("light blue")
score_card.penup()
score_card.hideturtle()
score_card.goto(0, 260)
score_card.write("Score", align="center", font=("Arial", 24, "normal"))


def move_paddle(paddle, position):
    y = paddle.ycor()
    y += position
    paddle.sety(y)


# Moving the paddles
window.listen()
window.onkeypress(lambda: move_paddle(left_paddle, 90), 'w')
window.onkeypress(lambda: move_paddle(left_paddle, -90), 's')
window.onkeypress(lambda: move_paddle(right_paddle, 90), 'Up')
window.onkeypress(lambda: move_paddle(right_paddle, -90), 'Down')

while True:
    window.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball_in_x)
    ball.sety(ball.ycor() + ball_in_y)

    if ball.ycor() > 290:
        ball.sety(290)
        ball_in_y *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball_in_y *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_in_x *= -1
        player1_score += 1
        score_card.clear()
        score_card.write(f"Player 1: {player1_score} \tPlayer 2: {player2_score}", align="center",
                         font=("Arial", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_in_x *= -1
        player2_score += 1
        score_card.clear()
        score_card.write(f"Player 1: {player1_score} \tPlayer 2: {player2_score}", align="center",
                         font=("Arial", 20, "normal"))

    # Collisions
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (
            right_paddle.ycor() + 40 > ball.ycor() > right_paddle.ycor() - 40):
        ball.setx(340)
        ball_in_x *= -1

    if (ball.xcor() < -340) and (ball.xcor() < -350) and (
            left_paddle.ycor() + 40 > ball.ycor() > left_paddle.ycor() - 40):
        ball.setx(-340)
        ball_in_x *= -1
