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

def ploteo_acotado(tiempo,t1,t2,señal,experimento):
    t_1=t1*250
    t_2=t2*250
    
    T=tiempo[t_1:t_2]
    x1=señal[t_1:t_2, 1]
    x2=señal[t_1:t_2, 2]
    x3=señal[t_1:t_2, 3]
    x4=señal[t_1:t_2, 4]
    x5=señal[t_1:t_2, 5]
    x6=señal[t_1:t_2, 6]
    x7=señal[t_1:t_2, 7]
    x8=señal[t_1:t_2, 8]
    señales=[x1,x2,x3,x4,x5,x6,x7,x8]
    n=1

    for i in señales:
        plt.plot(T,i)
        plt.title("EXG Channel " + str(n) + " para " + experimento)
        plt.grid(linestyle=":")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Amplitud")
        plt.show()
        n=n+1

def fft_c8(señal1,t1,t2,title):
    N=2**10
    Fs=250
    t1=250*t1
    t2=250*t2

    signal1 = señal1[t1:t2,1]
    signal2 = señal1[t1:t2,2]
    signal3 = señal1[t1:t2,3]
    signal4 = señal1[t1:t2,4]
    signal5 = señal1[t1:t2,5]
    signal6 = señal1[t1:t2,6]
    signal7 = señal1[t1:t2,7]
    signal8 = señal1[t1:t2,8]
    

    signal_fft1 = np.fft.fft(signal1, N)           # fft magtinud
    signal_fft1 = np.round(np.abs(signal_fft1),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
    signal_aux1 = signal_fft1/signal_fft1.max()     # hallamos el maximo para pasar la magnitud a escala db
    
    signal_fft2 = np.fft.fft(signal2, N)           # fft magtinud
    signal_fft2 = np.round(np.abs(signal_fft2),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
    signal_aux2 = signal_fft2/signal_fft2.max()     # hallamos el maximo para pasar la magnitud a escala db

    signal_fft3 = np.fft.fft(signal3, N)           # fft magtinud
    signal_fft3 = np.round(np.abs(signal_fft3),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
    signal_aux3 = signal_fft3/signal_fft3.max()     # hallamos el maximo para pasar la magnitud a escala db

    signal_fft4 = np.fft.fft(signal4, N)           # fft magtinud
    signal_fft4 = np.round(np.abs(signal_fft4),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
    signal_aux4 = signal_fft4/signal_fft4.max()     # hallamos el maximo para pasar la magnitud a escala db

    signal_fft5 = np.fft.fft(signal5, N)           # fft magtinud
    signal_fft5 = np.round(np.abs(signal_fft5),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
    signal_aux5 = signal_fft5/signal_fft5.max()     # hallamos el maximo para pasar la magnitud a escala db

    signal_fft6 = np.fft.fft(signal6, N)           # fft magtinud
    signal_fft6 = np.round(np.abs(signal_fft6),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
    signal_aux6 = signal_fft6/signal_fft6.max()     # hallamos el maximo para pasar la magnitud a escala db

    signal_fft7 = np.fft.fft(signal7, N)           # fft magtinud
    signal_fft7 = np.round(np.abs(signal_fft7),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
    signal_aux7 = signal_fft7/signal_fft7.max()     # hallamos el maximo para pasar la magnitud a escala db

    signal_fft8 = np.fft.fft(signal8, N)           # fft magtinud
    signal_fft8 = np.round(np.abs(signal_fft8),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
    signal_aux8 = signal_fft8/signal_fft8.max()     # hallamos el maximo para pasar la magnitud a escala db

    with np.errstate(divide='ignore'):
        signal_fft_db1 = 10*np.log10(signal_aux1)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero
    with np.errstate(divide='ignore'):
        signal_fft_db2 = 10*np.log10(signal_aux2)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero
    with np.errstate(divide='ignore'):
        signal_fft_db3 = 10*np.log10(signal_aux3)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero
    with np.errstate(divide='ignore'):
        signal_fft_db4 = 10*np.log10(signal_aux4)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero
    with np.errstate(divide='ignore'):
        signal_fft_db5 = 10*np.log10(signal_aux5)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero
    with np.errstate(divide='ignore'):
        signal_fft_db6 = 10*np.log10(signal_aux6)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero
    with np.errstate(divide='ignore'):
        signal_fft_db7 = 10*np.log10(signal_aux7)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero
    with np.errstate(divide='ignore'):
        signal_fft_db8 = 10*np.log10(signal_aux8)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero

    F_list1 = np.linspace(0,Fs/2, N//2)
    F1 = np.round(F_list1[np.argmax(signal_fft_db1)], 1)   # argmax, encuentra el argumento max en un array
    F_list2 = np.linspace(0,Fs/2, N//2)
    F2 = np.round(F_list2[np.argmax(signal_fft_db2)], 1)   # argmax, encuentra el argumento max en un array
    F_list3 = np.linspace(0,Fs/2, N//2)
    F3 = np.round(F_list3[np.argmax(signal_fft_db3)], 1)   # argmax, encuentra el argumento max en un array
    F_list4 = np.linspace(0,Fs/2, N//2)
    F4 = np.round(F_list4[np.argmax(signal_fft_db4)], 1)   # argmax, encuentra el argumento max en un array
    F_list5 = np.linspace(0,Fs/2, N//2)
    F5 = np.round(F_list5[np.argmax(signal_fft_db5)], 1)   # argmax, encuentra el argumento max en un array
    F_list6 = np.linspace(0,Fs/2, N//2)
    F6 = np.round(F_list6[np.argmax(signal_fft_db6)], 1)   # argmax, encuentra el argumento max en un array
    F_list7 = np.linspace(0,Fs/2, N//2)
    F7 = np.round(F_list7[np.argmax(signal_fft_db7)], 1)   # argmax, encuentra el argumento max en un array
    F_list8 = np.linspace(0,Fs/2, N//2)
    F8 = np.round(F_list8[np.argmax(signal_fft_db8)], 1)   # argmax, encuentra el argumento max en un array

    plt.plot(F_list1, signal_fft_db1,label="Channel 1")  #10 * np.log10(P / Pref) , decibelios
    plt.plot(F_list2, signal_fft_db2,label="Channel 2")  #10 * np.log10(P / Pref) , decibelios
    plt.plot(F_list3, signal_fft_db3,label="Channel 3")  #10 * np.log10(P / Pref) , decibelios
    plt.plot(F_list4, signal_fft_db4,label="Channel 4")  #10 * np.log10(P / Pref) , decibelios
    plt.plot(F_list5, signal_fft_db5,label="Channel 5")  #10 * np.log10(P / Pref) , decibelios
    plt.plot(F_list6, signal_fft_db6,label="Channel 6")  #10 * np.log10(P / Pref) , decibelios
    plt.plot(F_list7, signal_fft_db7,label="Channel 7")  #10 * np.log10(P / Pref) , decibelios
    plt.plot(F_list8, signal_fft_db8,label="Channel 8")  #10 * np.log10(P / Pref) , decibelios



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
f = open("OpenBCI.txt","r")
raw_data = f.readline()  # con f.read() leemos todo el contenido
f.close()

## Expresion regular para buscar automaticamente el contenido de un numero dentro de un string
x= re.findall("[0-5][0-9]\d", raw_data)

Fs = 250  #Obtenido de BCI
Ts=1/Fs

#print(f" Fs={Fs} hz\n Ts={Ts} s")

signal = np.genfromtxt("./OpenBCI.txt", delimiter=", ",skip_header = 5)

M = signal[:,1].shape[0]
n = np.arange(0,M)

t = n*Ts
t1=250*0
t2=250*35

T=t[t1:t2]
EO_ch1=signal[t1:t2,1]
EO_ch2=signal[t1:t2,2]
EO_ch3=signal[t1:t2,3]
EO_ch4=signal[t1:t2,4]
EO_ch5=signal[t1:t2,5]
EO_ch6=signal[t1:t2,6]
EO_ch7=signal[t1:t2,7]
EO_ch8=signal[t1:t2,8]

plt.plot(T,EO_ch1,label="CH1")
plt.plot(T,EO_ch2,label="CH2")
plt.plot(T,EO_ch3,label="CH3")
plt.plot(T,EO_ch4,label="CH4")
plt.plot(T,EO_ch5,label="CH5")
plt.plot(T,EO_ch6,label="CH6")
plt.plot(T,EO_ch7,label="CH7")
plt.plot(T,EO_ch8,label="CH8")
plt.legend(loc="upper right")
plt.title("Señal ojos cerrados")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.psd(EO_ch1,512,1/0.01,label="Ch1")
plt.psd(EO_ch2,512,1/0.01,label="Ch2")
plt.psd(EO_ch3,512,1/0.01,label="Ch3")
plt.psd(EO_ch4,512,1/0.01,label="Ch4")
plt.psd(EO_ch5,512,1/0.01,label="Ch5")
plt.psd(EO_ch6,512,1/0.01,label="Ch7")
plt.psd(EO_ch7,512,1/0.01,label="Ch7")
plt.psd(EO_ch8,512,1/0.01,label="Ch8")
plt.legend(loc="upper right")
plt.title("PSD para FFT de ojos cerrados")

t1=250*50
t2=250*100

EP1_ch1=signal[t1:t2,1]
EP1_ch2=signal[t1:t2,2]
EP1_ch3=signal[t1:t2,3]
EP1_ch4=signal[t1:t2,4]
EP1_ch5=signal[t1:t2,5]
EP1_ch6=signal[t1:t2,6]
EP1_ch7=signal[t1:t2,7]
EP1_ch8=signal[t1:t2,8]

T=t[t1:t2]
plt.plot(T,EP1_ch1,label="CH1")
plt.plot(T,EP1_ch2,label="CH2")
plt.plot(T,EP1_ch3,label="CH3")
plt.plot(T,EP1_ch4,label="CH4")
plt.plot(T,EP1_ch5,label="CH5")
plt.plot(T,EP1_ch6,label="CH6")
plt.plot(T,EP1_ch7,label="CH7")
plt.plot(T,EP1_ch8,label="CH8")
plt.legend(loc="upper right")
plt.title("Señal parpadeo")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
"""
t1=250*55
t2=250*60
T=t[t1:t2]
EP2_ch1=signal[t1:t2,1]
EP2_ch2=signal[t1:t2,2]
EP2_ch3=signal[t1:t2,3]
EP2_ch4=signal[t1:t2,4]
EP2_ch5=signal[t1:t2,5]
EP2_ch6=signal[t1:t2,6]
EP2_ch7=signal[t1:t2,7]
EP2_ch8=signal[t1:t2,8]
"""

plt.psd(EP1_ch1,512,1/0.01,label="Ch1EC")
plt.psd(EP1_ch2,512,1/0.01,label="Ch2EC")
plt.psd(EP1_ch3,512,1/0.01,label="Ch3EC")
plt.psd(EP1_ch4,512,1/0.01,label="Ch4EC")
plt.psd(EP1_ch5,512,1/0.01,label="Ch5EO")
plt.psd(EP1_ch6,512,1/0.01,label="Ch6EO")
plt.psd(EP1_ch7,512,1/0.01,label="Ch7EO")
plt.psd(EP1_ch8,512,1/0.01,label="Ch8EO")

plt.legend(loc="upper right")
plt.title("PSD FFT de parpadeo")



t1=250*140
t2=250*170
T=t[t1:t2]
PS_ch1=signal[t1:t2,1]
PS_ch2=signal[t1:t2,2]
PS_ch3=signal[t1:t2,3]
PS_ch4=signal[t1:t2,4]
PS_ch5=signal[t1:t2,5]
PS_ch6=signal[t1:t2,6]
PS_ch7=signal[t1:t2,7]
PS_ch8=signal[t1:t2,8]

plt.plot(T,PS_ch1,label="CH1")
plt.plot(T,PS_ch2,label="CH2")
plt.plot(T,PS_ch3,label="CH3")
plt.plot(T,PS_ch4,label="CH4")
plt.plot(T,PS_ch5,label="CH5")
plt.plot(T,PS_ch6,label="CH6")
plt.plot(T,PS_ch7,label="CH7")
plt.plot(T,PS_ch8,label="CH8")
plt.legend(loc="upper right")
plt.title("Señal problema sencillo")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")



t1=250*180
t2=250*220
T=t[t1:t2]
PC_ch1=signal[t1:t2,1]
PC_ch2=signal[t1:t2,2]
PC_ch3=signal[t1:t2,3]
PC_ch4=signal[t1:t2,4]
PC_ch5=signal[t1:t2,5]
PC_ch6=signal[t1:t2,6]

plt.psd(PS_ch1,512,1/0.01,label="Ch1PS")
plt.psd(PS_ch2,512,1/0.01,label="Ch2PS")
plt.psd(PS_ch3,512,1/0.01,label="Ch3PS")
plt.psd(PS_ch4,512,1/0.01,label="Ch4PS")
plt.psd(PS_ch5,512,1/0.01,label="Ch5PS")
plt.psd(PS_ch6,512,1/0.01,label="Ch6PS")
plt.psd(PS_ch7,512,1/0.01,label="Ch7PS")
plt.psd(PS_ch8,512,1/0.01,label="Ch8PS")
plt.legend(loc="upper right")
plt.title("PSD FFT de problema sencillo")
"""
plt.psd(PC_ch1,512,1/0.01,label="Ch1PC")
plt.psd(PC_ch2,512,1/0.01,label="Ch2PC")
plt.psd(PC_ch3,512,1/0.01,label="Ch3PC")
plt.psd(PC_ch4,512,1/0.01,label="Ch4PC")
plt.psd(PC_ch5,512,1/0.01,label="Ch5PC")
plt.psd(PC_ch6,512,1/0.01,label="Ch6PC")
plt.legend(loc="upper right")
plt.title("PSD FFT de problema sencillo (PS) vs problema complejo (PC)")
"""


t1=250*180
t2=250*220
T=t[t1:t2]
PC_ch1=signal[t1:t2,1]
PC_ch2=signal[t1:t2,2]
PC_ch3=signal[t1:t2,3]
PC_ch4=signal[t1:t2,4]
PC_ch5=signal[t1:t2,5]
PC_ch6=signal[t1:t2,6]
PC_ch7=signal[t1:t2,7]
PC_ch8=signal[t1:t2,8]

plt.plot(T,PC_ch1,label="CH1")
plt.plot(T,PC_ch2,label="CH2")
plt.plot(T,PC_ch3,label="CH3")
plt.plot(T,PC_ch4,label="CH4")
plt.plot(T,PC_ch5,label="CH5")
plt.plot(T,PC_ch6,label="CH6")
plt.plot(T,PC_ch7,label="CH7")
plt.plot(T,PC_ch8,label="CH8")
plt.legend(loc="upper right")
plt.title("Señal problema complejo")
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.psd(PC_ch1,512,1/0.01,label="Ch1PC")
plt.psd(PC_ch2,512,1/0.01,label="Ch2PC")
plt.psd(PC_ch3,512,1/0.01,label="Ch3PC")
plt.psd(PC_ch4,512,1/0.01,label="Ch4PC")
plt.psd(PC_ch5,512,1/0.01,label="Ch5PC")
plt.psd(PC_ch6,512,1/0.01,label="Ch7PC")
plt.psd(PC_ch7,512,1/0.01,label="Ch7PC")
plt.psd(PC_ch8,512,1/0.01,label="Ch8PC")
plt.legend(loc="upper right")
plt.title("PSD para FFT de problema complejo")

#fft_c8(signal,0,35,"Comparación de fft de canales para Ojos cerrados")

#fft_c8(signal,50,100,"Comparación de fft de canales para Ojos parpadeo")

#fft_c8(signal,50,100,"Comparación de fft de canales para Ojos parpadeo")

#ploteo_acotado(t,0,35,signal,"Ojos cerrados")

#ploteo_acotado(t,50,100,signal,"Ojos abiertos y cerrados cada 5s")

#ploteo_acotado(t,140,170,signal,"Ejercicio simple")

#ploteo_acotado(t,180,220,signal,"Ejercicio complejo")

#Comparación
#plt.plot(T3,x3,label="ojo abierto")     # graficamos la señal segun tiempo acotado
#plt.plot(T2,x2,label="ojo cerrado")
#plt.title("Comparación de señales")
#plt.grid(linestyle=":")
#plt.xlabel("Tiempo (s)")
#plt.ylabel("Amplitud")
#plt.legend(loc="upper right")
#plt.show()

#Comparación
#plt.plot(T3,x3,label="ojo abierto")     # graficamos la señal segun tiempo acotado
#plt.plot(T4,x4,label="ojo con luz")
#plt.title("Comparación de señales")
#plt.grid(linestyle=":")
#plt.xlabel("Tiempo (s)")
#plt.ylabel("Amplitud")
#plt.legend(loc="upper right")
#plt.show()


