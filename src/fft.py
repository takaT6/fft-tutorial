import numpy as np
import matplotlib.pyplot as plt 
import japanize_matplotlib

sf = 44100    # サンプリングレート [Hz]
sec = 1.0     # 信号の長さ [s]
dt = 1.0/sf   # サンプリング周期 [s]
A = 1.0       # 振幅
t = np.arange(0, sec, dt) # サンプリング点の生成

y2Hz = A*np.sin(2*np.pi*2.0*t) # 2Hzの正弦波の生成
y8Hz = A*np.sin(2*np.pi*8.0*t) # 8Hzの正弦波の生成

y_combine = y2Hz + y8Hz # 2つを合成

N = sf * int(sec) #データ点数

# 高速フーリエ変換
F = np.fft.fft(y_combine)

# 周波数軸
freq = np.fft.fftfreq(N, d=dt)

# 振幅スペクトル
Amp = np.abs(F / (N / 2))

plt.plot(freq[:20], Amp[:20])
plt.xlabel('周波数[Hz]', fontsize=10)
plt.ylabel('振幅スペクトル', fontsize=10)
plt.show()