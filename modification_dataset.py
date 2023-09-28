import re
import csv

# Определение шаблона для соответствия строке
pattern = r'^\d{2}-\d{2}-\d{4}\s\d{2}:\d{2}\s\d+\s\d+$'

# Открытие CSV файла для чтения
with open('89.csv', 'r') as infile:
    # Чтение строк из файла
    reader = csv.reader(infile, delimiter='\t')
    # Открытие нового CSV файла для записи
    with open('new_89.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile, delimiter='\t')
        # Обход строк и проверка соответствия шаблону
        for row in reader:
            # Объединение строк в одну
            row_str = ''.join(row)
            # Проверка соответствия шаблону
            if re.match(pattern, row_str):
                # Если строка соответствует шаблону, то запись в новый файл
                n_row = row_str.split()
                writer.writerow(n_row)
            else:
                regex = r"(\d{2})-\D*(\d{2})-\D*(\d{4})\D+(\d{2}):(\d{2})\D+(\d+)\D+(\d+)"
                # поиск совпадений в исходной строке
                matches = re.findall(regex, row_str)

                # если найдено несколько совпадений, то берем первое
                if len(matches) > 0:
                    match = matches[0]
                # формирование новой строки с нужным форматом
                new_s = f'{match[0]}-{match[1]}-{match[2]}\t{match[3]}:{match[4]}\t{match[5]}\t{match[6]}'
                cleaned_row = new_s.split()
                writer.writerow(cleaned_row)
       