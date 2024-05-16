'''В якому місяці на Netflix зазвичай виходить найбільше серіалів?'''
import pandas as pd

# Створюємо словник 'monthCounter', де ключі - назви місяців, а значення - лічильники для кількості серіалів.
monthCounter = {"January": 0,
                "February": 0,
                "March": 0,
                "April": 0,
                "May": 0,
                "June": 0,
                "July": 0,
                "August": 0,
                "September": 0,
                "October": 0,
                "November": 0,
                "December": 0}
data = pd.read_csv("netflix_titles.csv")
for i in range(len(data)):
    row = data.loc[i]
    date = row["date_added"]

    # Перевіряємо, чи тип дати є строкою.
    if type(date) != str:
        continue
    if row['type'] == "TV Show":
        # Перевіряємо, в якому місяці було додано серіал і оновлюємо відповідний лічильник місяця в словнику.
        for monthCheck in monthCounter.keys():
            if monthCheck in date:
                monthCounter[monthCheck] += 1
# Сортуємо місяці за кількістю серіалів у зворотньому порядку (найбільше - перший місяць).
topMonth = sorted(monthCounter, key=lambda x: -monthCounter[x])
print(f"{topMonth[0]} виходить найбільше серіалів - {monthCounter[topMonth[0]]}")
