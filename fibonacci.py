import time 

def fiboiter(n): # More efficient 
    prevNum = 0
    currNum = 1
    for _ in range ( 1 , n):
        prvPrevNum = prevNum
        prevNum = currNum
        currNum = prvPrevNum + prevNum 
    return currNum

def fiborecur(n): # Less efficient
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiborecur(n-2) + fiborecur(n-1)
if __name__ == "__main__":
    num = int(input("enter a number: \n"))
    init = time.time()
    #print(f"recursion value of fib({num}) is: {fiborecur(num)}")
    print(f"iterative value of fib({num}) is: {fiboiter(num)}")
    print(f"It took {time.time() - init} seconds ") #to see the time difference make one print from above as comment

    