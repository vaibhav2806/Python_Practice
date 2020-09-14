def matrix(m ,n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter value H[{i}][{j}]: "))
            row.append(inp)
        o.append(row)
    return o

def transpose(A):
    output = []
    for i in range (len(A)):
        row = []
        for j in range (len(A[0])):
            row.append(A[j][i])
        output.append(row)
    return output
            
def matrix_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("\t", matrix[i][j], end = " ")
        print("\t")
        
def again():
    print("""**type y or yes to do again otherwise type n or no**""")
    do_again = input("yes or no?")
    if do_again == 'yes' or do_again == 'y':
        transpose()
    elif do_again == 'no' or do_again == 'n':
        print("See You Later.")
    else:
        again()

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

print("Enter values in matrix A:\n")
A = matrix(m,n)
matrix_print(A)

again()

t = transpose(A)
print("\n")
matrix_print(t)