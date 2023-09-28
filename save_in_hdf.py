import pandas as pd

file = open(r"new_89.csv")
text = file.read()
file.close()
text = text.split('\n')
data = []
for i in range(len(text)-1):
    data.append(text[i].replace('"','').split('\t'))
df = pd.DataFrame(data,columns=['date','time','number1','number2'])
for i in range(len(df)):
    df.at[i, 'number2'] = str(df.at[i, 'number2']) + str(i)
meta_col = 'number2'
df[meta_col] = df[meta_col] + ' _meta_information'
filename = r"fileHdf.hdf5"
df.to_hdf(filename, key='data')
df = pd.read_hdf(filename, 'data')
print(df[:20])