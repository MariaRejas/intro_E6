
# **LABORATORIO 3: – USO DE BITalino PARA EMG**
# **Tabla de contenidos**

1. [Objetivos](#id1)
2. [Materiales y equipos](#id2)
3. [Resultados](#id3)\
     3.1 [Conexión usada](#id4)\
     3.2 [Video de la señal y Ploteo de la señal en OpenSignal](#id5)\
     3.3 [Resumen](#id6)\
     3.4 [Archivos](#id7)\
     3.5 [Ploteo de la señal en Python](#id8)
    
## **Objetivos** <a name="id1"></a>
* Adquirir señales biomédicas de EMG de un grupo muscular especifico.
* Hacer una correcta configuración de BiTalino.
* Extraer la información de las señales EMG  del software OpenSignals (r)evolution.



## **Materiales y equipos** <a name="id2"></a>

<div align="center">

|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
|       -      |      Laptop     |       1      |

</div>

<p align="justify">
<p align="center"><img src="https://i.postimg.cc/XNmdLX3Z/equipos.png" width="400" height="266"></p>
</p>

## **RESULTADOS** <a name="id3"></a>
### **Conexión usada** <a name="id4"></a>
Se utilizó la conexión EMG en la placa Bitalino utilizando el sensor EMG de 3 electrodos como se muestra a continuación.
<p align="justify">
<p align="center"><img src="https://i.postimg.cc/43WWwtJC/Whats-App-Image-2023-04-05-at-12-04-38-PM.jpg" width="400" height="266"></p>
</p>

El siguiente procedimiento consiste en colocar los electrodos EMG en el usuario de prueba. Para ello se utilizó la **Guía De Procedimiento de Electromiografía y velocidad de conducción de nervios periféricos** del año 2020 elaborada por el **Instituto Nacional del Niño de San Borja** para el Ministerio de Salud (MINSA).

### **Video de la señal y ploteo en Opensignal** <a name="id5"></a>
### PRUEBA 1 <br>

<p align="justify">
En la prueba 1 se tomo la señal de reposo del nervio mediano .<br>
La primera imagen muestra el posicionamiento de los electrodos en uno de los participantes del grupo
La segunda imagen muestra el posicionamiento de los electrodos que se tuvo como referencia
</p>
<p align="center"><img src="https://i.postimg.cc/kMYzy0T1/Whats-App-Image-2023-04-05-at-12-04-45-PM.jpg" width="400" height="350"></p> 
<p align="center"><img src="https://i.postimg.cc/bN2C9sDr/equipo-texto.png" width="400" height="266"></p>
En la siguiente figura se observa el ploteo de la señal en reposo en Opensignal. En este se puede observar que la señal no varía mucho y mas bien presenta ruido, esto principalmente a que la señal EMG de superficie recibe los impulsos de varias unidades motoras. Asimismo, la señal en este caso mide las distancias y amplitudes entre los electrodos de estimulo proximal y distal, al no existir un desplazamiento la señal no varía. Por último, la señal tambien mide la velocidad de conducción entre la muñeca y el codo, entre ambos electrodos.
</p>
<p align="center"><img src="https://i.postimg.cc/NFQfY5yx/estado-reposo.png" width="400" height="266"></p>
<div align="center">
En el siguiente icono se encuentra el link del video de la prueba 1.
</p> 

[<img src="https://cdn.icon-icons.com/icons2/1713/PNG/512/iconfinder-videologoplayicon-3993847_112649.png" width="20%" height="20%">](https://youtu.be/QVbB6sypamE)

</div>

### PRUEBA 2 <br>

<p align="justify">
En la prueba 2 se tomo la señal de la conducción nerviosomotora del nervio mediano durante la contracción en forma de puño <br>
</p>
<p align="center"><img src="https://i.postimg.cc/xThD3X0F/pu-o.png" width="400" height="266"></p>
En la siguiente figura se observa el ploteo de la señal de conduccion nerviosa motora del nervio mediano durante el movimiento puño cerrado en Opensignal. En este a diferencia de en la primera prueba sí se puede observar una variación en las amplitudes de la señal ya que existe un movimiento por parte de la mano. Asimismo, las frecuencias en ambos casos no varían ya que las frecuencias a a las cuales se lleva a cabo la conducción nerviosa son constantes.
</p>
<p align="center"><img src="https://i.postimg.cc/Gt4g4js3/se-al-completa.png" width="1000" height="266"></p>
<div align="center">
En el siguiente icono se encuentra el link del video de la prueba 2.
</p>  

[<img src="https://cdn.icon-icons.com/icons2/1713/PNG/512/iconfinder-videologoplayicon-3993847_112649.png" width="20%" height="20%">](https://youtu.be/yfaGtikDpqY)

</div>
</p>  

## **Resumen y explicación de la señal ploteada** <a name="id6"></a>
### Técnica del estudio de conducción nerviosa motora del nervio mediano
El siguiente es el procedimiento para el estudio de conducción nerviosa motora del nervio mediano. 

*Electrodos de registro*
- Electrodo activo (G1): Colocar sobre el centro del músculo abductor corto del pulgar (ACP), un tercio de la distancia entre el pliegue carpo metacarpiano y la articulación metacarpo falángica del pulgar (1er dedo).
- Electrodo de referencia (G2): Colocar sobre la articulación metacarpo falángico del primer dedo, distal al electrodo activo.
- Electrodo tierra: Colocado en el dorso de la mano.

*Electrodos de estímulo*
- Distal: Colocar a nivel de la muñeca proximal al electrodo activo entre los tendones de los músculos flexores radiales del carpo y palmar mayor.
- Proximal: Colocar sobre la arteria braquial (pulso braquial) en el codo, entre el tendón del músculo bíceps braquial y el epicóndilo medial.

 *Mediciones*
- Distancias, latencias y amplitudes de todos los lugares (distal y proximal) evaluados.
- Velocidad de conducción entre la muñeca y el codo.





### **Archivos** <a name="id7"></a>
- [Documentos (.txt)](https://github.com/MariaRejas/intro_E6/blob/main/laboratorios/3.%20Adquisici%C3%B3n%20de%20se%C3%B1ales%20EMG/Se%C3%B1al%20EMG%20Lab1.txt)
- [Programa de ploteo en python](https://github.com/MariaRejas/intro_E6/blob/main/laboratorios/3.%20Adquisici%C3%B3n%20de%20se%C3%B1ales%20EMG/Se%C3%B1al_EMG.py)


### **Ploteo de la señal en Python** <a name="id8"></a>
<p align="justify">
La primera prueba se realizo en estado de reposo,la cual dura un total de X segundos. Esto se puede observar en la siguiente gráfica.
</p>
- Señal sin movimiento:
</p>
Debido a que la señal era pequeña se amplió la imagen reduciendo la amplitud para una mejor observación de la señal. Se puede observar amplitudes parecidas, ya que corresponde a una señal sin movimiento.
<p align="center"><img src="https://i.postimg.cc/zBdLvCnf/Whats-App-Image-2023-04-05-at-7-52-40-PM.jpg" width="600" height="400"></p>

La segunda prueba se realizó con la contraccion maxima del puño cerrado. En la figura se puede observar la reconstrucción de la señal en el tiempo a partir de 81000 muestras y de una frecuencia de muestreo de 1000 Hz, lo cual nos da una duración total de 81 segundos.
</p>
- Señal con picos máximos obtenidos del movimiento puño cerrado: Se oberva picos más altos de amplitud cuando se da el movimiento del puño cerrado, en la cual las unidades motoras se activan con mayor frecuencia.
<p align="center"><img src="https://i.postimg.cc/LsTN8WhF/Whats-App-Image-2023-04-05-at-7-34-03-PM.jpg" width="600" height="400"></p>
</p>
- Gráfico en el dominio de la frecuencia: Al realizar la Trasnformada Rápida de Fourier a nuestra señal y transformarla del dominio del tiempo al dominio de la frecuencia, se observa que predomina la actividad en 2 frecuencias: una a 60 Hz a proximadamente y la otra a 120 Hz aproximadamente. 
<p align="center"><img src="https://i.postimg.cc/VvM7mkCD/Whats-App-Image-2023-04-05-at-7-34-19-PM.jpg" width="600" height="400"></p>


