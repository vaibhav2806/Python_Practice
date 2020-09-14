def matrix(m,n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"H[{i}][{j}]"))
            row.append(inp)
        o.append(row)
    return o

def sub(m,n):
    output = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        output.append(row)
    return output

m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

print("Enter values in matrix A: \n")
A = matrix(m,n)
print (A)

print("Enter the values in matrix B: \n")
B = matrix(m,n)
print(B)

sb = sub(A,B)
print(sb)