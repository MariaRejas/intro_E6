import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re

f = open("Señal EMG Lab1.txt","r")
raw_data = f.readline()  # con f.read() leemos todo el contenido
f.close()

raw_data

## Expresion regular para buscar automaticamente el contenido de un numero dentro de un string
x = re.findall("[0-5][0-9]\d", raw_data)

print(x)

Fs = 1000
Ts=1/Fs

print(f" Fs={Fs} hz\n Ts={Ts} s")
array = np.genfromtxt("./Señal EMG Lab1.txt", delimiter="	",skip_header = 2)
array

M = array[:,-2].shape[0]

n = np.arange(0,M)
t = n*Ts

plt.plot(t, array[:,-2], label="señal")      # graficamos la señal
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.show()

N = 2**10                                     # 10 bits, 0-1023

signal1 = array[:,-2]

signal_fft = np.fft.fft(signal1, N)           # fft magtinud
signal_fft = np.round(np.abs(signal_fft),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
signal_aux = signal_fft/signal_fft.max()     # hallamos el maximo para pasar la magnitud a escala db

with np.errstate(divide='ignore'):
    signal_fft_db = 10*np.log10(signal_aux)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero

F_list = np.linspace(0,Fs/2, N//2)
F = np.round(F_list[np.argmax(signal_fft_db)], 1)   # argmax, encuentra el argumento max en un array

plt.plot(F_list, signal_fft_db)  #10 * np.log10(P / Pref) , decibelios
plt.text(F,0, f"{F}Hz")
plt.grid(linestyle=":")
plt.ylabel("Magnitud (db)")
plt.xlabel("Frecuencias (Hz)")
plt.title("FFT en el decibelios")
plt.xlim([0,200])
#plt.xticks(np.arange(0,200,10))
plt.show()
