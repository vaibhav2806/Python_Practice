# actual number = 45
# guess = 5
# computer : your guess was too low 
# store any number in a variable. you have to guess that number. your program should be able to tell whether the number you guesed was lesser or 
# greater than the actual number. you have to finally tell the number of attempts it took the guesser tpo guess the number.

import random 

actual_number = random.randint(1,100)
attempts = 0

while True:
    attempts +=1
    guess = int(input("Guess the number: \n"))
    if guess < actual_number:
        print("guessed number is too low!!")
    elif guess > actual_number:
        print("guessed number is too high!!")
    else:
        print("you guessed the correct number in {attempts} attempts1")
        break
print("Thanks for playing")
    