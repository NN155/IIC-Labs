'''Реалізуйте калькулятор, який виконує операції додавання, віднімання, множення і ділення.'''
number1 = float(input("Введіть перше число: "))
operation = input("Ведіть операцію +, -, *, /: ")
number2 = float(input("Введіть друге число: "))
match operation:
    case '+':
        print(f"{number1} + {number2} = {number1 + number2}")
    case '-':
        print(f"{number1} - {number2} = {number1 - number2}")
    case '*':
        print(f"{number1} * {number2} = {number1 * number2}")
    case '/':
        print(f"{number1} / {number2} = {number1 / number2}")
    case nonCorrectOperation:
        print(f"{nonCorrectOperation} - не коректна операція")
