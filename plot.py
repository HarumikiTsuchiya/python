import matplotlib.pyplot as plt
import numpy as np

# 平均50、分散20の乱数を10万個作成する
#x = np.random.normal(50, 20, 100000)
#left = np.array([1, 2, 3, 4, 5])
#height = np.array([100, 300, 200, 500, 400])
x = np.arange(-100, 100, 0.1)

# 計算式
y = 2 * (x**2)

#plt.plot(left, height)
#plt.plot(y)
# 画像のプロット先の準備
fig = plt.figure()

# ヒストグラムの描画
#plt.hist(x, bins=100, ec='black')

plt.plot(x, y)

# グラフの指定
plt.title("X-Y")
# x方向のラベル
plt.xlabel("x")
# y方向のラベル
plt.ylabel("y")
# グラフの表示範囲(x方向)
#plt.xlim(-50, 150)
# グリッドを表示する
#plt.grid()

# グラフをファイルに保存する
fig.savefig("img.png")