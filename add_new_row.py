import pandas as pd
from datetime import datetime

# читаем CSV-файл в DataFrame
df = pd.read_csv('new_file.csv')

# создаем новый столбец "дни недели" на основе столбца "date"
df['week'] = pd.to_datetime(df['date']).apply(lambda x: x.strftime('%A')).replace({
    'Monday': 'Понедельник',
    'Tuesday': 'Вторник',
    'Wednesday': 'Среда',
    'Thursday': 'Четверг',
    'Friday': 'Пятница',
    'Saturday': 'Суббота',
    'Sunday': 'Воскресенье'
})

# сохраняем DataFrame в CSV-файл
df.to_csv('example_with_new_column.csv', index=False)
print(df)