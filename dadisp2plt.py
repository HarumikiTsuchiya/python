import dadisp
import matplotlib.pyplot as plt

#ファイル名を指定してインスタンス作成
a=dadisp.DadispConv('F001')

#numpyリスト変換実行
b=a.convnp(COEF=True,OFFSET=True)
#print(b)

c=dadisp.HeaderRead('F001')
d=c.conv('SERIES')
#print(d)

#インスタンス削除
del(a)


fig = plt.figure(figsize = (8,6))

#plt.xlabel('Time')
#plt.ylabel('wind speed(m/s)')

ch=[0,1,2,3]
for i in ch:
    plt.plot(range(len(b)),b[:,i], label=d[i])


#タイトル
#plt.title("Wind Speed")
#凡例表示
plt.legend()
#グリッド表示
plt.grid()
#45度回転
#plt.xticks(rotation=45)

#画像保存
fig.savefig("dadisp2plt.png")
