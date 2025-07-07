import random

number=random.randint(1,100)
guess=None
NumberOfTimeToGuess=1

while guess!=number:
    guess=int(input("Guess a number between 1 to 100 : "))
    
    if guess<number:
        print("too low")
        NumberOfTimeToGuess+=1
    elif guess>number:
        print("Too high")
        NumberOfTimeToGuess+=1
    else:
        print("You got it!")
        print("You guessed in",NumberOfTimeToGuess,"times")