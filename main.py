import numpy as np

# Ввод значений x и y
x = np.array([0, 1, 2, 3])
y = np.array([11, 12, 19, 38])

# Ввод матрицы A
A = np.array([
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [8, 4, 2, 1],
    [27, 9, 3, 1]
])

# Ввод матрицы с одним столбцом
B = np.array([[11], [12], [19], [38]])

X = np.array([[1], [0], [0], [11]])


def p(x, c):
    a3, a2, a1, a0 = c[0][0], c[1][0], c[2][0], c[3][0]
    return a3 * x**3 + a2 * x**2 + a1 * x + a0

# Заданные значения x для формулы
x1 = [0, 0.5, 1, 1.5, 2, 2.5, 3]

new_values = [float(p(x, X)) for x in x1]

# Вывод таблицы значений x и y
print("Значения x:", x)
print("Значения y:", y)

# Вывод матрицы A
print("Матрица A:")
print(A)

# Вывод матрицы B (столбец)
print("Матрица B:")
print(B)

# Вывод матрицы X (коэффициенты)
print("Матрица X (коэффициенты a3, a2, a1, a0):")
print(X)

# Вывод таблицы с расчетами для x = 1, 2, 3
print("\nТаблица вычислений по формуле a3*x^3 + a2*x^2 + a1*x + a0:")
print("Значения x:           ", x1)
print("Вычисленные значения: ", new_values)

