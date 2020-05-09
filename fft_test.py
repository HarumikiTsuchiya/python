import matplotlib.pyplot as plt
import numpy as np

N=4096
dt = 0.0001
t=np.arange(0,N*dt,dt)
freq=np.linspace(0,1.0/dt,N)
omega=2*np.pi*100
fn=1/dt/2

y=0.8*np.sin(omega*t)+0.6*np.cos(2*omega*t)

F=np.fft.fft(y)/(N/2)

# 画像のプロット先の準備
fig = plt.figure()

#plt.plot(t, y)
plt.plot(freq,np.abs(F))

# グラフの指定
plt.title("X-Y")
# x方向のラベル
plt.xlabel("x")
# y方向のラベル\
plt.ylabel("y")
# グラフの表示範囲(x方向)
plt.xlim(0, fn)
# グリッドを表示する
#plt.grid()

# グラフをファイルに保存する
fig.savefig("fft_test.png")