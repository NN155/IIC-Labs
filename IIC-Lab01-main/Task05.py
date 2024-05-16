'''Створіть програму, яка обчислює факторіал числа, яке вводить користувач.'''
number = int(input("Введіть число: "))
factorial = 1
for i in range(2, number + 1):
    factorial *= i
print(f"{factorial} - факторіал числа {number}")
