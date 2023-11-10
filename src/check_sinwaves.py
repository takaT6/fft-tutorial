import numpy as np
import matplotlib.pyplot as plt 
import japanize_matplotlib

sf = 44100    # サンプリングレート [Hz]
sec = 1.0    # 信号の長さ [s]
dt = 1.0/sf   # サンプリング周期 [s]
A = 1.0      # 振幅
t = np.arange(0, sec, dt) # サンプリング点の生成

y2Hz = A*np.sin(2*np.pi*2.0*t) # 2Hzの正弦波の生成
y8Hz = A*np.sin(2*np.pi*8.0*t) # 8Hzの正弦波の生成

plt.plot(t, y2Hz, color="b") # y-tグラフのプロット
plt.plot(t, y8Hz, color="r") # y-tグラフのプロット
plt.xlabel('時間[s]', fontsize=10)
plt.ylabel('振幅', fontsize=10)
plt.show()