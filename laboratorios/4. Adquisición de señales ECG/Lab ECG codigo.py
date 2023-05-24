import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re

#Abrimos los archivos txt
f1 = open("Lab4_Basal.txt","r")
raw_data1 = f1.readline()  # con f.read() leemos todo el contenido
f1.close()

f2 = open("Lab4_Respiracion.txt","r")
raw_data2 = f2.readline()  # con f.read() leemos todo el contenido
f2.close()

f3 = open("Lab4_RespiracionV2.txt","r")
raw_data3 = f3.readline()  # con f.read() leemos todo el contenido
f3.close()

f4 = open("Lab4_PostEjercicio.txt","r")
raw_data4 = f4.readline()  # con f.read() leemos todo el contenido
f4.close()

f5 = open("Lab4_SimuEjercicio.txt","r")
raw_data5 = f5.readline()  # con f.read() leemos todo el contenido
f5.close()

## Expresion regular para buscar automaticamente el contenido de un numero dentro de un string
x1 = re.findall("[0-5][0-9]\d", raw_data1)

x2 = re.findall("[0-5][0-9]\d", raw_data2)

x3 = re.findall("[0-5][0-9]\d", raw_data3)

x4 = re.findall("[0-5][0-9]\d", raw_data4)

x5 = re.findall("[0-5][0-9]\d", raw_data5)

Fs = 1000  #Obtenido de bitalino
Ts=1/Fs

print(f" Fs={Fs} hz\n Ts={Ts} s")

#Lectura y guardado de archivos

array1 = np.genfromtxt("./Lab4_Basal.txt", delimiter="	",skip_header = 2)
array2 = np.genfromtxt("./Lab4_Respiracion.txt", delimiter="	",skip_header = 2)
array3 = np.genfromtxt("./Lab4_RespiracionV2.txt", delimiter="	",skip_header = 2)
array4 = np.genfromtxt("./Lab4_PostEjercicio.txt", delimiter="	",skip_header = 2)
array5 = np.genfromtxt("./Lab4_SimuEjercicio.txt", delimiter="	",skip_header = 2)

M1 = array1[:,-2].shape[0]
n1 = np.arange(0,M1)

M2 = array2[:,-2].shape[0]
n2 = np.arange(0,M2)

M3 = array3[:,-2].shape[0]
n3 = np.arange(0,M3)

M4 = array4[:,-2].shape[0]
n4 = np.arange(0,M4)

M5 = array5[:,-2].shape[0]
n5 = np.arange(0,M5)

#Obtencio de matrices de tiempo

t1=34*1000
t2=35*1000

t_1 = n1*Ts
T1=t_1[t1:t2] #Tiempo

t_2 = n2*Ts
T2=t_2[t1:t2] #Tiempo
T2_1=t_2[40000:45000]

t3 = n3*Ts
T3=t3[t1:t2] #Tiempo

t4 = n4*Ts
T4=t4[t1:t2] #Tiempo

t5 = n5*Ts
T5_1=t5[:10000]
T5=t5[t1:t2] #Tiempo


X1=array1[:,-2] #Toda la señal
x1=array1[t1:t2,-2] #Conjunto de datos a mostrar segun tiempo

X2=array2[:,-2] #Toda la señal
x2=array2[t1:t2,-2] #Conjunto de datos a mostrar segun tiempo
x2_1=array2[40000:45000,-2]

X3=array3[:,-2] #Toda la señal
x3=array3[t1:t2,-2] #Conjunto de datos a mostrar segun tiempo

X4=array4[:,-2] #Toda la señal
x4=array4[t1:t2,-2] #Conjunto de datos a mostrar segun tiempo

X5=array5[:10000,-2] #Toda la señal
x5=array5[t1:t2,-2] #Conjunto de datos a mostrar segun tiempo

#Ploteo de señales

plt.plot(t_1,X1)
plt.title("Señal basal")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()

plt.plot(T1,x1)
plt.title("Señal basal acotada")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()

plt.plot(t_2,X2)
plt.title("Señal Respiración")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()

plt.plot(T2_1,x2_1)
plt.title("Señal Respiración parte basal")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()

plt.plot(T2,x2)
plt.title("Señal Respiración acotada")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()

plt.plot(t3,X3)
plt.title("Señal Respiración 2")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()

plt.plot(T3,x3)
plt.title("Señal Respiración 2 acotada")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.show()

plt.plot(t4,X4)
plt.title("Post ejercicio")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.show()

plt.plot(T4,x4)
plt.title("Post ejercicio acotada")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()

plt.plot(T5_1,X5)
plt.title("Simulación de ejercicio")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()

plt.plot(T5,x5)
plt.title("Simulación de ejercicio acotada")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()

plt.plot(T3,x3,label="señal reposo")     # graficamos la señal segun tiempo acotado
plt.plot(T4,x4,label="señal postejercicio")
plt.title("Comparación de señales")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.show()

#Ploteo de respuesta en frecuencia
N = 2**10                                     # 10 bits, 0-1023

# Para array1
signal1 = array1[:,-2]

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
plt.title("FFT en el decibelios para señal basal")
plt.xlim([0,200])
#plt.xticks(np.arange(0,200,10))
plt.show()

# Para array2
signal2 = array2[:,-2]

signal_fft = np.fft.fft(signal2, N)           # fft magtinud
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
plt.title("FFT en el decibelios para señal Respiración")
plt.xlim([0,200])
#plt.xticks(np.arange(0,200,10))
plt.show()

# Para array3
signal3 = array3[:,-2]

signal_fft = np.fft.fft(signal3, N)           # fft magtinud
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
plt.title("FFT en el decibelios para señal Respiración 2")
plt.xlim([0,200])
#plt.xticks(np.arange(0,200,10))
plt.show()

# Para array4
signal4 = array4[:,-2]

signal_fft = np.fft.fft(signal4, N)           # fft magtinud
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
plt.title("FFT en el decibelios para señal Post ejercicio")
plt.xlim([0,200])
#plt.xticks(np.arange(0,200,10))
plt.show()

# Para array5
signal5 = array5[:,-2]

signal_fft = np.fft.fft(signal5, N)           # fft magtinud
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
plt.title("FFT en decibelios para Simulación de ejercicio")
plt.xlim([0,200])
#plt.xticks(np.arange(0,200,10))
plt.show()
