# Find Factorial & No Of Trailing Zeros In A Factorial Of A Number

def factorial(number):
    fact = 1
    while number>0:
        fact = fact * number 
        number = number-1
    return fact

def factorialTrailingZero(number):
    # 5! = 5*4*3*2*1
    # 6! = 6*5*4*3*2*1
    #100 ! = 100//5 + 100 // 5*5
    count = 0
    i = 5 
    while (number//i != 0):
        count += int(number/i)
        i = i*5
    return count
    #fact = factorial(number)                #THIS WON'T WORK ON BIG NUMBERS 
    #count = 0
    #while (fact%10 == 0):
    #   count += 1
    #    fact = fact /10
    #return count 

if __name__ == "__main__":
    number = int(input("Enter the number : \n"))
    fact = factorial(number)
    print (f"The factorial of number is {fact}")
    print(factorialTrailingZero(number))