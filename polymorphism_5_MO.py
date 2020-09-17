#METHOD OVERLOADING 
import multipledispatch

@dispatch (int,int)
def add(a,b):
    r = a+b
    print(r)

@dispatch(int,int,int)
def add(a,b,c):
    r = a+b+c
    print(r)

#add(5,6)
add(5,6,7)