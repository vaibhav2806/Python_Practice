def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range (i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

list = [5,3,2,8,6,7]
sort (list)
print(list)