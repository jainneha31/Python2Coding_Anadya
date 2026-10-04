import turtle

screen = turtle.Screen()
screen.title('Rainbow Hexagon Fractal')
screen.setup(800, 700)
screen.bgcolor('white')

t = turtle.Turtle()
t.speed(0)
t.width(1)


def hexagon(size, turn):
  t.penup()
  t.goto(0, 0)
  t.setheading(turn - 90)
  t.forward(size)
  t.setheading(turn + 30)
  t.pendown()

  # draw the sides
  for side in range(6):
    t.forward(size)
    t.left(60)


colors = ['red', 'orange', 'yellow', 'green',
          'blue', 'purple', 'pink']

size = 250
turn = 0
number = 0


while size > 10:
  t.color(colors[number % len(colors)])
  hexagon(size, turn)
  size = size * 0.97
  turn = turn + 4
  number = number + 1

t.hideturtle()
turtle.done()
