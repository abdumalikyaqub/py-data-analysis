import numpy as np 
import math
with open('new_89.csv') as f:
    data = f.readlines()

#Разделить строки на колонки по пробелу
data = [line.strip().split('\t') for line in data]
numbers = [int(line[2]) for line in data]

first_minimax_normalization =[]
second_minimax_normalization =[]
decimal_scaled=[]

#Десятичное масшатибирование.
num_digits = len(str(max(numbers)))
num_pow = pow(10,num_digits)
for number in numbers:
    decimal_scaled.append(number/num_pow)
    
#Минимаксная нормализация
for number in numbers:
    a,b=0,1
    min_number,max_number = min(numbers),max(numbers)
    #1 Формула X=(X- X_min)/(X_max- X_min )
    first_normalization_value = (number - min_number) / (max_number - min_number)
    first_minimax_normalization.append(first_normalization_value)
    #2 Формула X= a+(X- X_min)/(X_max- X_min )*(b-a)
    second_normalization_value =  a + (number - min_number)/(max_number - min_number) * (b - a)
    second_minimax_normalization.append(second_normalization_value)


#Функция вычесление выборочное стандартное отклонение
def sample_std_deviation(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    sample_variance = sum(deviations) / (n - 1)
    sample_std_deviation = math.sqrt(sample_variance)
    return sample_std_deviation


#Нормализация средним (Z-нормализация) x_i=((x_i-X))/σ_i
std =  sample_std_deviation(numbers)
mean = (sum(numbers) /len(numbers) )
z_normalization =[]
for number in numbers:
    z_value = (number - mean)/std
    z_normalization.append(z_value)

from sklearn import preprocessing as pre

normalized_array = pre.minmax_scale(numbers,(0,1))
scale_array = pre.scale(numbers)

#Отношение
k = 10
otn =[]
for i in range(len(numbers)):
   otn.append(numbers[i]/k)


print("\n МинМакс нормализация с использованием Библиотеки")
print(normalized_array[:10])
print("\n2 МинМакс нормализация")
print(second_minimax_normalization[:10]) # [:10] выводит по 10 значений

print("\n Нормализация средним Библиотека")
print(scale_array[:10])

print("\n Нормализация средним")
print(z_normalization[:10])