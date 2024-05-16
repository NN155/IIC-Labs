'''Напишіть програму, яка знаходить кількість голосних літер у слові, яке вводить користувач.'''
word = input("Введіть слово: ")
count = 0
letters = "уеїіаоєяию"
for i in word.lower():
    if i in letters:
        count += 1
print(f"{count} - голосних літер в слові {word}")
