import turtle

# Function defs
def head(speed):
  turtle.speed(speed)
  for i in range (18):
    turtle.right(140)
    turtle.left(120)
    turtle.back(100)

def mouth(speed):
  turtle.speed(speed)
  turtle.up ()
  turtle.goto(-50,50)
  turtle.down()
  turtle.forward(mouth_size)
  
def eyes(speed, pupil):
  turtle.speed(speed)
  turtle.up ()
  turtle.goto(100,100)
  turtle.down()
  for i in range (2):
    for n in range (1,3):
      turtle.begin_fill()
      turtle.pendown()
      if n == 1:
        red_or_black = 'red'
      else:
        red_or_black = 'black'
      turtle.color(str(red_or_black))
      turtle.circle(45*(n/2))
      turtle.penup()
    turtle.back(175)
  turtle.color('black')
  
def ballon(speed):
  turtle.speed(10)
  turtle.up()
  turtle.goto(-300,50)
  turtle.down()
  turtle.right(90)
  turtle.forward(300)
  turtle.up()
  turtle.goto(-355,110)
  turtle.down()
  for i in range (18):
    turtle.right(60)
    turtle.left(40)
    turtle.back(20)

# Start code
head(10)
mouth_size = 15
mouth(2)
eyes(10,1)
ballon(10)
