#С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. 
#Для тестирования использовать не случайное заполнение, а целенаправленное.
#4.	Формируется матрица F следующим образом: если в Е количество нулевых элементов в нечетных столбцах в области 4 больше, чем количество отрицательных  элементов в четных строках в области 1, то поменять в 
#В симметрично области 4 и 3 местами, иначе В и Е поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: ((F+A)– (K * F) )*AT . 
#Выводятся по мере формирования А, F и все матричные операции последовательно
import random

K_test = 2
N_test = 11
A_test = [
    [1, 2, 3, 4, 5, 4, -9, 8, -1, 5, 3],
    [6, 7, 8, 9, 10, 2, -4, -8, -5, -1, 3],
    [10, 9, 8, 7, 6, 9, -3, 3, 5, -1, -9],
    [5, 4, 3, 2, 1, -5, 2, 7, 3, 8, 0],
    [1, 2, 3, 4, 5, -4, 3, 3, -2, 4, -1],
    [-1, 8, 6, 10, -3, 7, -8, -9, -9, -5, 2],
    [-2, -6, -3, 1, 2, -3, 0, 5, 0, 0, 7],
    [-7, 10, -4, -8, -9, -9, 0, 5, 0, -10, -4],
    [3, 6, -9, 7, 2, -10, 4, 0, 2, -4, 0],
    [10, 9, 9, 5, 8, -8, -8, 0, 10, -7, 1],
    [6, -5, 0, 1, -5, -3, -5, 0, 7, -2, 0]]

print('Использовать тестовые данные или случайные?')
choice = input('Ваш выбор (1 - тестовые данные, 2 - случайные, q-выход): ')

if choice == '1':
    K = K_test
    N = N_test
    A = A_test

if choice == '2':
    K = int(input('Введите K: '))
    N = int(input('Введите N: '))

    if (N < 6):
        print(
            'Ошибка в исходных данных. Длина сторон матрицы А (N,N) должна быть больше 5')
        exit()

    A = []
    for row in range(N):
        cur_row = []
        for col in range(N):
            cur_row.append(random.randint(-10, 10))
        A.append(cur_row)

B, C, D, E = [], [], [], []
n = N // 2  

if N % 2 == 0:
    step = N // 2
else:
    step = N // 2 + 1

for row in range(n):
    row_b, row_c, row_d, row_e = [], [], [], []
    for col in range(n):
        row_e.append(A[row][col])
        row_b.append(A[row][col + step])
        row_d.append(A[row + step][col])
        row_c.append(A[row + step][col + step])
    B.append(row_b)
    C.append(row_c)
    D.append(row_d)
    E.append(row_e)

if choice == 'q':
    exit()


print('Матрица E:')
for row in range(n):
    print(E[row])

print('Матрица B:')
for row in range(n):
    print(B[row])

print('Матрица C:')
for row in range(n):
    print(C[row])

print('Матрица D:')
for row in range(n):
    print(D[row])

print('Матрица A:')
for row in range(N):
    print(A[row])


count_zero_e_4 = 0
for row in range(1, n - 1):
    if n % 2 == 1:
        if row <= n // 2:
            end_col = row
        else:
            end_col = n - row - 1
    else:
        if row < n // 2:
            end_col = row
        else:
            end_col = n - row - 1
    for col in range(0, end_col):
        if col % 2 == 1:
            if E[row][col] < 0:
                count_zero_e_4 += 1  
print(
    f'Количество отрицательных элементов в матрице E в области 4 в нечетных столбцах: {count_zero_e_4}')


count_zero_e_1 = 0
for col in range(1, n - 1):
    if n % 2 == 1:
        if col <= n // 2:
            end_row = col
        else:
            end_row = n - col - 1
    else:
        if col < n // 2:
            end_row = col
        else:
            end_row = n - col - 1
    for row in range(0, end_row):

        if col % 2 == 0:
            if E[row][col] < 0:
                count_zero_e_1 += 1  
print(
    f'Количество нулевых элементов в матрице E в области 1 в четных столбцах: {count_zero_e_1}')

F = []
for row in range(N):
    cur_row = []
    for col in range(N):
        cur_row.append(A[row][col])
    F.append(cur_row)


if count_zero_e_4 > count_zero_e_1:
    
    for col in range(1, n - 1):
        if n % 2 == 1:
            if col <= n // 4:
                end_row = n - col - 1
            else:
                end_row = col
        else:
            if col < n // 4:
                end_row = n - col - 1
            else:
                end_row = col
        for row in range(n - 1, end_row, -1):
            temp = B[row][col]
            B[row][col] = B[col][row]
            B[col][row] = temp
    print('Матрица B после изменений:')
    for row in range(n):
        print(B[row])
    
    if N % 2 == 0:
        step = N // 2
    else:
        step = N // 2 + 1
    for row in range(n):
        for col in range(n):
            F[row][col] = E[row][col]
            F[row][col + step] = B[row][col]
            F[row + step][col] = D[row][col]
            F[row + step][col + step] = C[row][col]

else:  
    
    if N % 2 == 0:
        step = N // 2
    else:
        step = N // 2 + 1
    for row in range(n):
        for col in range(n):
            F[row][col] = B[row][col]
            F[row][col + step] = E[row][col]
            F[row + step][col] = D[row][col]
            F[row + step][col + step] = C[row][col]

print('Матрица F:')
for row in range(N):
    print(F[row])
#-------------------------------------------------


#1 Транспонированная А
A_transpose = []
for row in range(N):
    A_transpose_row = []
    for col in range(N):
        A_transpose_row.append(A[col][row])
    A_transpose.append(A_transpose_row)
print('Транспонированная матрица A: ')
for row in range(N):
    print(A_transpose[row])


#2
F_sum_A = []
for row in range(N):
    cur_row = []
    for col in range(N):
        cur_row.append(0)
    F_sum_A.append(cur_row)

for row in range(N):
    for col in range(N):
        F_sum_A[row][col] = F[row][col] + A[row][col]
print('Сумма F+A: ')
for row in range(N):
    print(F_sum_A[row])

#3
F_mul_K = []  
for row in range(N):
    cur_row = []
    for col in range(N):
        cur_row.append(0)
    F_mul_K.append(
        cur_row)  

for row in range(N):
    for col in range(N):
        F_mul_K[row][col] = K * F[row][col]

print('Умножение F на константу: ')
for row in range(N):
    print(F_mul_K[row])

#4
F_sum_a_div_F_mul_K = []
for row in range(N):
    cur_row = []
    for col in range(N):
        cur_row.append(0)
    F_sum_a_div_F_mul_K.append(cur_row)
for row in range(N):
    for col in range(N):
        F_sum_a_div_F_mul_K[row][col] = F_sum_A[row][col] - F_mul_K[row][col]
print('Сумма F_A - F_mul_K: ')
for row in range(N):
    print(F_sum_a_div_F_mul_K[row])


#5
At_mul_res = []
for row in range(N):
    F_row = []
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += F_sum_a_div_F_mul_K[row][j] * A_transpose[j][i]
        F_row.append(sum)
    At_mul_res.append(F_row)

print('Результат: ')
for row in range(N):
    print(At_mul_res[row])
