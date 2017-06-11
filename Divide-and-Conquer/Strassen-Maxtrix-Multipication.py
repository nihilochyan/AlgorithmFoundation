"""
Square Matrix Multiplication:
Cij = sigma(1,n){Aik * Bkj}
"""

from random import choice


def generate_matrix(n):
    matrix = [[choice(range(-10, 10)) for j in range(n)] for i in range(n)]
    return matrix

matrix1 = generate_matrix(2)
matrix2 = generate_matrix(2)
for i in matrix1:
    print(i)
print()
for i in matrix2:
    print(i)


def square_matrix_multiply(a, b):
    """
    SQUARE-MATRIX-MULTIPLY(A,B)
    :param a: matrix left
    :param b: matrix right
    :return: product result
    """
    n = len(a)
    matrix = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(n):
                sum = sum + a[i][k]*b[k][j]
            matrix[i].append(sum)
    return matrix

print()
c = square_matrix_multiply(matrix1, matrix2)
for i in c:
    print(i)


# http://blog.csdn.net/shaungyezhai/article/details/52229500
def strassen_maxtrix_multipication(a, b):
    """
    :param a: Martrix
    :param b: Martrix
    :return: list of result
    """
    def matrixproductmask(mat_a, mat_b):
        if mat_a.row == 1:
            c11 = [[mat_a.mat_list[mat_a.row_list[0]][mat_a.col_list[0]] *
                    mat_b.mat_list[mat_b.row_list[0]][mat_b.col_list[0]]]]
            return Martrix(c11)
        else:
            mat_a11 = mat_a.divide('11')
            mat_a12 = mat_a.divide('12')
            mat_a21 = mat_a.divide('21')
            mat_a22 = mat_a.divide('22')
            mat_b11 = mat_b.divide('11')
            mat_b12 = mat_b.divide('12')
            mat_b21 = mat_b.divide('21')
            mat_b22 = mat_b.divide('22')

            s1 = mat_b12 - mat_b22
            s2 = mat_a11 + mat_a12
            s3 = mat_a21 + mat_a22
            s4 = mat_b21 - mat_b11
            s5 = mat_a11 + mat_a22
            s6 = mat_b11 + mat_b22
            s7 = mat_a12 - mat_a22
            s8 = mat_b21 + mat_b22
            s9 = mat_a11 - mat_a21
            s10 = mat_b11 + mat_b12

            p1 = matrixproductmask(mat_a11, s1)
            p2 = matrixproductmask(s2, mat_b22)
            p3 = matrixproductmask(s3, mat_b11)
            p4 = matrixproductmask(mat_a22, s4)
            p5 = matrixproductmask(s5, s6)
            p6 = matrixproductmask(s7, s8)
            p7 = matrixproductmask(s9, s10)

            c11 = (p5 + p4 - p2 + p6)
            c12 = (p1 + p2)
            c21 = (p3 + p4)
            c22 = (p5 + p1 - p3 - p7)

            return matrixmerge(c11, c12, c21, c22)

    mat_a = Martrix(a)
    mat_b = Martrix(b)
    product = matrixproductmask(mat_a, mat_b)
    return product.mat_list


def matrixmerge(c11, c12, c21, c22):
    mat_list = []
    for i in c11.row_list:
        mat_list.append(c11.mat_list[i] + c12.mat_list[i])
    for i in c21.row_list:
        mat_list.append(c21.mat_list[i] + c22.mat_list[i])
    return Martrix(mat_list)


class Martrix(object):
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], list):
            self.mat_list = args[0]
            self.row = len(args[0])
            self.col = len(args[0][0])
            self.row_list = range(self.row)
            self.col_list = range(self.col)

    def __add__(self, mat2):
        mat_list = [
            [self.mat_list[self.row_list[i]][self.col_list[j]] + mat2.mat_list[mat2.row_list[i]][mat2.col_list[j]]
             for j in range(self.col)] for i in range(self.row)]
        return Martrix(mat_list)

    def __sub__(self, mat2):
        mat_list = [
            [self.mat_list[self.row_list[i]][self.col_list[j]] - mat2.mat_list[mat2.row_list[i]][mat2.col_list[j]]
             for j in range(self.col)] for i in range(self.row)]
        return Martrix(mat_list)

    def divide(self, block):
        result = Martrix()
        result.mat_list = self.mat_list
        result.row = int(self.row / 2)
        result.col = int(self.col / 2)
        dic = {'11': [self.row_list[:result.row], self.col_list[:result.col]],
               '12': [self.row_list[:result.row], self.col_list[result.col:]],
               '21': [self.row_list[result.row:], self.col_list[:result.col]],
               '22': [self.row_list[result.row:], self.col_list[result.col:]]}
        result.row_list = dic[block][0]
        result.col_list = dic[block][1]
        return result

print()
c = strassen_maxtrix_multipication(matrix1, matrix2)
for i in c:
    print(i)