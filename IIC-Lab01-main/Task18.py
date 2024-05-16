'''Розробіть програму для знаходження середнього значення списку чисел.'''
numbers = list(map(float, input("Введіть декілька чисел: ").split()))
print(f"{sum(numbers) / len(numbers)} - середнє значення списку {numbers}")
