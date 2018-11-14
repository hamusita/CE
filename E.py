import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv_in = pd.read_csv(filepath_or_buffer="/Users/hamusita/Desktop/授業/コンピューター計測/課題2/t.csv", sep='\n')

data = list(csv_in.iloc[0:250, 0])

num = 7
b = np.ones(num) / num

F = np.fft.fft(data)

y = np.convolve(data, b, mode='same')
x = [i for i in range(0,250)]

N = 250
dt = 0.01          # サンプリング間隔
t = np.arange(0, N*dt, dt)

fig, ax = plt.subplots(nrows=3, sharex=True, figsize=(6,6))
ax[0].plot(x, data, label='元データ')
ax[1].plot(x, y,'r',label='平滑化')
ax[2].plot(F, , label='FFT')