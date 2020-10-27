str = input("Enter a string \n")
list = []
vowel = 'aeiouAEIOU'
count1= 0 
count2= 0 
count3= 0 
count4= 0
count5= 0
for x in str:
    if x in vowel:
        list.append(x)
        new_str = str.replace(x,"")

for i in list:
    if i == 'a' :
        count1 = count1+1
    elif i == 'e':
        count2 = count2+1
    elif i == 'i':
        count3 = count3+1
    elif i == 'o':
        count4 = count4+1
    elif i == 'u':
        count5 = count5+1
    else:
        pass             
print("a:",count1)
print("e:",count2)
print("i:",count3)
print("o:",count4)
print("u:",count5)

print(new_str)
