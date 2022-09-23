input = open("C:\Программирование\start_map.txt", "r")
output = open("C:\Программирование\result.txt", "w")
A=[] # Пустой массив
for i in range(6):
    A.append([float(i) for i in input.readline().split()])
output.write("Input: ")
for i in range(6):
    output.write("\n" + str(A[i]))
print(A, "\n")
index_j=0
min = 10000000.1
for j in range(6):
    if A[0][j] < min:        # Нахождение минимального первого элемента в столбцах
        index_j = j          # Номер столбца с мин. элементом
        min = A[0][j]
for i in range(6):
    for k in range(5 - i):    # Сортируем элементы в порядке убывания методом обмена.
        if A[k][index_j] < A[k + 1][index_j]:
            A[k][index_j], A[k + 1][index_j] = A[k + 1][index_j], A[k][index_j]

print(A)
output.write("\n" + "\n" + "Output: ")
for i in range(6):
    output.write("\n" + str(A[i]))
