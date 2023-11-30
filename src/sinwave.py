import sys
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

sf = 44100  # サンプリング周波数 [Hz]
sec = 1.0     # 信号の長さ [s]
dt = 1/sf   # サンプリング周期 [s]
A = 1.0     # 振幅
f = float(sys.argv[1])    # 周波数 [Hz]
t = np.arange(0, sec, dt) # サンプリング点の生成
y = A*np.sin(2*np.pi*f*t) # 正弦波の生成

plt.plot(t, y, color="b")
plt.xlabel('時間[s]', fontsize=10)
plt.ylabel('振幅', fontsize=10)
plt.show()