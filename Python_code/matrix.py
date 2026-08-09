import array

def multiply_matrices(a, b) -> array:
    # make a size x size result matrix filled with zeros
    result =  [[0]*len(b[0]) for _ in range(len(a))]
    # i chooses the row of matrix A (0 = top row, 1 = bottom row)
    for i in range(len(a)):
        # j chooses the column of matrix B (0 = left column, 1 = right column)
        for j in range(len(b[0])):
            # k moves across row i of matrix A and down column j of matrix B
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

    return result

def create_matrix(rows, cols, name) -> array:
    matrix = []
    # loop through the rows to create the matrix
    for i in range(rows):
        row = []
        # loop through the columns to create the matrix
        for j in range(cols):
            # ask for input and append it to the row
            # added 1 to i and j to make it more user friendly
            value = int(input(f"Enter value for matrix {name} at [{i+1}][{j+1}]: "))
            row.append(value)
        matrix.append(row)
    return matrix


def dimensions(x):
    # removes x so we can define the first character as rows and columns, then splits the string into a list of two elements
    dims = input(x).strip().lower().split('x')
    if len(dims) != 2:
        raise ValueError("Enter dimensions in the format rows x columns, for example 4x3")
    rows = int(dims[0])
    cols = int(dims[1])
    return rows, cols

rows_a, cols_a = dimensions("Enter dimensions for matrix A (eg: 4x3): ")
rows_b, cols_b = dimensions("Enter dimensions for matrix B (eg: 3x1): ")

# checks to see if we can multiply the two matrices together if not it raises an error
if cols_a != rows_b:
    raise ValueError("Incompatible dimensions: matrix A columns must equal matrix B rows")

# create the matrices
matrix_a = create_matrix(rows_a, cols_a, "A")
matrix_b = create_matrix(rows_b, cols_b, "B")

# multiply the matrices
result_matrix = multiply_matrices(matrix_a, matrix_b)

# Display the output
print("Result Matrix:")
for row in result_matrix:
    print(row)