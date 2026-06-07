import turtle
import random
import time

CELL = 20
N_FOODS = 10

# ---- SCREEN SETUP ----
screen = turtle.Screen()
screen.setup(450, 480)
screen.title('Hungry Snake')
screen.bgcolor('light green')
screen.tracer(0)

# ---- SNAKE HEAD SHAPE ----
head_shape = ((-10, -10), (10, -10), (14, 12), (0, 17), (-14, 12))
turtle.register_shape("snake_head", head_shape)

# ---- DRAW GRID ----
def draw_grid():
    grid = turtle.Turtle()
    grid.speed(0)
    grid.penup()
    grid.hideturtle()
    for row in range(20):
        for col in range(20):
            grid.goto(-190 + col * CELL, -190 + row * CELL)
            grid.pendown()
            grid.color("lime green" if (row + col) % 2 == 0 else "DarkOliveGreen1")
            grid.begin_fill()
            for _ in range(4):
                grid.forward(CELL)
                grid.right(90)
            grid.end_fill()
            grid.penup()

draw_grid()
screen.update()

# ---- SNAKE HEAD ----
t = turtle.Turtle()
t.shape("snake_head")
t.color("#4285F4")
t.penup()
t.speed(0)

# ---- EYES ----
eye1 = turtle.Turtle()
eye2 = turtle.Turtle()
for eye in [eye1, eye2]:
    eye.shape("circle")
    eye.turtlesize(0.3)
    eye.color("black")
    eye.penup()
    eye.speed(0)

def position_eyes():
    x, y = t.xcor(), t.ycor()
    if t.heading() in (0.0, 180.0):
        eye1.goto(x, y + 5)
        eye2.goto(x, y - 5)
    else:
        eye1.goto(x + 5, y)
        eye2.goto(x - 5, y)

# ---- SCORE & REPORT ----
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.color("black")
pen.goto(-185, 205)

report = turtle.Turtle()
report.penup()
report.hideturtle()
report.color("black")
report.goto(0, 0)

# ---- FOOD ----
food = turtle.Turtle()
food.shape("circle")
food.color("IndianRed3")
food.penup()
food.speed(0)

# ---- PLAY AGAIN BUTTON ----
btn = turtle.Turtle()
btn.hideturtle()
btn.speed(0)
btn.penup()

btn_lbl = turtle.Turtle()
btn_lbl.penup()
btn_lbl.hideturtle()
btn_lbl.color("black")
btn_lbl.goto(0, -38)

segments    = []
foods_eaten = 0

def get_occupied():
    pos = {(round(t.xcor()), round(t.ycor()))}
    for s in segments:
        pos.add((round(s.xcor()), round(s.ycor())))
    return pos

def place_food():
    occupied = get_occupied()
    grid = [(x, y)
            for x in range(-180, 181, CELL)
            for y in range(-180, 181, CELL)
            if (x, y) not in occupied and not (x == 0 and y == 0)]
    if grid:
        food.goto(random.choice(grid))
        food.showturtle()

# ---- CONTROLS ----
next_heading = [0.0]

def right():
    if t.heading() != 180.0: next_heading[0] = 0.0
def left():
    if t.heading() != 0.0:   next_heading[0] = 180.0
def up():
    if t.heading() != 270.0: next_heading[0] = 90.0
def down():
    if t.heading() != 90.0:  next_heading[0] = 270.0

screen.onkey(right, "Right")
screen.onkey(left,  "Left")
screen.onkey(up,    "Up")
screen.onkey(down,  "Down")
screen.listen()

# ---- GRID-SNAPPED MOVEMENT ----
def move():
    h = t.heading()
    if   h == 0.0:   t.setx(t.xcor() + CELL)
    elif h == 180.0: t.setx(t.xcor() - CELL)
    elif h == 90.0:  t.sety(t.ycor() + CELL)
    elif h == 270.0: t.sety(t.ycor() - CELL)

# ---- PLAY GAME ----
def play_game(x=None, y=None):
    global segments, foods_eaten

    btn.clear()
    btn_lbl.clear()
    screen.onclick(None)

    for seg in segments:
        seg.hideturtle()
        seg.goto(2000, 2000)
    segments    = []
    foods_eaten = 0
    next_heading[0] = 0.0

    t.goto(0, 0)
    t.setheading(0)
    t.showturtle()
    eye1.showturtle()
    eye2.showturtle()
    position_eyes()
    pen.clear()
    report.clear()
    food.hideturtle()
    place_food()

    steps     = 0
    speed     = 0.3
    game_over = False

    while not game_over:
        screen.update()
        pen.clear()

        if foods_eaten < N_FOODS:
            pen.write('Score: ' + str(foods_eaten) + ' / ' + str(N_FOODS),
                      font=("Courier", 14, "normal"))
        else:
            pen.write('Score: ' + str(foods_eaten) + ' / ' + str(N_FOODS) +
                      '   Return to center!',
                      font=("Courier", 11, "normal"))

        t.setheading(next_heading[0])
        position_eyes()

        if segments:
            tail_x, tail_y = segments[-1].xcor(), segments[-1].ycor()
        else:
            tail_x, tail_y = t.xcor(), t.ycor()

        for i in range(len(segments) - 1, 0, -1):
            segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())
        if segments:
            segments[0].st()
            segments[0].goto(t.xcor(), t.ycor())

        move()
        steps += 1
        position_eyes()

        hx, hy = t.xcor(), t.ycor()

        if hx > 190 or hx < -190 or hy > 190 or hy < -190:
            report.write("Game Over!\nScore: " + str(foods_eaten) +
                         "    Steps: " + str(steps),
                         align="center", font=("Courier", 18, "normal"))
            game_over = True

        for seg in segments:
            if abs(seg.xcor() - hx) < 5 and abs(seg.ycor() - hy) < 5:
                report.write("Game Over!\nScore: " + str(foods_eaten) +
                             "    Steps: " + str(steps),
                             align="center", font=("Courier", 18, "normal"))
                game_over = True
                break

        if game_over:
            break

        if foods_eaten < N_FOODS and food.isvisible():
            if abs(food.xcor() - hx) < 15 and abs(food.ycor() - hy) < 15:
                foods_eaten += 1
                food.hideturtle()
                new_seg = turtle.Turtle()
                new_seg.shape('square')
                new_seg.color('#4285F4')
                new_seg.penup()
                new_seg.speed(0)
                new_seg.goto(tail_x, tail_y)
                new_seg.st()
                segments.append(new_seg)
                speed = max(0.05, speed - 0.005)
                if foods_eaten < N_FOODS:
                    place_food()

        if foods_eaten == N_FOODS:
            if abs(hx) < 20 and abs(hy) < 20:
                time.sleep(1)
                t.ht()
                eye1.ht()
                eye2.ht()
                for seg in segments:
                    seg.ht()
                report.write("You Win!\nSteps: " + str(steps),
                             align="center", font=("Courier", 22, "normal"))
                game_over = True

        time.sleep(speed)

    # Draw white button rectangle 
    btn.clear()
    btn.goto(-70, -15)
    btn.color("white", "white")
    btn.pendown()
    btn.begin_fill()
    for side in [140, 40, 140, 40]:
        btn.forward(side)
        btn.right(90)
    btn.end_fill()
    btn.penup()

    # Write "Play Again"
    btn_lbl.clear()
    btn_lbl.goto(0, -38)
    btn_lbl.write("Play Again", align="center", font=("Courier", 13, "bold"))

    screen.onclick(lambda x, y: play_game() if -70 < x < 70 and -55 < y < -15 else None)
    screen.update()

play_game()
turtle.mainloop()
