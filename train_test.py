# file = open('new_89.csv')
# values= file.read().split('\n')
# file.close()

# vib1 = []
# vib2 = []
# vib3 = []
# ob = []
# n = 0

# m = (len(values)//((len(values) * 12)/100))

# for i in range(len(values)):
#     if n==m-1:
#         vib1.append(values[i])
#         n=0
#     else:
#         ob.append(values[i])
#         n=n+1
# for i in range(len(ob)):
#     if n==7:
#         vib3.append(ob[i])
#         n=0
#     else:
#         vib2.append(ob[i])
#         n=n+1

# print("Тестовая выборка")
# for i in range(len(vib1)):
#     print(vib1[i])
# print("\n Тренировочная выборка")
# for i in range(len(vib2)):
#     print(vib2[i])

# print("\n Валидационная выборка")
# for i in range(len(vib3)):
#     print(vib3[i])

# with open ('89_train.csv','w') as file:
#      for txt in vib2:
#         file.write(''.join(txt)+'\n')
# with open ('89_test.csv','w') as file:
#    for txt in vib1:
#          file.write(''.join(txt)+'\n')
# with open ('89_valid.csv','w') as file:
#    for txt in vib3:
#          file.write(''.join(txt)+'\n')
# print("Запись в новые файлы успешна")

import random

with open("new_89.csv", 'r') as readcsv:
    DataFromFile = readcsv.read().split('\n')

trainData = [] # Train data
testData = [] # Test data

lengthData = len(DataFromFile)

countTraining = lengthData * 0.7

# Перемешивание списка
random.shuffle(DataFromFile)

for data in DataFromFile:
    if countTraining > 0:
        trainData.append(data)
        countTraining -= 1
    else:
        testData.append(data)

with open('trainingPartOne.csv', 'w') as fileNew:
 for str_data in trainData:
    fileNew.write(''.join(str_data)+"\n")

with open('testPartOne.csv', 'w') as fileNew:
 for str_data in testData:
    fileNew.write(''.join(str_data)+"\n")


# Check length data


with open("trainingPartThree.csv", 'r') as readcsv:
    DataFromFile = readcsv.read().split('\n')

print(len(DataFromFile))

# import random

# # Ваш список данных
# data = [1, 2, 3, 4, 5]

# # Перемешивание списка
# random.shuffle(data)

# # Вывод перемешанного списка
# print(data)