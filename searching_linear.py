pos = 0
def search(list,n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i+1
    return False

if __name__ == "__main__":
    
    list = [9,5,8,7,2,3,4,1]
    n = int(input("Enter the number you want to search: \n"))
    
    if search(list, n):
        print(f"Found at {pos+1} position.")
    else:
        print("Not Found")

