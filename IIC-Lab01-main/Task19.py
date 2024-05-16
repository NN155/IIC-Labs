'''Напишіть програму, яка генерує випадковий пароль заданої довжини з літер, цифр і спеціальних символів.'''
from random import randint
from string import ascii_letters, digits, punctuation

letters = ascii_letters + digits + punctuation
lenPassword = int(input("Введіть довжину пароля: "))
lst = []
for i in range(lenPassword):
    lst.append(letters[randint(0, len(letters) - 1)])
print(''.join(lst))