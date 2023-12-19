import random

options = ["rock", "paper", "scissors"]

user_option = input('Choose: paper, rock or scissors => ')
user_option = user_option.lower()

if user_option not in options:
  print('Invalid option')
  
computer_option = random.choice(options)

print('User option => ', user_option)
print('Computer option => ', computer_option)

if user_option == computer_option :
  print('DRAW!')
elif user_option == 'rock' :
    if computer_option == 'scissors':
      print('YOU WIN!')
    else:
      print( 'YOU LOSE!')
elif user_option == 'paper' :
    if computer_option == 'rock' :
      print('YOU WIN!')
    else:
      print( 'YOU LOSE!')
      
elif user_option == 'scissors' :
    if computer_option == 'paper':
      print('YOU WIN!')
    else:
      print( 'YOU LOSE!')
else:
  print('Invalid option!')