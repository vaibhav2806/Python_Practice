# pattern printing
# input = integer n
# boolean = true or false 
# if True then,
# *
# **
# ***
# ****
# else 
# ****
# ***
# **
# *

def pattern():

    n = int(input("Enter a number:\n"))
    inp = input("Enter t for True OR f for False: ")

    if inp == 'True'or inp == 't':
        for i in range (n+1):
            for j in range (i):
                print("*",end = ' ')
            print("\n")

    elif inp == 'False' or inp == 'f':
        for i in range (n+1):
            for j in range (n-i):
                print("*",end = ' ')
            print("\n")

    else:
        print("You made a wrong choice.")

    again()

def again():

    do_again = input("""Do you want to do it again type y for yes and n for no.: """)
    if do_again == 'y' or do_again == 'yes':
        pattern()
    elif do_again == 'n' or do_again == 'no':
        print("See You Later.")
    else:
        again()

pattern()