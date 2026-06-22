import random
import time

print('Welcome to the Card Game of WAR!')
print('Pick a card from your dealt deck. if your cards value is greater, then you recive the cards placed on the table. If not, the computer keeps the cards on the table.')
print('If its called WAR, your fate will be decided based on the card you will play.')
print('Good luck!')

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K', 'A']    # X = 10
suits = [' ♣️  ', ' ♦️  ', ' ♥️  ', ' ♠️  ']   

# Deck of Cards
deck_of_cards = []

for kk in range(len(suits)):
    for jj in range(len(cards)):
        deck_of_cards.append(suits[kk]+cards[jj])

print('Unshuffled Deck:')
for kk in range(len(deck_of_cards)):
    print(deck_of_cards[kk], end = ' ')
print()

random.shuffle(deck_of_cards) 

print('Shuffled Deck:')
for kk in range(len(deck_of_cards)):
    print(deck_of_cards[kk], end = ' ')

# Toss will decide which player goes first
toss = random.choice(deck_of_cards)
print()
if '♣' in toss or '♦' in toss:
    first_mover = 'player'
    print('You won the toss, you will play first.')
else:
    first_mover = 'computer'
    print('Computer won the toss, it will play first')

# Deal the cards
table_cards = []
run_cnt = 0
done = False
player_cards = []
comput_cards = []

while not done:
    n_cards_p = random.randint(1, 3)       
    n_cards_c = random.randint(1, 3)

    if len(player_cards) + n_cards_p > 26:
        n_cards_p = 26 - len(player_cards)
        n_cards_c = 26 - len(comput_cards)
        done = True

    elif len(comput_cards) + n_cards_c > 26:
        n_cards_c = 26 - len(comput_cards)
        n_cards_p = 26 - len(player_cards)
        done = True

    for kk in range(run_cnt, run_cnt + n_cards_p, 1):
        player_cards.append(deck_of_cards[kk])

    run_cnt = run_cnt + n_cards_p

    for kk in range(run_cnt, run_cnt + n_cards_c, 1):
        comput_cards.append(deck_of_cards[kk])

    run_cnt = run_cnt + n_cards_c

print()
print('Player Dealt Cards (' + str(len(player_cards)) + '):')   
for kk in range(len(player_cards)):
    print(player_cards[kk], end = ' ')
print()

# Game loop
move_complete = False
game_complete = False
moves_played = 0

while not(game_complete):
  move_complete = False
  if len(player_cards)<1 or len(comput_cards)<1:
    move_complete = True
    game_complete = True

  while not(move_complete):
    print()
    print('Your Cards:')
    for kk in range(len(player_cards)):
        print(str(kk+1) + '.' + player_cards[kk], end = ' ')
    print()
    choice = int(input('Pick a card (enter number): ')) - 1
    card_p = player_cards.pop(choice)
    card_c = comput_cards.pop(random.randint(0, len(comput_cards)-1))
    print()
    print('Player Card is ...', card_p)
    print('Computer Card is ...', card_c)

    table_cards.append(card_p)
    table_cards.append(card_c)

    if cards.index(card_p[-1]) > cards.index(card_c[-1]):    
      print('Player Wins ... ')
      input()
      player_cards.extend(table_cards)
      table_cards.clear()
      move_complete = True
      moves_played = moves_played + 1
    elif cards.index(card_p[-1]) < cards.index(card_c[-1]):  
      print('Computer Wins ... ')
      input()
      comput_cards.extend(table_cards)
      table_cards.clear()
      move_complete = True
      moves_played = moves_played + 1
    else:
      print("War begins")
      input()
      if len(player_cards)<4 or len(comput_cards)<4:
        print('Not enough cards for war.')
        table_cards.clear()
        move_complete = True
      else:
        print('3 cards face down from each player:')
        for kk in range(3):
            table_cards.append(player_cards.pop(0))
        for kk in range(3):
            table_cards.append(comput_cards.pop(0))
        print('Table Cards:', len(table_cards))

    if moves_played == 100:
      game_complete = True

    print("Player Cards:", len(player_cards), "Computer Cards:", len(comput_cards), "Table Cards:", len(table_cards))    

print()
print()

if len(player_cards) > len(comput_cards):
  print('PLAYER is the winner')
elif len(player_cards) < len(comput_cards):
  print('COMPUTER is the winner')
else:
  print('GAME drawn!')