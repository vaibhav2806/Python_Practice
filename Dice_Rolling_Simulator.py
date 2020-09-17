import random
import time
min = 1 
max = 6
roll =  "yes"
while roll == "yes" or roll == "YES" or roll == "Yes" or roll == "y":
    print("rolling dice........")
    time.sleep(1)
    dice_1 = random.randint(min,max)
    dice_2 = random.randint(min,max)
    print("player 1 number =", dice_1)
    print("player 2 number =", dice_2)
    if dice_1 == dice_2:
        print("congratulations you got the same values!!")
    elif dice_1>dice_2:
        print("player 1 wins!")
    else:
        print("player 2 wins!")
    roll = input("roll the dice again?")



