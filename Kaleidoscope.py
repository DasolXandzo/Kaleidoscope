# Генерация цифрового калейдоскопа
from random import randint
print("Введите целое число (половина стороны желаемого квадрата): ")
x = int(input())
matrix = []
for _ in range(x):
    prime = [randint(0, 9) for i in range(x)]
    prime1 = prime[::-1]
    matrix.append(prime)
    matrix.append(prime1)
z = 0
for _ in range(x):
    print(*matrix[z], *matrix[z + 1])
    z += 2
for _ in range(x):
    print(*matrix[z-2], *matrix[z-1])
    z -= 2
