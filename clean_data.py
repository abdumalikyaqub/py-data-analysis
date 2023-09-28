import csv
from datetime import datetime

datas = []
# Проверка на дубликатов и на пустоту 
with open('new_89.csv') as f:
    temp = f.readlines()
    for x in temp:
        if len(x) > 0:
            if x not in datas:
                datas.append(x)

# Разделить строки на колонки по пробелу
data = [line.strip().replace('"', '').split('\t') for line in datas]

# Переобразовать данные в нужный формат
date = [datetime.strptime(line[0], '%m-%d-%Y').date() for line in data]
hours = [datetime.strptime(line[1], '%H:%M').time() for line in data]
number1 = [int(line[2]) for line in data]
number2 = [int(line[3]) for line in data]

# Сохранить с правильным форматом 
headers = ['date', 'time', 'number1', 'number2']

with open('new_file.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    # Записываем заголовки столбцов, если файл был пуст
    if file.tell() == 0:
        writer.writerow(headers)
    #writer.writerow(headers)
    for i in range(len(date)):
        writer.writerow([date[i], hours[i].strftime('%H:%M'), number1[i], number2[i]])