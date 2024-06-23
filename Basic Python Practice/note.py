
# Function, List, List Comprehension Practice.

import random

# Step 1: Ask the user for two integers n and m
# n = int(input("Enter the value of n: "))
# m = int(input("Enter the value of m (where m > n): "))

# # Check if m > n
if m <= n:
    print("The value of m must be greater than n.")
else:
    # Step 2: Create a list x of size n
    x = [0] * n
    
    # Step 3: Populate the list with n random integers in the range 1 through m
    for i in range(n):
        x[i] = random.randint(1, m)
    
    # Print the resulting list
    print("The list x with random integers is:", x)


# Ask the user for three integer n and m and k, where k>m*n.
# Create a two dimensional table (list of lists) x of size n*m. Populate the list with n*m unique random
# integers in the range 1through k.

def dimensional(n, m, k):
    row = []
    column = []
    numberReference = set()
    randomNumber = random.randint(1, k)
    for i in range(m):
        row = [0] * n
        column.append(row)
    
    for i in range(len(row)):
        if randomNumber not in numberReference:
            row[i] = randomNumber
            randomNumber = random.randint(1, k)
        else:
            randomNumber = random.randint(1, k)
    return column

def dimensional(n, m, k):
    if k < (n * m):
        raise ValueError("k must be greater than n * m to ensure unique numbers")
    
    # Create a two-dimensional list with m rows and n columns
    column = []
    for i in range(m):
        row = [0] * n
        column.append(row)
    
    # Generate a set of unique random numbers in the range 1 through k
    number_reference = set()
    while len(number_reference) < n * m:
        number_reference.add(random.randint(1, k))
    
    unique_numbers = list(number_reference)
    
    # Populate the 2D list with unique random numbers
    idx = 0
    for i in range(m):
        for j in range(n):
            column[i][j] = unique_numbers[idx]
            idx += 1
    
    return column


# n = int(input("Input integer n: "))
# m = int(input("Input integer m: "))
# k = int(input("Input integer k: "))
# print(dimensional(n, m, k))

# row = []
# column = []

# for i in range(2):
#     row = [0] * 3
#     column.append(row)
# print(column)

# Problem Write a function get_row(x,i) which takes a square matrix (=table=list of lists) and returns a list
# containing the ith row of matrix X.
x = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]
def get_row(x, i):
    result = []
    for j in range(len(x)):
        result.append(x[i][j])
    return result
    # return x[i]
        


# print(get_row(x, 2))

# Problem Write a function get_col(x,i) which takes a square matrix (=table=list of lists) and returns a list
# containing the ith column of matrix X.

def get_col(x, i):
    res = []
    for j in range(len(x)):
        res.append(x[j][i])
    return res
# print(get_col(x, 1))

# Problem Write a function to calculate and return the sum of all the elements on the “main diagonal” of the
# square two dimensional list x passed to it as an argument. This is the diagonal going from the upper left
# to the bottom right.

def diagonal_sum(matrix):
    sum = 0
    for index in range(len(matrix)):
        sum += matrix[index][index]
    return sum
# print(diagonal_sum(x))

a = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]
def opposite_Diagonal_sum(matrix):
    result = 0
    # (0, 2)
    # (1, 1)
    # (2, 0)
    for index in range(len(matrix)):
        print("The number added will be: " + str(matrix[index][len(matrix) - 1 - index]))
        result += matrix[index][len(matrix) - 1 - index]
    return result
# print(opposite_Diagonal_sum(a))

# Problem Write a function diag_diff(x,i) which takes a square matrix (=table=list of lists) and the difference of
# two main diagonals of matrix X. In other words, let d1 be the diagonal of X from upper left to bottom
# right, and d2 to be the diagonal from upper right to lower left. The function returns d1-d2. Use list
# comprehensions.

def diag_diff(x, i):
    d1 = [sum(x[i][i]) for j in range(len(x))]
    d2 = [sum(x[i][len(i) - i - 1]) for j in range(x)]
    return d1 - d2


def make_int(x: str) -> list:
    return [int(digit) for digit in x]

# print(make_int("123456789"))

# Problem Write a function int_add(x,y) that takes two “integers” as represented above, and returns their sum.
# Note that these “integers” needn’t be the same size. You can simplify your program by padding the shorter one with
# zeros (on the left).
# Note as well, there might be a final carry that will increase the answer by one digit more than the addends
def int_add(x, y):
    xDigit = make_int(x) # [1, 2, 3]
    yDigit = make_int(y) # [4, 5]

    lenX_Digit = len(xDigit)
    lenY_Digit = len(yDigit)

    if lenY_Digit < lenX_Digit:
        # [0] * 1 + [4, 5]
        # [0, 4, 5] 
        yDigit = [0] * (lenX_Digit - lenY_Digit) + yDigit
        # This creates a new list of the needed padding and concate the original to the list.
    elif lenY_Digit > lenX_Digit:
        xDigit = [0] * (lenY_Digit - lenX_Digit) + xDigit

    carry = 0
    result = [0] * len(x)
    # Addition
    for digits in range(len(xDigit) - 1, -1, -1):
        # [1, 2, 3] -> X
        # [0, 4, 5] -> Y

        # [3, 7, 8]
        # [2, 6, 3]
        
        currentSum = xDigit[digits] + yDigit[digits] + carry
        if currentSum >= 10:
            carry = 1
            result[digits] = currentSum - 10
        else:
            carry = 0
            result[digits] = currentSum
    
    if carry > 0:
        result = [carry] + result
    return result


# print(int_add(x = "123", y = "45"))
# print(int_add(x = "378", y = '263'))

matrixA = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrixB = [
    [3, 4, 5],
    [6, 7, 8],
    [9, 10, 11]
]

def matrix_add(x, y):
    resultMatrix = []
    for i in range(len(x)):
        resultMatrix.append([0] * len(x))
    
    if len(x) == len(y):
        for index in range(len(x)):
            for j in range(len(y)):
                resultMatrix[index][j] = x[index][j] + y[index][j]
    return resultMatrix

print(matrix_add(matrixA, matrixB))



