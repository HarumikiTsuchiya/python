import pandas as pd
import matplotlib.pyplot as plt
from dadisp2csv import HeaderRead 

filename = 'F001'

plt_ch=['CH_1','CH_2','CH_3']

#ヘッダ読み込み
header=HeaderRead(filename)
DATE = header.conv('DATE')
#print(DATE)
TIME = header.conv('TIME')
#print(TIME)
#plt_ch = header.conv('SERIES')

#df = pd.read_csv('dat003.csv', names=['date','ch0', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6'])
df = pd.read_csv(filename + '.csv')

#print(df)

fig = plt.figure()

#plt.plot(range(len(df)),df['ch0'])

for i in plt_ch:
    plt.plot(range(len(df)),df[i], label=i)
    
#plt.plot(range(len(df)),df['CH_1'], label="CH_1")
#plt.plot(range(len(df)),df['CH_2'], label="CH_2")

#凡例表示
plt.legend()
#グリッド表示
plt.grid()
plt.title(DATE + TIME)

#画像保存
fig.savefig("F001.png")

