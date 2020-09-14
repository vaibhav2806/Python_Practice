number = int(input("Enter a number: \n"))
sum = 0
temp = number 
order = len(str(number))

while number>0:
    digit = number % 10
    sum += digit ** order
    number = number//10

if (sum == temp):
    print(f"{temp} is an armstrong number")
else:
    print(f"{temp} is not an armstrong number")