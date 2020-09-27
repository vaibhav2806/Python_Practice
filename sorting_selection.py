def sort(list):
    for i in range(len(list)):
        min_posn = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_posn]:
                min_posn = j
            
            temp = list[i]
            list[i] = list[min_posn]
            list[min_posn] = temp

list = [5,3,8,6,7,2]
sort(list)
print(list)