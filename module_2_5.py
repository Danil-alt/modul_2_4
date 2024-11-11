def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        if n == 0:
            break
        elif m == 0:
            break
        matrix_ = []
        matrix.append(matrix_)
        for j in range(m):
            matrix_.append(value)
    return matrix


print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))
print(get_matrix(1, 0, 7))
