class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __add__(self, other):
        result = [[self.mat[i][j] + other.mat[i][j] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def __mul__(self, other):
        result = [[sum(self.mat[i][k] * other.mat[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
        return Matrix(result)

    def transpose(self):
        result = [[self.mat[j][i] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def __str__(self):
        return "\n".join(str(row) for row in self.mat)

# Test
m1 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
m2 = Matrix([[9,8,7],[6,5,4],[3,2,1]])

print("Addition:\n", m1 + m2)
print("Multiplication:\n", m1 * m2)
print("Transpose of first matrix:\n", m1.transpose())
