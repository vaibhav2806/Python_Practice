# Health Managment System
# 3 clients harry , rohan and hammad
# 3 files for food log and 3 files for exercise log, total 6 files
# write a function that when executed takes as input 1 for harry, 2 for rohan, 3 for hammad
# write 1 more function to retrieve exercise or food for any client 
# print logs with time stamp


import datetime
def getdate():
    return datetime.datetime.now()

def log(k):
    if k == 1:
        c = int(input("Enter 1 for food & 2 for exercise: "))
        if c == 1:
            meal = input("What did you eat? : ")
            with open ("harry_food.txt", "a") as m:
                m.write(str([str(getdate())])+":"+meal+"\n")
            print("Done")
        elif c == 2:
            exercise = input("Which exercise did you do? : ")
            with open("harry_exercise.txt", "a") as e:
                e.write(str([str(getdate())])+":"+exercise+"\n")
            print("Done")
        else:
            print("Wrong Choice!!!")

    elif k == 2:
        c = int(input("Enter 1 for food & 2 for exercise: "))
        if c == 1:
            meal = input("What did you eat? : ")
            with open("rohan_food.txt", "a") as m:
                m.write(str([str(getdate())])+":"+meal+"\n")
            print("Done") 
        elif c == 2:
            exercise = input("Which exercise did you do? :") 
            with open("rohan_exercise.txt", "a") as e:
                e.write(str([str(getdate())])+":"+exercise+"\n")
            print("Done")
        else:
            print("Wrong Choice!!!")

    elif k == 3:
        c = int(input("Enter 1 for food & 2 for exercise: "))
        if c == 1:
            meal = input("What did you eat? : ")
            with open("hammad_meal.txt", "a") as m:
                m.write(str([str(getdate())])+":"+meal+"\n")
            print("Done")
        elif c == 2:
            exercise = input("Which exercise did you do? : ")
            with open("hammad_exercise.txt" , "a") as e:
                e.write(str([str(getdate())])+":"+exercise+"\n")
            print("Done")
        else:
            print("Wrong Choice!!!")

    else:
        print("Please enter a valid input!!!")

def retrieve(k):
    if k == 1:
        c = int(input("Enter 1 for food & 2 for exercise: "))
        if c == 1:
            with open ("harry_food.txt") as m:
                for i in m:
                    print(i,end = "")
        elif c == 2:
            with open("harry_exercise.txt") as e:
                for i in e:
                    print(i,end = "")
        else:
            print("Wrong Choice!!!")

    elif k == 2:
        c = int(input("Enter 1 for food & 2 for exercise: "))
        if c == 1:
            with open("rohan_food.txt") as m:
                for i in m:
                    print(i ,end = "") 
        elif c == 2:
            with open("rohan_exercise.txt") as e:
                for i in e:
                    print(i ,end = "")
        else:
            print("Wrong Choice!!!")

    elif k == 3:
        c = int(input("Enter 1 for food & 2 for exercise: "))
        if c == 1:
            with open("hammad_meal.txt") as m:
                for i in m:
                    print(i,end = "")
        elif c == 2:
            with open("hammad_exercise.txt") as e:
                for i in e:
                    print(i,end = "")
        else:
            print("Wrong Choice!!!")

    else:
        print("Please enter a valid input!!!")


print("********Health Managment System********")
a = int(input("Press 1 for log and 2 to retrieve: "))
if a == 1:
    name = int(input("""Press: 1 for Harry 2 for Rohan 3 for Hammad \n"""))
    log(name)
                                           
else:
    name = int(input("""Press: 1 for Harry 2 for Rohan 3 for Hammad \n"""))
    retrieve(name)