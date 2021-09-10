menu = {'burger':3.5 , 'chips':2.5 , 'drink':1.75} # Establishing dictionary
salads = ['cucumber' , 'lettuce' , 'tomato'] # Establishing list
sauces = ['mustard', 'bbq', 'tomato'] # Establishing list

price = 0 # Initialising value of price outside of function
total_price = 0 # Initialising value of total_price outside of function

print('Welcome!') # Welcome message

# Creating a function to call back in loop.

def menu():
  global total_price # making variable global so that it is preserved outside of function

  burger = input('Burger (Y/N): ').lower() # Burger Input

  if burger == 'y': # if burger, run the rest of the options for the burger.
    total_price = price + 3.5 # adds price of burger
    input(f'White bread? (Y/N): ').lower() # Bread Choice, normalised input through .lower() string function
    input(f'Vegetarian Pattie? (Y/N): ').lower() # Pattie Choice
    for salad in salads: # loops through elements in list to ask for salads
      salad_choice = input(f'{salad.capitalize()}? (Y/N): ').lower() # input
      if salad_choice == 'y':
        total_price = total_price + 0.75 # adds price per salad in the loop
    for sauce in sauces: # loops through elements in list to ask for salads
      sauce_choice = input(f'{sauce.capitalize()}? (Y/N): ').lower() # input
      if sauce_choice == 'y':
        total_price = total_price + 0.5 # adds price per sauce


  chips = input('Chips (Y/N): ').lower() # chips input

  if chips == 'y':
    if burger == 'y':
      total_price = total_price + 1.5 # changes price according to if a burger had been ordered
    else:
      total_price = total_price + 2.5
  drinks = input('Drink? (Y/N): ').lower() # drink input
  if drinks == 'y':
    if burger == 'y':
      total_price = total_price + 1 # changes price according to if a burger had been ordered
    else:
      total_price = total_price + 1.75

  return total_price # returns total_ price to the loop outside of the function

while True: # creates a loop for the menu function
  total_price += menu() # runs the function
  ending = input('Would you like anything more with that? (Y/N): ').lower() # reruns the function if user wants anything more

  if ending == 'n': # if user has finished the order, total price is given
    print(f'Your total price comes to ${total_price}!')
    break # breaks the loop if user has finished