'''Напишіть програму для знаходження найбільшого числа серед трьох чисел, які вводить користувач.'''
numbers = list(map(int, input("Введіть 3 числа: ").split()))
print(f"{max(numbers)} - найбільше серед цих чисел:", *numbers)

# maxValue = numbers[0]
# for i in numbers:
#     if maxValue < i:
#         maxValue = i
# print(maxValue)