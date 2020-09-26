pos = -1
def search(list,n):
    l = 0
    u = len(list)-1
    while l <= u:
        mid = (l+u)//2

        if list[mid] == n:
            globals()['pos'] = mid
            return True

        else:
            if list[mid] < n:
                l = mid+1

            else:
                u = mid - 1
    

if __name__ == "__main__":

    list = [4,7,8,12,45,99]
    n = int(input("Enter the number: \n"))

    if search(list,n):
        print(f"Element found at {pos+1} position")
    else:
        print("Element not found")