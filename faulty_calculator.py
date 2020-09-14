# 45 * 3 = 555 
# 56 + 9 = 77
# 56 / 6 = 4
def calculator():

    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    operator = input("""Enter operator you want to use:
                                    1) Add: +
                                    2) Sub: -
                                    3) Mul: *
                                    4) Div: /
                                    5) Pow: ** \n""")
    if num1 == 45 and num2 == 3 and operator == '*':
        print(555)
    
    elif num1 == 56 and num2 == 9 and operator =='+':
        print(77)

    elif num1 == 56 and num2 == 6 and operator =='/':
        print(4)

    elif operator == "+":
        answer = num1 + num2
        print(answer)
    
    elif operator == "-":
        answer = num1 - num2
        print(answer)

    elif operator == "/":
        answer = num1 / num2
        print(answer)

    elif operator == "*":
        answer = num1 * num2
        print(answer)
    elif operator == "**":
        answer = num1 ** num2
        print(answer)

    

    else:
        print("Error! Check your inputs.")

    again()

def again():
    call_again = input("""Do you want to calculate again?
    enter y or yes to calculate again otherwise n or no. \n""")
    
    if call_again == 'yes' or call_again == 'y':
        calculator()
    elif call_again == 'no' or call_again == 'n':
        print("see you later!")
    else:
        again()

calculator()