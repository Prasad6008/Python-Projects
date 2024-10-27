import turtle
import winsound

def play_sound(audio):
    winsound.PlaySound(audio,winsound.SND_ASYNC)
    

win = turtle.Screen()

win.setup(800,600)
win.bgcolor('blue')
win.title("'***Ball Game***' by Prasad6008")
win.tracer(0)


block1 = turtle.Turtle()
block1.shape('square')
block1.color('white')
block1.shapesize(stretch_wid = 1.5,stretch_len = 5*12)

block1.speed(0)
block1.penup()
block1.goto(0,230)

block2 = turtle.Turtle()
block2.shape('square')
block2.color('white')
block2.shapesize(stretch_wid = 1.5,stretch_len = 5*12)

block2.speed(0)
block2.penup()
block2.goto(0,-230)



#Right paddle
left_paddle = turtle.Turtle()

left_paddle.shape('square')
left_paddle.color('white')
left_paddle.shapesize(stretch_wid = 5,stretch_len = 1)

left_paddle.speed(0)
left_paddle.penup()
left_paddle.goto(-390,0)

#Right paddle
right_paddle = turtle.Turtle()

right_paddle.shape('square')
right_paddle.color('white')
right_paddle.shapesize(stretch_wid = 5,stretch_len = 1)

right_paddle.speed(0)
right_paddle.penup()
right_paddle.goto(390,0)

#Ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx = 0.50
ball.dy = 0.50


#Paddle movements
win.listen()

def left_paddle_up():
    if left_paddle.ycor() < 150:
        left_paddle.sety(left_paddle.ycor() + 50)

win.onkeypress(left_paddle_up,'w')

def left_paddle_down():
    if left_paddle.ycor() > -150:
        left_paddle.sety(left_paddle.ycor() - 50)

win.onkeypress(left_paddle_down,'s')

def right_paddle_up():
    if right_paddle.ycor() < 150:
        right_paddle.sety(right_paddle.ycor() + 50)

win.onkeypress(right_paddle_up,'Up')

def right_paddle_down():
    if right_paddle.ycor() > -150:
        right_paddle.sety(right_paddle.ycor() - 50)

win.onkeypress(right_paddle_down,'Down')


#score Board
p1_score = 0
p2_score = 0

score = turtle.Turtle()
score.speed(0)
score.penup()
score.goto(0,250)
score.color('white')
score.write("Player 1 : 0 | Player 2 : 0",align="center",font=('Arial',30,'normal'))

score.hideturtle()


while True:
    turtle.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 200:
        ball.dy *= -1

    if ball.xcor() > 390:
        p1_score += 1
        score.clear()
        score.write("Player 1 : {} | Player 2 : {}".format(p1_score,p2_score),align="center",font=('Arial',30,'normal'))
        ball.dx *= -1

    if ball.ycor() < -200:
        ball.dy *= -1

    if ball.xcor() < -390:
        p2_score += 1
        score.clear()
        score.write("Player 1 : {} | Player 2 : {}".format(p1_score,p2_score),align="center",font=('Arial',30,'normal'))
        ball.dx *= -1

    if ball.xcor() < -370 and ball.ycor() < left_paddle.ycor() + 60 and ball.ycor() > left_paddle.ycor() - 60:
        play_sound('x')
        ball.dx *= -1

    if ball.xcor() > 370 and ball.ycor() < right_paddle.ycor() + 60 and ball.ycor() > right_paddle.ycor() - 60:
        play_sound('x')
        ball.dx *= -1

    #game Over:
    if p1_score == 5:
        game_over1 = turtle.Turtle()
        game_over1.color('red')
        game_over1.write("***Player 1 Wins***",align="center",font=('Arial',50,'normal'))
        game_over1.hideturtle()
        break
        

    if p2_score == 5:
        game_over2 = turtle.Turtle()
        game_over2.color('red')
        game_over2.write("***Player 2 Wins***",align="center",font=('Arial',30,'normal'))
        game_over2.hideturtle()
        break
        
