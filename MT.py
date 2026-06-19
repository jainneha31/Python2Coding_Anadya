import turtle
import random

print("Welcome to Hangman!")
print("Guess any letter from the secret word. You have 6 chances before the hangman is fully drawn. Good luck!")

# Turtle Setup

drawer = turtle.Turtle()
drawer.speed(3)

screen = turtle.Screen()
screen.title("Hangman")

# Background Setup

screen.bgcolor("lightblue")

# Drawing for Hanger

drawer.penup()
drawer.goto(-100, -100)
drawer.pendown()

drawer.forward(100)

drawer.backward(50)
drawer.left(90)
drawer.forward(150)

drawer.right(90)
drawer.forward(75)

drawer.right(90)
drawer.forward(25)

# Drawing for Body Parts

def draw_head():

    drawer.penup()
    drawer.goto(5, 5)
    drawer.pendown()

    drawer.circle(20)


def draw_body():

    drawer.penup()
    drawer.goto(25, -15)
    drawer.setheading(270)
    drawer.pendown()

    drawer.forward(60)


def draw_left_arm():

    drawer.penup()
    drawer.goto(25, -45)
    drawer.pendown()

    drawer.goto(5, -65)


def draw_right_arm():

    drawer.penup()
    drawer.goto(25, -45)
    drawer.pendown()

    drawer.goto(45, -65)


def draw_left_leg():

    drawer.penup()
    drawer.goto(25, -75)
    drawer.pendown()

    drawer.goto(5, -100)


def draw_right_leg():

    drawer.penup()
    drawer.goto(25, -75)
    drawer.pendown()

    drawer.goto(45, -100)
    
# Word list

words = ["python", "coding", "wibyte", "turtle", "output", "string", "import", "codespaces", "loops", "slicing"]

secret_word = random.choice(words)


print("Hint: Contains letter", secret_word[2:7:3])

# Create Blanks

display = []

for letter in secret_word:

    display.append("_")

# Game Variables

wrong_guesses = 0

guessed_letters = []

# Main Loop

while wrong_guesses < 6 and "_" in display:

    print()
    print("Word:", " ".join(display))

    guess = input("Guess a letter: ")

    if len(guess) == 0:

        print("Please enter a letter.")

    elif len(guess) > 1:

        print("Only one letter allowed.")

    elif guess in guessed_letters:

        print("You already guessed that letter.")

    else:

        guessed_letters.append(guess)

        if guess in secret_word:

            print("Correct!")

            index = 0

            for letter in secret_word:

                if letter == guess:

                    display[index] = guess

                index += 1

        else:

            print("Wrong!")

            wrong_guesses += 1

            if wrong_guesses == 1:

                draw_head()

            elif wrong_guesses == 2:

                draw_body()

            elif wrong_guesses == 3:

                draw_left_arm()

            elif wrong_guesses == 4:

                draw_right_arm()

            elif wrong_guesses == 5:

                draw_left_leg()

            elif wrong_guesses == 6:

                draw_right_leg()

# End Game

print()

if "_" not in display:

    print("You Win!")
    print("The word was:", secret_word)

else:

    print("Game Over!")
    print("The word was:", secret_word)

turtle.done()
