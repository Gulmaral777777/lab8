def max_index(arr):
    return arr.index(max(arr)) + 1  # порядковый номер, начиная с 1

A = list(map(float, input("Введите числа массива A через пробел: ").split()))
B = list(map(float, input("Введите числа массива B через пробел: ").split()))
C = list(map(float, input("Введите числа массива C через пробел: ").split()))

print("Номер максимума A:", max_index(A))
print("Номер максимума B:", max_index(B))
print("Номер максимума C:", max_index(C))