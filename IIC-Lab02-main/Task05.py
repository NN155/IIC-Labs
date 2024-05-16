'''Визначте 5 найбільш популярних жанрів на Netflix та побудуйте
відповідну кругову діаграму їх розподілу.'''
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("netflix_titles.csv")
# Створюється порожній словник genreDict, який буде використовуватися для підрахунку кількості проектів за телевізійним рейтингом.
genreDict = {}
for i in range(len(data)):
    row = data.loc[i]
    genres = row["listed_in"]
    # Перевірка, чи є жанр рядком (строкою).
    # Якщо жанр не є строкою (наприклад, він може бути NaN або іншого типу), то цей рядок ігнорується, і програма переходить до наступного рядка.
    if type(genres) != str:
        continue

    # Розділяємо жанри, які можуть бути перераховані через кому.
    for genre in genres.split(","):

        # Враховуємо, що після розділу може виникнути пустий рядок, тому перевіряємо на нього.
        if genre:
            genre = genre.strip()
            # Метод setdefault вертає значення під ключем 'genre'. Якщо ключ 'genre' не існує, він його створює і присвоює йому значення 0.
            genreDict[genre] = genreDict.setdefault(genre, 0) + 1

genre = pd.Series(genreDict)
genre = genre.sort_values(ascending=False)
genre.head(5).plot(kind='pie')

# Ця команда виводить створену кругову діаграму на екран користувача.
plt.show()

