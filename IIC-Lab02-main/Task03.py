'''Визначте, яка країна випустила найбільше проектів на Netflix у 2023
році. А яка найменше?'''
import pandas as pd

# netflix_titles.csv файл 2021 року.
# Визначаємо цільовий рік, за який аналізуємо дані.
year = 2021
data = pd.read_csv("netflix_titles.csv")
# Створюємо порожній словник 'countryCount' для підрахунку кількості проектів кожної країни.
countryCount = {}
for i in range(len(data)):
    row = data.loc[i]

    # Перевіряємо, чи рік випуску проекту відповідає цільовому року.
    if row["release_year"] == year:
        countries = row["country"]

        # Перевіряємо, чи рік випуску проекту відповідає цільовому року.
        if type(countries) != str:
            continue

        # Розділяємо країни, які можуть бути перераховані через кому.
        for country in countries.split(","):

            # Враховуємо, що після розділу може виникнути пустий рядок, тому перевіряємо на нього.
            if country:
                country = country.strip()
                # Метод setdefault вертає значення під ключем 'country'. Якщо ключ 'country' не існує, він його створює і присвоює йому значення 0.
                countryCount[country] = countryCount.setdefault(country, 0) + 1

# Сортуємо країни за кількістю проектів у зворотньому порядку (найбільше - перше).
topCountries = sorted(countryCount, key=lambda x: -countryCount[x])

print(f"{topCountries[0]} найбільше випустила проектів у {year} році - {countryCount[topCountries[0]]}, а найменше {topCountries[-1]} - {countryCount[topCountries[-1]]}")