import random

print("Welcome to Domino's Pizza Shop.")
print('Choose your pizza preferences.')
print('Type done when you are finished choosing a group.')
print()

def add_s(word):
  return word + 's'

def correct_case(answer, choices):
  for choice in choices:
    if answer.lower() == choice.lower():
      return choice
  return answer


def choose_toppings(name, choices, limit, word):
  chosen = []

  if limit == 0:
    print('You have used all of your meat and veggie topping spaces.')
    return chosen

  print()
  print(name, 'choices:', ', '.join(choices))

  if name == 'Cheese':
    print('Cheese does not count as a topping.')
    print('Choose as much cheese as you want, or type done.')
  else:
    print('You can choose up to', limit, word, 'toppings.')

  while len(chosen) < limit:
    answer = input('Choose a ' + word + ' topping or type done:\n')

    if answer.lower() == 'done' or answer.lower() == 'none':
      break
    
    answer = correct_case(answer, choices)

    if answer in choices and answer not in chosen:
      chosen.append(answer)
    elif answer in chosen:
      print('You already chose that', word, 'topping.')
    else:
      print('That is not one of the available', word, 'toppings.')

  return chosen


# parts of a pizza.
specs = ['Size', 'Crust', 'Sauce', 'Price']
specs_new = list(map(add_s, specs))
master_dict = dict.fromkeys(specs_new)

master_dict['Sizes'] = ['10"', '12"', '14"', '18"']
master_dict['Crusts'] = ['Original', 'Thin', 'Pan', 'Stuffed']
master_dict['Sauces'] = ['Marinara', 'Garlic Parmesan', 'Alfredo', 'BBQ']
master_dict['Prices'] = ['$8', '$10', '$12', '$14']

meat_toppings = ['Pepperoni', 'Italian Sausage','Grilled Chicken', 'Smoked Bacon','Corn', 'Spinach']
cheese_toppings = ['Mozzarella', 'Cheddar', 'Parmesan', 'Provolone', 'Feta', 'Ricotta', 'Extra Cheese']

#list of random pizzas.
pizzas = []

for number in range(60):
  new_pizza = dict.fromkeys(specs)

  for spec in new_pizza:
    new_pizza[spec] = random.choice(master_dict[spec + 's'])

  # price decides amount of toppings
  if new_pizza['Price'] == '$10':
    topping_number = 3
  elif new_pizza['Price'] == '$12':
    topping_number = 5
  elif new_pizza['Price'] == '$14':
    topping_number = 7
  else:
    topping_number = 1

  # Cheese is not topping
  meat_number = random.randint(0, min(topping_number, len(meat_toppings)))
  veggie_number = topping_number - meat_number

  if veggie_number > len(veggie_toppings):
    veggie_number = len(veggie_toppings)
    meat_number = topping_number - veggie_number

  new_pizza['Meat'] = random.sample(meat_toppings, meat_number)
  new_pizza['Veggies'] = random.sample(veggie_toppings, veggie_number)
  new_pizza['Cheese'] = random.sample(
      cheese_toppings, random.randint(1, len(cheese_toppings)))
  pizzas.append(new_pizza)


# ask the customer for the size, crust, sauce, and price
customer_choice = dict.fromkeys(specs)

for spec in specs:
  choices = ', '.join(master_dict[spec + 's'])
  answer = input(
      'What ' + spec.lower() + ' do you want? (' + choices + ')\n')
  customer_choice[spec] = correct_case(
      answer, master_dict[spec + 's'])

# total number of meat and veggie toppings allowed by the price
if customer_choice['Price'] == '$10':
  topping_number = 3
elif customer_choice['Price'] == '$12':
  topping_number = 5
elif customer_choice['Price'] == '$14':
  topping_number = 7
else:
  topping_number = 1

# meat and veggie toppings share the limit
chosen_meat = choose_toppings(
    'Meat', meat_toppings, topping_number, 'meat')
leftover_toppings = topping_number - len(chosen_meat)
chosen_veggies = choose_toppings(
    'Veggies', veggie_toppings, leftover_toppings, 'veggie')


# Cheese is chosen separately 
chosen_cheese = choose_toppings(
    'Cheese', cheese_toppings, len(cheese_toppings), 'cheese')


# Add the customer's pizza to the list.
# This makes sure the customer's choices can always be found.
customer_pizza = dict.fromkeys(specs)

for spec in customer_choice:
  customer_pizza[spec] = customer_choice[spec]

customer_pizza['Meat'] = chosen_meat
customer_pizza['Veggies'] = chosen_veggies
customer_pizza['Cheese'] = chosen_cheese
pizzas.append(customer_pizza)


# Make a query from the customer's choices.
query = ''

for spec in customer_choice:
  if customer_choice[spec].lower() == 'none':
    pass
  else:
    query = query + "pizza['" + spec + "'] == '" + \
            customer_choice[spec] + "' and "

for topping in chosen_meat:
  query = query + "'" + topping + "' in pizza['Meat'] and "

for topping in chosen_veggies:
  query = query + "'" + topping + "' in pizza['Veggies'] and "

for topping in chosen_cheese:
  query = query + "'" + topping + "' in pizza['Cheese'] and "

if query != '':
  query = query[:-5]
  selected = [pizza for pizza in pizzas if eval(query)]
else:
  selected = pizzas


print()
print(len(selected), 'pizzas matched your choices.')
print()

headers = ['Size', 'Crust', 'Sauce', 'Price',
           'Meat', 'Veggies', 'Cheese']
rows = []

for pizza in selected:
  row = [pizza['Size'], pizza['Crust'], pizza['Sauce'],
         pizza['Price'], ', '.join(pizza['Meat']),
         ', '.join(pizza['Veggies']), ', '.join(pizza['Cheese'])]
  rows.append(row)

widths = []

for kk in range(len(headers)):
  longest = len(headers[kk])

  for row in rows:
    if len(row[kk]) > longest:
      longest = len(row[kk])

  widths.append(longest + 3)

for kk in range(len(headers)):
  print(headers[kk].ljust(widths[kk]), end = '')
print()

for row in rows:
  for kk in range(len(row)):
    print(row[kk].ljust(widths[kk]), end = '')
  print()
