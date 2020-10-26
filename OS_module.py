import os
print(dir(os))
# print(os.getcwd())          #get current workng directly 
# os.chdir("C://")            #to change directory
# print(os.getcwd())
# f = open("harry_food.txt")  #after changing directory we wont be able to open once we comment out os.chdir() then we will be able to open the file.
# print(os.listdir())         #list of folders in present directory
# print(os.listdir("C://"))   #list of folders in C drive
# os.mkdir("This")            #this will make a directory 
# os.makedirs("This/that")    #this will make a directory named 'This" and 'that' within it.

#  os.rename("harry_food.txt","vaibhav_food.txt") #to rename a file 

# print(os.path.join("C://","/vaibhav_food.txt")) #to join directory with other drive

# print(os.path.exists("C://"))                   #will return true or false if path exists
# print(os.path.isfile("C://"))