"""
GUESS THE NUMBER GAME

Welcome to game

random number generated

Think of number between x and y

Ask user to guess

Say if correct

Say if incorrect

Say "thanks for playing"


EXTRAS
ask user to set max/min vals
offer user clues
"""
import random
import time

def RandomNum():
  randomNumber = random.randint(1,10)
  return randomNumber

randomNumber=RandomNum()

def welcome():
  print ("Welcome to Cesar's Number guess!")

def gameStart():
  print("I am thinking of a number between 1 and 10.")
  time.sleep(1)
  print("Can you guess what it is?")
  userInput(randomNumber)
 



def userInput(NumberToGuess):
  try:
    userGuess = int(input("Go on, enter a number between 1 and 10."))
    if userGuess == NumberToGuess:
        rightAnswer()
    elif userGuess >10 or userGuess <1:
      UserGuessOutOfBounds()
    elif userGuess > NumberToGuess:
      UserGuessHigh()
    elif userGuess < NumberToGuess:
      UserGuessLow()
  except ValueError:
    WrongInput()



def ByeBye():
  time.sleep(0.5)
  print("Thanks for playing!")

def WrongInput():
  print("What you just typed in makes no sense, you useless clobberbat.")
  userInput(randomNumber)

def UserGuessLow():
  time.sleep(0.5)
  print("That's too low! Try again.")
  userInput(randomNumber)
  

def UserGuessHigh():
  time.sleep(0.5)
  print("That's too high! Try again.")
  userInput(randomNumber)

def UserGuessOutOfBounds():
  time.sleep(0.5)
  print("I said between 1 and 10! How lucky did you bloody feel when you put finger to button?")
  time.sleep(1)
  print("Honestly, I suspect a problem exists between your chair and your keyboard...")
  time.sleep(1)
  print("Right...")
  time.sleep(1)
  print("Sigh...let's try that again...")
  time.sleep(1)
  userInput(randomNumber)

def rightAnswer():
  time.sleep(0.5)
  print("That's right, you bloody genius. How'd you get to be so clever?")
  time.sleep(1)
  playAgain()

def playAgain():
  userPlayAgain=input("Would you like to play again? Enter 'yes' or 'no'.")
  if userPlayAgain == "yes":
    gameStart()
  elif userPlayAgain =="no":
    ByeBye()
  elif userPlayAgain != "yes" or "no":
    time.sleep(1)
    print("Speak slowly and carefully. 'yes', or 'no'?")
    playAgain()
    
    
  
welcome()

gameStart()



