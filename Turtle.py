import turtle
import random

score=0
s=turtle.Screen()
s.setup(600,600)
s.bgcolor('snow2')
s.title('Game')


#Wall
wall=turtle.Turtle()
wall.up()
wall.goto(-250,250)
wall.down()
wall.width(4)
wall.color('SlateGray')

for i in range (4):
    wall.forward(500)
    wall.right(90)
    
wall.ht()

#Game Characters
tuttlle=turtle.Turtle()
tuttlle.shape('turtle')
tuttlle.shapesize(1.5)
tuttlle.color('RoyalBlue3')
tuttlle.up()
ball=turtle.Turtle()
ball.shape('circle')
ball.shapesize(0.75)
ball.color('SlateBlue')
ball.up()
ball.goto(random.randint(-250,250),random.randint(-250,250))

#Motion_Functions
def move_right():
    tuttlle.right(30)

def move_left():
    tuttlle.left(30)

def move_up():
    tuttlle.right(180)

def move_down():
    tuttlle.left(180)
    
s.listen()
s.onkey(move_right,'Right')
s.onkey(move_left,'Left')
s.onkey(move_up,'Up')
s.onkey(move_down,'Down')

#Print_Score
wr=turtle.Turtle()
wr.up()
wr.goto(-265,265)
wr.ht()
wr.color('black')
wr.write('Your Score: '+str(score),font=15)

#Move
while True:
    tuttlle.fd(1)
    if tuttlle.xcor()>250 or tuttlle.xcor()<-250 or tuttlle.ycor()>250 or tuttlle.ycor()<-250:
        tuttlle.right(180)
        score=score-5
        wr.clear()
        wr.write('yur scoure'+str(score),font=2)
        if score<0:
           wr.goto(-20,0)
           wr.write('Lose',font=50)
           break
    if tuttlle.distance(ball)<15:
        ball.goto(random.randint(-250,250),random.randint(-250,250))
        score=score+10
        wr.clear()
        wr.write('Your Score: '+str(score),font=15)

    if score>=50:
        wr.goto(-20,0)
        wr.write('Winner',font=50)
        break
