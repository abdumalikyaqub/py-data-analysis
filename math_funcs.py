with open('new_89.csv') as f:
    data = f.readlines()

# Разделить строки на колонки по пробелу
data = [line.strip().split('\t') for line in data]

years = [int(line[0].split('-')[-1]) for line in data]

hours = [int(line[1].split(':')[0]) for line in data]

# Преобразовать данные в нужный формат
data = [[float(num.strip('"')) for num in line[2:]] for line in data]

print(f"Years: Mean={sum(years) / len(years):.2f}, Mode={max(set(years), key=years.count):.0f}, Median={sorted(years)[len(years) // 2]:.0f}")
print(f"Hours: Mean={sum(hours) / len(hours):.2f}, Mode={max(set(hours), key=hours.count):.0f}, Median={sorted(hours)[len(hours) // 2]:.0f}")

# Вычислить среднее значение, моду и медиану для каждой колонки
for i in range(len(data[0])):
    column = [row[i] for row in data]
    mean = sum(column) / len(column)
    mode = max(set(column), key=column.count)
    n = len(column)
    sorted_column = sorted(column)
    if n % 2 == 0:
        median = (sorted_column[n // 2 - 1] + sorted_column[n // 2]) / 2
    else:
        median = sorted_column[n // 2]
    print(f"Column {i+3}: Mean={mean:.2f}, Mode={mode:.2f}, Median={median:.2f}")