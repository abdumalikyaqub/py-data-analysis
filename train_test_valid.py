import random

with open("new_89.csv", 'r') as readcsv:
    DataFromFile = readcsv.read().split('\n')


trainData = []
testData = []
validData = []

lengthData = len(DataFromFile)

# Перемешивание списка
random.shuffle(DataFromFile)

countTest = int(lengthData*0.12)

for data in DataFromFile:
    if countTest > 0:
        testData.append(data)
        countTest -= 1
        DataFromFile.remove(data)

size = lengthData - countTest
subsize = size 
subsubsize = subsize 

for i in range(7):
    start = i * subsize
    end = start + subsize

    for j in range(7):
        substart = start + j * subsubsize
        subend = substart + subsubsize

        if j == i:
            for data in DataFromFile[substart:subend]:
                validData.append(data)

        else:
            for data in DataFromFile[substart:subend]:
                trainData.append(data)

with open('trainingPartThree.csv', 'w') as fileNew:
 for text in trainData:
    fileNew.write(''.join(text)+"\n")

with open('testPartThree.csv', 'w') as fileNew:
 for text in testData:
    fileNew.write(''.join(text)+"\n")

with open('valPartThree.csv', 'w') as fileNew:
 for text in validData:
    fileNew.write(''.join(text)+"\n")

