# Create a menu using a dictionary
restaurant_menu = {'Potatoes w/ caviar':24.50, '10 Mushroom Soup':15.50, 'Black Sea Bass':37.99, 'Maine Lobster':59.50, 'Chocolate Sorbet':9.41, 'Grapefruit Granite':10.99}

#Prompt user for commands
def prompt_user():
  user_choice = input("S Start New Order \n E Edit Order \n P Print Bill \n R Receiver Payment \n M Manager Report \n Q Quit \n ---------- Enter Choice>")
  if user_choice == "S":
    start_order()
  elif user_choice == "E":
    edit_order()
  elif user_choice == "P":
    print_bill()
  elif user_choice == "R":
    receive_payment()
  elif user_choice == "M":
    manager_report()
  elif user_choice == "Q":
    quit_program()
  else user_choice:
    print('invalid choice')
    prompt_user()