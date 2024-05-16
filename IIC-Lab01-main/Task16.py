'''Напишіть програму, яка визначає, чи є введене слово анаграмою іншого слова.'''
word1 = input("Введіть перше слово: ")
word2 = input("Введіть друге слово: ")
lst = list(word2.lower())
myBool = False
if len(word1) == len(word2):
    for i in word1.lower():
        if i in lst:
            lst.remove(i)
    if len(lst) == 0:
        myBool = True
print(f'{word1} {"є" if myBool else "не є"} анаграмою слова {word2}')