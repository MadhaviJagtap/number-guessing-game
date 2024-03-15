import random as rd

logo = """


   ___                  _   _                         _             
  / __|_  _ ___ ______ | |_| |_  ___   _ _ _  _ _ __ | |__  ___ _ _ 
 | (_ | || / -_|_-<_-< |  _| ' \/ -_) | ' \ || | '  \| '_ \/ -_) '_|
  \___|\_,_\___/__/__/  \__|_||_\___| |_||_\_,_|_|_|_|_.__/\___|_|  


"""

easy = 10
hard = 5

def difficulty():
  level =  input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return easy
  elif level == "hard":
    return hard
  else:
    print("Invalid input")

def check(user,number,remains):
  if user < number:
    print("Too low")
    return remains-1
  elif user > number:
    print("Too high")
    return remains-1
  else:
    print(f"You got it! The answer was {number}.")
 
  
def game():
  print(logo)
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  
  number = rd.randint(1,100)
  remaining = difficulty()

  user = 0
  while user != number:
    print(f"You have {remaining} attempts remaining to guess the number.")

    user = int(input("Make a guess: "))

    remaining = check(user, number, remaining)
    if remaining == 0:
      print(f"You've run out of guesses, you lose. The answer was {number}")
      return
    elif user != number:
      print("Guess again.")


game()
