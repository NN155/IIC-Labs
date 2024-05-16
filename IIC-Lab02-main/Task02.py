'''Чи правда, що останніми роками Netflix більше фокусується на серіалах
(TV Show), ніж на фільмах?'''
import pandas as pd

data = pd.read_csv("netflix_titles.csv")

# Ініціалізуємо лічильники для серіалів (TV Show) та фільмів (Movie).
TVShowCounter = 0
movieCounter = 0

# Визначаємо поточний рік та кількість років, яку вважатимемо "останніми роками".
year = 2023
yearRange = 5

for i in range(len(data)):
    row = data.loc[i]

    # Перевіряємо, чи тип проекту є "TV Show" і чи він вийшов протягом останніх 5 років.
    if row["type"] == "TV Show" and row["release_year"] > (year - yearRange):
        TVShowCounter += 1

    # Перевіряємо, чи тип проекту є "Movie" і чи він вийшов протягом останніх 5 років.
    elif row["type"] == "Movie" and row["release_year"] > (year - yearRange):
        movieCounter += 1

# Виводимо кількість фільмів та серіалів, які вийшли протягом останніх 5 років.
print(f'Фільмів за останні 5 років вийшло - {movieCounter}, а серіалів  - {TVShowCounter}')
print(f'Тому відповідь {"ні" if TVShowCounter < movieCounter else "так"}')
