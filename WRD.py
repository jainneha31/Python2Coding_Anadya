import tkinter as tk
import random

with open('five_letter_words.txt') as file:
  wordlist = file.read().split('\n')

chosenWord = random.choice(wordlist)
guessnum = 0
current_guess = []
key_btns = {}
game_over = False

window = tk.Tk()
window.title("Wordle")


def update_grid():
  for kk in range(5):
    if kk < len(current_guess):
      grid[guessnum][kk].config(text = current_guess[kk].upper())
    else:
      grid[guessnum][kk].config(text = '')


def press_key(letter):
  global current_guess
  if game_over or len(current_guess) >= 5:
    return
  current_guess.append(letter)
  update_grid()


def press_back():
  global current_guess
  if len(current_guess) == 0:
    return
  current_guess.pop()
  update_grid()


def color_key(letter, color):
  btn = key_btns[letter]
  old = btn.cget('bg')
  if old == 'green':
    return
  if old == 'gold' and color == 'grey':
    return
  btn.config(bg = color, fg = 'white')


def press_enter():
  global guessnum, current_guess, game_over
  if game_over:
    return
  guessedWord = ''.join(current_guess).lower()
  if len(guessedWord) < 5:
    msg_label.config(text = 'Not enough letters!')
    return
  if guessedWord not in wordlist:
    msg_label.config(text = 'Not a valid word!')
    return
  msg_label.config(text = '')
  remaining = []
  for kk in range(5):
    if guessedWord[kk] != chosenWord[kk]:
      remaining.append(chosenWord[kk])
  for kk in range(5):
    lbl = grid[guessnum][kk]
    ch = guessedWord[kk]
    if ch == chosenWord[kk]:
      lbl.config(bg = 'green', fg = 'white')
      color_key(ch, 'green')
    elif ch in remaining:
      remaining.remove(ch)
      lbl.config(bg = 'gold', fg = 'white')
      color_key(ch, 'gold')
    else:
      lbl.config(bg = 'grey', fg = 'white')
      color_key(ch, 'grey')
  if guessedWord == chosenWord:
    msg_label.config(text = 'You got it!')
    game_over = True
  elif guessnum == 5:
    msg_label.config(text = 'Answer: ' + chosenWord.upper())
    game_over = True
  guessnum = guessnum + 1
  current_guess = []


grid = []
for rr in range(6):
  row_frame = tk.Frame(window)
  row_frame.pack()
  row = []
  for cc in range(5):
    lbl = tk.Label(row_frame, text = '', width = 4, height = 2,
                   font = ('Arial', 14, 'bold'), bg = 'white',
                   borderwidth = 2, relief = 'solid')
    lbl.pack(side = tk.LEFT, padx = 2, pady = 2)
    row.append(lbl)
  grid.append(row)

msg_label = tk.Label(window, text = '', font = ('Arial', 11))
msg_label.pack()

top_keys = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
top_frame = tk.Frame(window)
top_frame.pack()
for letter in top_keys:
  btn = tk.Button(top_frame, text = letter, width = 2, height = 1,
                  font = ('Arial', 10, 'bold'), bg = 'lightgrey',
                  command = lambda l = letter: press_key(l.lower()))
  btn.pack(side = tk.LEFT, padx = 1, pady = 1)
  key_btns[letter.lower()] = btn

mid_keys = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
mid_frame = tk.Frame(window)
mid_frame.pack()
for letter in mid_keys:
  btn = tk.Button(mid_frame, text = letter, width = 2, height = 1,
                  font = ('Arial', 10, 'bold'), bg = 'lightgrey',
                  command = lambda l = letter: press_key(l.lower()))
  btn.pack(side = tk.LEFT, padx = 1, pady = 1)
  key_btns[letter.lower()] = btn

bot_keys = ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
bot_frame = tk.Frame(window)
bot_frame.pack()
tk.Button(bot_frame, text = 'BACK', width = 4, height = 1,
          font = ('Arial', 9, 'bold'), bg = 'lightgrey',
          command = press_back).pack(side = tk.LEFT, padx = 1, pady = 1)
for letter in bot_keys:
  btn = tk.Button(bot_frame, text = letter, width = 2, height = 1,
                  font = ('Arial', 10, 'bold'), bg = 'lightgrey',
                  command = lambda l = letter: press_key(l.lower()))
  btn.pack(side = tk.LEFT, padx = 1, pady = 1)
  key_btns[letter.lower()] = btn
tk.Button(bot_frame, text = 'ENTER', width = 4, height = 1,
          font = ('Arial', 9, 'bold'), bg = 'lightgrey',
          command = press_enter).pack(side = tk.LEFT, padx = 1, pady = 1)


tk.mainloop()
