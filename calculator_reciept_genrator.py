# keep adding numbers until the user presses enter 
list = []
sum = 0
count = 1
while(True):

    user_input = input("Enter the item price or press q to exit : \n")

    if (user_input != 'q'):
        n = int(user_input)
        list.append(n)
        sum = sum + n
        print (f"Your Order total so far {sum}")
    else:
        print(f"Your total bill is : {sum}. Thank You \n")
        break

print ("Harry Bhai Kirana Store \n" )
for x in list:
    print (count, x) 
    count += 1