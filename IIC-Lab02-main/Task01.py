'''Побудуйте стовпчикову діаграму розподілу кількості проектів за
телевізійним рейтингом (TV-MA, TV-14, TV-PG тощо).'''
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("netflix_titles.csv")
# Створюється порожній словник ratingDict, який буде використовуватися для підрахунку кількості проектів за телевізійним рейтингом.
ratingDict = {}
for i in range(len(data)):
    row = data.loc[i]
    rating = row["rating"]
    # Перевірка, чи є рейтинг рядком (строкою).
    # Якщо рейтинг не є строкою (наприклад, він може бути NaN або іншого типу), то цей рядок ігнорується, і програма переходить до наступного рядка.
    if type(rating) != str:
        continue
    # Перевірка, чи починається рейтинг зі слова "TV". Це вказує на те, що це телевізійний рейтинг.
    if rating[:2] == "TV":
        # Метод setdefault вертає значення під ключем 'rating'. Якщо ключ 'rating' не існує, він його створює і присвоює йому значення 0.
        ratingDict[rating] = ratingDict.setdefault(rating, 0) + 1

rating = pd.Series(ratingDict)
rating.plot(kind='bar')
# Ця команда виводить створену стовпчикову діаграму на екран користувача.
plt.show()
