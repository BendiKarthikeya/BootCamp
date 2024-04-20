class Matrix:
    def __init__(self, A):
        self.A = A

    def add(self, other):
        new_matrix = []
        for i in range(len(self.A)):
            row = []
            for j in range(len(self.A[0])):
                row.append(self.A[i][j] + other.A[i][j])
            new_matrix.append(row)
        return new_matrix

    def transpose(self):
        transpose_matrix = []
        for i in range(len(self.A[0])):
            row = []
            for j in range(len(self.A)):
                row.append(self.A[j][i])
            transpose_matrix.append(row)
        return transpose_matrix

    def multiply(self, other):
        if len(self.A[0]) != len(other.A):
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication")

        result_matrix = []
        for i in range(len(self.A)):
            row = []
            for j in range(len(other.A[0])):
                element = 0
                for k in range(len(other.A)):
                    element += self.A[i][k] * other.A[k][j]
                row.append(element)
            result_matrix.append(row)
        return result_matrix

# Example usage:
matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])

result_matrix_addition = matrix1.add(matrix2)
print("Matrix Addition:")
for row in result_matrix_addition:
    print(row)

transpose_matrix = matrix1.transpose()
print("Transpose Matrix:")
for row in transpose_matrix:
    print(row)

result_matrix_multiplication = matrix1.multiply(matrix2)
print("Matrix Multiplication:")
for row in result_matrix_multiplication:
    print(row)
