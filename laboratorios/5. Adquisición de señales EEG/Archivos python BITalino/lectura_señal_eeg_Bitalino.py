import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re

def ploteo(tiempo,señal,canal,titulo):
    X1=señal[:,canal]
    plt.plot(tiempo,X1)
    plt.title(titulo)
    plt.grid(linestyle=":")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.show()

def ploteo_acotado(tiempo,t1,t2,señal,canal,titulo):
    t_1=t1*1000
    t_2=t2*1000
    
    T1=tiempo[t_1:t_2]
    x1=señal[t_1:t_2, canal]
    
    plt.plot(T1,x1)
    plt.title(titulo)
    plt.grid(linestyle=":")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.show()

def fft(señal,title):
    Fs=1000
    N=2**10
    signal1 = señal[:,-2]

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
    plt.title(title)
    plt.xlim([0,50])
    #plt.xticks(np.arange(0,200,10))
    plt.show()

def fft_c(señal1,señal2,label1,label2,title):
    N=2**10
    Fs=1000
    
    signal1 = señal1[:,-2]
    signal2 = señal2[:,-2]

    signal_fft1 = np.fft.fft(signal1, N)           # fft magtinud
    signal_fft1 = np.round(np.abs(signal_fft1),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
    signal_aux1 = signal_fft1/signal_fft1.max()     # hallamos el maximo para pasar la magnitud a escala db
    
    signal_fft2 = np.fft.fft(signal2, N)           # fft magtinud
    signal_fft2 = np.round(np.abs(signal_fft2),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
    signal_aux2 = signal_fft2/signal_fft2.max()     # hallamos el maximo para pasar la magnitud a escala db


    with np.errstate(divide='ignore'):
        signal_fft_db1 = 10*np.log10(signal_aux1)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero
    with np.errstate(divide='ignore'):
        signal_fft_db2 = 10*np.log10(signal_aux2)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero

    F_list1 = np.linspace(0,Fs/2, N//2)
    F1 = np.round(F_list1[np.argmax(signal_fft_db1)], 1)   # argmax, encuentra el argumento max en un array
    F_list2 = np.linspace(0,Fs/2, N//2)
    F2 = np.round(F_list2[np.argmax(signal_fft_db2)], 1)   # argmax, encuentra el argumento max en un array

    plt.plot(F_list1, signal_fft_db1,label=label1)  #10 * np.log10(P / Pref) , decibelios
    plt.plot(F_list2, signal_fft_db2,label=label2)  #10 * np.log10(P / Pref) , decibelios

    plt.text(F1,0, f"{F1}Hz")
    plt.grid(linestyle=":")
    plt.ylabel("Magnitud (db)")
    plt.xlabel("Frecuencias (Hz)")
    plt.legend(loc="upper right")
    plt.title(title)
    plt.xlim([0,50])
    #plt.xticks(np.arange(0,200,10))
    plt.show()

def fft_c3(señal1,señal2,señal3,label1,label2,label3,title):
    N=2**10
    Fs=1000
    signal1 = señal1[:,-2]
    signal2 = señal2[:,-2]
    signal3 = señal3[:,-2]

    signal_fft1 = np.fft.fft(signal1, N)           # fft magtinud
    signal_fft1 = np.round(np.abs(signal_fft1),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
    signal_aux1 = signal_fft1/signal_fft1.max()     # hallamos el maximo para pasar la magnitud a escala db
    
    signal_fft2 = np.fft.fft(signal2, N)           # fft magtinud
    signal_fft2 = np.round(np.abs(signal_fft2),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
    signal_aux2 = signal_fft2/signal_fft2.max()     # hallamos el maximo para pasar la magnitud a escala db

    signal_fft3 = np.fft.fft(signal3, N)           # fft magtinud
    signal_fft3 = np.round(np.abs(signal_fft3),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
    signal_aux3 = signal_fft3/signal_fft3.max()     # hallamos el maximo para pasar la magnitud a escala db


    with np.errstate(divide='ignore'):
        signal_fft_db1 = 10*np.log10(signal_aux1)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero
    with np.errstate(divide='ignore'):
        signal_fft_db2 = 10*np.log10(signal_aux2)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero
    with np.errstate(divide='ignore'):
        signal_fft_db3 = 10*np.log10(signal_aux3)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero

    F_list1 = np.linspace(0,Fs/2, N//2)
    F1 = np.round(F_list1[np.argmax(signal_fft_db1)], 1)   # argmax, encuentra el argumento max en un array
    F_list2 = np.linspace(0,Fs/2, N//2)
    F2 = np.round(F_list2[np.argmax(signal_fft_db2)], 1)   # argmax, encuentra el argumento max en un array
    F_list3 = np.linspace(0,Fs/2, N//2)
    F3 = np.round(F_list3[np.argmax(signal_fft_db3)], 1)   # argmax, encuentra el argumento max en un array

    plt.plot(F_list1, signal_fft_db1,label=label1)  #10 * np.log10(P / Pref) , decibelios
    plt.plot(F_list2, signal_fft_db2,label=label2)  #10 * np.log10(P / Pref) , decibelios
    plt.plot(F_list3, signal_fft_db3,label=label3)  #10 * np.log10(P / Pref) , decibelios

    plt.text(F1,0, f"{F1}Hz")
    plt.grid(linestyle=":")
    plt.ylabel("Magnitud (db)")
    plt.xlabel("Frecuencias (Hz)")
    plt.legend(loc="upper right")
    plt.title(title)
    plt.xlim([0,50])
    #plt.xticks(np.arange(0,200,10))
    plt.show()

# Ejercicio con bitalino
f1 = open("Lab5_ejerciciocomplejo.txt","r")
raw_data1 = f1.readline()  # con f.read() leemos todo el contenido
f1.close()

f2 = open("Lab5_ojocerrados 30.txt","r")
raw_data2 = f2.readline()  # con f.read() leemos todo el contenido
f2.close()

f3 = open("Lab5_ojos abiertos.txt","r")
raw_data3 = f3.readline()  # con f.read() leemos todo el contenido
f3.close()

f4 = open("Lab5_ojos con luz telefono.txt","r")
raw_data4 = f4.readline()  # con f.read() leemos todo el contenido
f4.close()

f5 = open("Lab5_pensando.txt","r")
raw_data5 = f5.readline()  # con f.read() leemos todo el contenido
f5.close()

f6 = open("Lab5_problema 1.txt","r")
raw_data6 = f6.readline()  # con f.read() leemos todo el contenido
f6.close()

## Expresion regular para buscar automaticamente el contenido de un numero dentro de un string
x1 = re.findall("[0-5][0-9]\d", raw_data1)

x2 = re.findall("[0-5][0-9]\d", raw_data2)

x3 = re.findall("[0-5][0-9]\d", raw_data3)

x4 = re.findall("[0-5][0-9]\d", raw_data4)

x5 = re.findall("[0-5][0-9]\d", raw_data5)

x6 = re.findall("[0-5][0-9]\d", raw_data6)

Fs = 1000  #Obtenido de bitalino
Ts=1/Fs

print(f" Fs={Fs} hz\n Ts={Ts} s")

signal1 = np.genfromtxt("./Lab5_ejerciciocomplejo.txt", delimiter="	",skip_header = 2)
signal2 = np.genfromtxt("./Lab5_ojocerrados 30.txt", delimiter="	",skip_header = 2)
signal3 = np.genfromtxt("./Lab5_ojos abiertos.txt", delimiter="	",skip_header = 2)
signal4 = np.genfromtxt("./Lab5_ojos con luz telefono.txt", delimiter="	",skip_header = 2)
signal5 = np.genfromtxt("./Lab5_pensando.txt", delimiter="	",skip_header = 2)
signal6 = np.genfromtxt("./Lab5_problema 1.txt", delimiter="	",skip_header = 2)

M1 = signal1[:,-2].shape[0]
n1 = np.arange(0,M1)

M2 = signal2[:,-2].shape[0]
n2 = np.arange(0,M2)

M3 = signal3[:,-2].shape[0]
n3 = np.arange(0,M3)

M4 = signal4[:,-2].shape[0]
n4 = np.arange(0,M4)

M5 = signal5[:,-2].shape[0]
n5 = np.arange(0,M5)

M6 = signal6[:,-2].shape[0]
n6 = np.arange(0,M6)

### Registro de ojos abiertos ###
t3 = n3*Ts
ploteo(t3,signal3,-2,"Señal ojos abiertos")
fft(signal3,"FFT en decibelios para señal ojos abiertos")

### Registro de ojos cerrados ###
t_2 = n2*Ts
ploteo(t_2,signal2,-2,"Señal ojos cerrados")
#ploteo_acotado(t_2,0,30,signal2,-2,"Señal ojos cerrados acotado")
fft(signal2,"FFT en decibelios para señal ojos cerrados")
fft_c(signal2,signal3,"Señal ojo abierto","Señal ojos abiertos","Comparación FFT de ojo cerrado y abierto")

### Registro con exposición a luz(linterna) ###
t4 = n4*Ts
ploteo(t4,signal4,-2,"Señal ojos con luz")
#ploteo_acotado(t4,0,30,signal4,-2,"Señal ojos con luz acotada")
fft(signal4,"FFT en decibelios para señal ojos con luz")

### Registro de ejercicio de memoria ###
t_1 = n1*Ts
#ploteo(t_1,signal1,-2,"Señal ejercicio complejo")
ploteo_acotado(t_1,65,100,signal1,-2,"Señal ejercicio complejo acotado")
fft(signal1,"FFT en decibelios para señal ejercicio complejo")

### Registro de razonamiento de un problema matemático ##
t6 = n6*Ts
ploteo(t6,signal6,-2,"Señal problema 1")
#ploteo_acotado(t6,65,100,signal6,-2,"Señal problema 1 acotada")
fft(signal6,"FFT en decibelios para señal problema 1")

### EXTRAS ###
ploteo_acotado(t3,0,30,signal3,-2,"Señal ojos abiertos acotada")

t5 = n5*Ts
ploteo(t5,signal5,-2,"Señal memorizando")
#ploteo_acotado(t5,65,100,signal5,-2,"Señal memorizando acotada")
fft(signal5,"FFT en decibelios para señal memorizando")

#Comparación
ta=1000*0
tb=1000*30
T3=t3[ta:tb]
T2=t_2[ta:tb]
x3=signal3[ta:tb,-2]
x2=signal2[ta:tb,-2]
plt.plot(T3,x3,label="ojo abierto")     # graficamos la señal segun tiempo acotado
plt.plot(T2,x2,label="ojo cerrado")
plt.title("Comparación de señales")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.show()

#Comparación
ta=1000*0
tb=1000*30
T3=t3[ta:tb]
T4=t4[ta:tb]
x3=signal3[ta:tb,-2]
x4=signal4[ta:tb,-2]
plt.plot(T3,x3,label="ojo abierto")     # graficamos la señal segun tiempo acotado
plt.plot(T4,x4,label="ojo con luz")
plt.title("Comparación de señales")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.show()

#Comparación de ojo abierto y con luz
fft_c(signal3,signal4,"Señal ojo abierto","Señal ojo con luz","Comparación FFT de ojo abierto y con luz")

fft_c3(signal2,signal3,signal4,"Ojos cerrados","Ojos abiertos","Ojos con luz","Comparación FFT de señales ojos cerrados, ojos abiertos y ojos con luz")

#Comparación de ojo abierto y con luz
#fft_c(signal2,signal3,"Señal ojos cerrados","Señal ojos abiertos","Comparación FFT de ojo cerrado y abierto")
señal2=signal2[:,-2]
señal3=signal3[:,-2]
plt.psd(señal2,512,1/0.01,label="Ojos abiertos")
plt.psd(señal3,512,1/0.01,label="Ojos cerrados")
plt.legend(loc="upper right")
plt.title("PSD para FFT ojos cerrados vs ojos abiertos")
