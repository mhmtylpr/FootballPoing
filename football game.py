import time
import turtle
import winsound

scrn = turtle.Screen()
scrn.title("pinpon")
scrn.setup(width=800,height=600)
scrn.bgcolor("#66ff00")
scrn.tracer(0)

center_bla = turtle.Turtle()
center_bla.color("white")
center_bla.shape("circle")
center_bla.shapesize(0.8)
center_bla.goto(0,0)

center_line = turtle.Turtle()
center_line.color("white")
center_line.shape("square")
center_line.shapesize(60,0.1)
center_line.goto(0,0)

center_circle = turtle.Turtle()
center_circle.goto(0,-150)
center_circle.hideturtle()
center_circle.color("white")
center_circle.pensize(2)
center_circle.circle(150)

field_line_up = turtle.Turtle()
field_line_up.penup()
field_line_up.goto(-380,280)
field_line_up.down()
field_line_up.color("white")
field_line_up.pensize(2)
field_line_up.forward(760)
field_line_up.hideturtle()

field_line_down = turtle.Turtle()
field_line_down.penup()
field_line_down.goto(-380,-280)
field_line_down.down()
field_line_down.color("white")
field_line_down.pensize(2)
field_line_down.forward(760)
field_line_down.hideturtle()

field_line_right = turtle.Turtle()
field_line_right.penup()
field_line_right.goto(-380,280)
field_line_right.down()
field_line_right.left(270)
field_line_right.color("white")
field_line_right.pensize(2)
field_line_right.forward(560)
field_line_right.hideturtle()

field_line_left = turtle.Turtle()
field_line_left.penup()
field_line_left.goto(380,280)
field_line_left.down()
field_line_left.left(270)
field_line_left.color("white")
field_line_left.pensize(2)
field_line_left.forward(560)
field_line_left.hideturtle()

score_bg_one = turtle.Turtle()
score_bg_one.hideturtle()
score_bg_one.color("blue")
score_bg_one.penup()
score_bg_one.goto(-300,280)
score_bg_one.down()
score_bg_one.fillcolor("blue")
score_bg_one.begin_fill()
score_bg_one.forward(290)
score_bg_one.left(270)
score_bg_one.forward(50)
score_bg_one.left(270)
score_bg_one.forward(290)
score_bg_one.left(270)
score_bg_one.forward(50)
score_bg_one.end_fill()

score_bg_two = turtle.Turtle()
score_bg_two.hideturtle()
score_bg_two.color("red")
score_bg_two.penup()
score_bg_two.goto(10,280)
score_bg_two.down()
score_bg_two.fillcolor("red")
score_bg_two.begin_fill()
score_bg_two.forward(290)
score_bg_two.left(270)
score_bg_two.forward(50)
score_bg_two.left(270)
score_bg_two.forward(290)
score_bg_two.left(270)
score_bg_two.forward(50)
score_bg_two.end_fill()

POINT_RED = 0
POINT_BLUE = 0
FONT = ("Verdana" , 17, "bold")

racket_one = turtle.Turtle()
racket_one.shape("square")
racket_one.color("red")
racket_one.penup()
racket_one.shapesize(5,1)
racket_one.speed(0)
racket_one.goto(x=-350,y=0)

racket_two = turtle.Turtle()
racket_two.shape("square")
racket_two.color("blue")
racket_two.penup()
racket_two.shapesize(5,1)
racket_two.speed(0)
racket_two.goto(x=350, y=0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.shapesize(1)
ball.speed(0)
ball.goto(x=0, y=0)

ball_x = 0.5
ball_y = 0.5

def one_up():
    y = racket_one.ycor()
    y += 23
    racket_one.sety(y)
    if racket_one.ycor() > 255:
        racket_one.sety(255)

def one_down():
    y = racket_one.ycor()
    y -= 23
    racket_one.sety(y)
    if racket_one.ycor() < -255:
        racket_one.sety(-255)

def two_up():
    y = racket_two.ycor()
    y += 23
    racket_two.sety(y)
    if racket_two.ycor() > 255:
        racket_two.sety(255)

def two_down():
    y = racket_two.ycor()
    y -= 23
    racket_two.sety(y)
    if racket_two.ycor() < -255:
        racket_two.sety(-255)

scrn.listen()
scrn.onkeypress(one_up,"w")
scrn.onkeypress(one_down,"s")
scrn.onkeypress(one_up,"W")
scrn.onkeypress(one_down,"S")
scrn.onkeypress(two_up,"Up")
scrn.onkeypress(two_down,"Down")

score_one = turtle.Turtle()
score_one.penup()
score_one.goto(-150,240)
score_one.color("red")
score_one.hideturtle()
score_one.speed(0)
score_one.write(arg="Red Player Score : {} ".format(POINT_RED),align="center" , font=FONT)

score_two = turtle.Turtle()
score_two.penup()
score_two.goto(160,240)
score_two.color("blue")
score_two.hideturtle()
score_two.speed(0)
score_two.write(arg="Blue Player Score : {} ".format(POINT_BLUE),align="center" , font=FONT)

red_win = turtle.Turtle()
red_win.color("red")
red_win.goto(0,0)
red_win.penup()
red_win.hideturtle()

blue_win = turtle.Turtle()
blue_win.color("blue")
blue_win.goto(0,0)
blue_win.penup()
blue_win.hideturtle()

while True:
    x = ball.xcor()
    x += ball_x
    ball.setx(x)

    y = ball.ycor()
    y += ball_y
    ball.sety(y)

    if (ball.xcor() > 340 and ball.xcor() < 350)  :
        if (ball.ycor()< racket_two.ycor() + 60 and ball.ycor() > racket_two.ycor() - 60) :
            winsound.PlaySound("boing.wav" , winsound.SND_ASYNC)
            ball.setx(340)
            ball_x = ball_x*-1

    if (ball.xcor() < -340 and ball.xcor() > -350)   :
        if (ball.ycor()< racket_one.ycor() + 60 and ball.ycor() > racket_one.ycor() - 60):
            winsound.PlaySound("boing.wav", winsound.SND_ASYNC)
            ball.setx(-340)
            ball_x = ball_x*-1

    if ball.ycor() > 290 or ball.ycor()<-290:
        ball_y = ball_y*-1

    if ball.xcor() <-355:
        winsound.PlaySound("goal.wav", winsound.SND_ASYNC)
        ball_x = ball_x*-1
        ball_y = ball_y * -1
        ball.goto(0,0)
        POINT_BLUE += 1
        score_two.clear()
        score_two.write(arg="Blue Player Score : {} ".format(POINT_BLUE), align="center", font=FONT)

    if ball.xcor() > 355:
        winsound.PlaySound("goal.wav", winsound.SND_ASYNC)
        ball_x = ball_x*-1
        ball_y = ball_y * -1
        ball.goto(0, 0)
        POINT_RED += 1
        score_one.clear()
        score_one.write(arg="Red Player Score : {} ".format(POINT_RED), align="center", font=FONT)

    if POINT_RED == 10:
        red_win.write(arg="Red Team Won !!!", align="center" ,font=FONT)
        ball_x = 0
        ball_y = 0
        for i in range(3):
            time.sleep(1)
            if i == 2 :
                POINT_RED = 0
                POINT_BLUE = 0
                ball_x = 0.24
                ball_y = 0.24
                red_win.clear()

    if POINT_BLUE == 10:
        blue_win.write(arg="Blue Team Won !!!", align="center" ,font=FONT)
        ball_x = 0
        ball_y = 0
        for i in range(3):
            time.sleep(1)
            if i == 2:
                POINT_RED = 0
                POINT_BLUE = 0
                ball_x = 0.24
                ball_y = 0.24
                blue_win.clear()

    scrn.update()

