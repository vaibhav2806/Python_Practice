def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("\t", matrix[i][j], end = " ")
        print("\n")

def multiplication():
    m = int(input("Enter value of rows of matrix1: "))
    n = int(input("Enter value of column of matrix1: "))
    p = int(input("Enter value of rows of matrix2: "))
    q = int(input("Enter value of column of matrix2: "))
    
    if n!=p:
        print("Soory!! multiplication is not possible.")
        exit()

    # declaration of matrix
    matrix1 =[[0 for j in range (0 , n)]for i in range (0 , m) ] 
    matrix2 =[[0 for j in range (0 , q)]for i in range (0 , p) ] 
    result  =[[0 for j in range (0 , q)]for i in range (0 , m) ]

    # taking input from user
    print("For matrix1:\n")
    for i in range (0 , m):
        for j in range (0 , n):
            matrix1[i][j] = int(input("Enter element: "))
    
    print("For matrix2:\n")
    for i in range (0 , p):
        for j in range (0 , q):
            matrix2[i][j] = int(input("Enter element: "))

    print("Matrix1:\n")
    print(matrix1)
    print("Matrix2:\n")
    print(matrix2)

    # multiplication of matrix
    for i in range (0 , m): #for rendering into rows of matrix1
        for j in range (0 , q): #for rendering into column of matrix2 
            for k in range (0 , n): # for rendering into rows of matrix2
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    print("multiplication of matrix is:\n")
    print_matrix(result)

    again()


def again():
    do_again = input("""Do you want to do it again, if you want then type yes or y otherwise type no or n: """)
    if do_again == 'yes' or do_again == 'y':
        multiplication()
    elif do_again == 'no' or do_again == 'n':
        print("See You Later, Thank You.")
    else:
        again()

multiplication()