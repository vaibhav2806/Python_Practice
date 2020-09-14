import random
def game():
    list = ['snake','water','gun']
    i = 0
    comp_score = 0
    user_score = 0
    while i<3:
        comp = random.choice(list)
        user = input("Choose one of the options: snake , water , gun : \n")

        if user == 'water' and comp == 'gun':
            print("You Won ")
            user_score += 1
            print(f"Scores You = {user_score} and CPU = {comp_score} ")
        elif user == 'snake' and comp == 'water':
            print("You Won ")
            user_score += 1
            print(f"Scores You = {user_score} and CPU = {comp_score} ")
        elif user == 'gun' and comp == 'snake':
            print("You Won ")
            user_score += 1
            print(f"Scores You = {user_score} and CPU = {comp_score} ")

        elif user == 'water' and comp == 'snake':
            print("CPU Won ")
            comp_score += 1
            print(f"Scores You = {user_score} and CPU = {comp_score} ")
        elif user == 'gun' and comp == 'water':
            print("CPU Won ")
            comp_score += 1
            print(f"Scores You = {user_score} and CPU = {comp_score} ")
        elif user == 'snake' and comp == 'gun':
            print("CPU Won ")
            comp_score += 1
            print(f"Scores You = {user_score} and CPU = {comp_score} ")

        elif user == 'water' and comp == 'water':
            print("Draw ")
            print(f"Scores You = {user_score} and CPU = {comp_score} ")
        elif user == 'gun' and comp == 'gun':
            print("Draw ")
            print(f"Scores You = {user_score} and CPU = {comp_score} ")
        elif user == 'snake' and comp == 'snake':
            print("Draw ")
            print(f"Scores You = {user_score} and CPU = {comp_score} ")
        else:
            print("Enter a valid option!")
        i = i+1
    print("Thank you for playing")
game()