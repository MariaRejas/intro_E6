# **LABORATORIO 5 PARTE 2: – Uso de Ultracortex y BiTalino para EEG**
Realizado el 19 de abril de 2023
<p align="center">
     <img width="500" height="300" src="https://images.squarespace-cdn.com/content/v1/5f7b55a801226812a44f7180/1609441748072-S5NU5R5YSQF4LYBO7KZT/OpenBCI-WebXR-EEG.gif">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/17307/31218894-586281e4-a9c4-11e7-81d8-bd6f3dfd4267.gif">
</p>

# **Tabla de contenidos**
[Laboratorio 5 parte 1](https://github.com/MariaRejas/intro_E6/blob/main/laboratorios/laboratorio5/lsb5.md)</p>

5. Análisis de la señal EEG con BiTalino\
   5.4 [Ploteo de la señal en Python](#id8)\
   5.5 [Archivos](#id9)

6. [Análisis de la señal EEG con Ultracortex](#id10)\
  6.1 [Conexión usada](#id11)\
  6.2 [Procedimiento](#id12)\
  6.3 [Videos de la señal](#id13)\
  6.4 [Ploteo de la señal en OpenBCI](#id14)\
  6.5 [Ploteo de la señal en Python](#id15)\
  6.6 [Interpretación de las gráficas](#id16)\
  6.6 [Archivos](#id17)
7. [Conclusiones](#id18)
8. [Referencias](#id19)

### **Ploteo de la señal en tiempo y frecuencia en Python** <a name="id8"></a>
---

a) Registro de ojos abiertos:
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707896/233435534-127743c3-b838-42a4-9e89-a6ecc3f1d1f3.png">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/55772705/233763304-2fba7e15-52e9-4112-859b-862c22d6b595.jpeg">

b) Registro de ojos cerrados:
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707896/233436145-77ea47c1-b1b0-41c0-8a16-e9290dcd5a55.png">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/55772705/233763335-c48152dd-90c8-4bdd-a2a1-851dafbb2b7c.jpeg">
</p>

</p>
<p align="center">
 <img width="500" height="400" src="https://user-images.githubusercontent.com/55772705/233763485-4c853f4b-4edf-4d48-aa31-001d6076bb55.jpeg">
 
c) Registro de ojos con exposición a luz (linterna)
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707896/233436743-12f53bdd-2ea8-4449-b317-1197f3d16200.png">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/55772705/233763380-f1faafe7-5e87-41fd-9f35-ddd5150a2756.jpeg">
</p>

d) Registro del ejercicio de memoria
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707896/233437078-a52679d2-54c3-4a41-82e1-2f9a68aba8e8.png">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/55772705/233763413-e948cf34-8c39-49cf-96a5-f846f209657d.jpeg">
</p>

e) Registro de razonamiento de un problema matemático
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707896/233438470-38edfe1e-7f6b-4ab0-9307-37dd809a14c6.png">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/55772705/233763444-0e951533-12d5-486f-9fe5-1211fc59712b.jpeg">
     
</p>

### **Archivos** <a name="id9"></a>
Se encuentran en la carpeta del laboratorio 5.
#

## **Análisis de la señal EEG con Ultracortex** <a name="id10"></a>

## **Conexión usada** <a name="id11"></a>
<p align="justify">
La colocación de los 16 electrodos está de acuerdo con la configuración del sistema 10-20, por lo cual la ubicación es la siguiente: AF3, AF4, F7, F3, F4, F8, T7, C3,C4, T8, P7, P3, P4, P8, O1, O2 como se indica con nodos coloreados en la Fig. 9.Así mismo los electrodos de referencia (barra de resistencia superficial - SRB) y de tierra (Bias) se colocaron en la oreja izquierda y derecha, respectivamente. Los headsets Mark IV de 16 canales funcionaron a una frecuencia de muestreo de 125 Hz.</p>
<p align="center">
     <img width="400" height="300" src="https://user-images.githubusercontent.com/89707896/233443718-3bb5e437-ca15-4c20-9b96-161e88d367a1.png">
</p>
<p align="center">
Figura 9.Ubicación de los electrodos por colores [13].
</p>

<p align="center">
     <img width="250" height="200" src="https://user-images.githubusercontent.com/89707896/233676279-73daf977-f8c3-48ac-b704-c278ebf8a9bb.jpeg">
     <img width="250" height="200" src="https://user-images.githubusercontent.com/89707896/233676333-74a22680-21e1-4f9b-8ed7-1ec3e50cce09.jpeg">
     <img width="250" height="200" src="https://user-images.githubusercontent.com/89707896/233676411-5cbc485f-706d-4985-a59a-0aea82ff6c89.jpeg">
</p>
<p align="center">
Figura 10.Colocación de los electrodos en el participante según  el sistema 10-20. [Elaboración propia]
</p>

## **Procedimiento** <a name="id12"></a>
* Con los ojos cerrados
* Con los ojos abiertos y cerrados cada 5 segundos
* Descanso de 30 segundos
* Tras realizar un ejercicio complejo
* Tras realizar un ejercicio simple

## **Video de la señal** <a name="id13"></a>
| Ojos cerrados (30 segundos) | Ojos abiertos y cerrados cada 5 segundos |
| ------------ |  :------------------------------------: |
| <video src="https://user-images.githubusercontent.com/89707896/233675019-76a1d66c-2838-4e2a-88d4-9d079feb7924.mp4" width="200" /> | <video src="https://user-images.githubusercontent.com/89707896/233675136-332bb7ca-7135-46bc-baad-86459f931beb.mp4" width="200" /> |
</div>

| Ejercicio complejo | Ejercicio simple |
| ------------|  :------------------------------------: |
|[![Alt text](https://user-images.githubusercontent.com/89707896/233679236-ffa95c49-1b5f-4ce8-aa9a-fc081d68bd91.png)](https://www.youtube.com/watch?v=R1aoqyflylQ)| <video src="https://user-images.githubusercontent.com/89707896/233675841-df32f803-5873-4b8d-9b2a-7d8b73eebed8.mp4" width="200" /> |
</div>



## **Ploteo de la señal en OpenBCI** <a name="id14"></a>

## **Ploteo de la señal en Python** <a name="id15"></a>

a) Con los ojos cerrados
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707127/233770786-0b27e7c0-90d4-4539-bcb7-3a5944c2d159.jpeg">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/55772705/233766532-87d26b98-41de-485b-a43e-1ea816f9bf19.jpeg">
</p>

b) Con los ojos abiertos y cerrados cada 5 segundos
</p>
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707127/233770954-2f5d0cc3-70ef-4bc0-a17d-a860826f79b1.jpeg">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/55772705/233766561-310c06c0-8c28-4466-b2f5-8c9dcf0af332.jpeg">
 </p>   
  
c) Tras realizar un ejercicio complejo
</p>
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707127/233771035-c368718b-f2ff-4001-b202-298c1d86a6fd.jpeg">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/55772705/233766624-a48657ac-d4d7-4865-8779-f78acad29e2b.jpeg">
 </p>
 
d) Tras realizar un ejercicio simple
</p>
<p align="center">
    <img width="500" height="400" src="https://user-images.githubusercontent.com/89707127/233771054-3c1bd770-8cd2-47eb-abad-c6b3597fc6c0.jpeg">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/55772705/233766597-d34e4430-1160-4f71-bf86-570f917f975e.jpeg">
</p>    

## **Interpretación de las gráficas** <a name="id16"></a>
a) Ojos cerrados vs ojos abiertos: Para analizar el procesamiento visual, las regiones de interés son el lóbulo frontal (F7, F8, Fp1 y Fp2) y occipital (O1 y O2) [1C]. El paso del estado de ojos cerrados (reposo) a otro con los ojos abiertos se denomina activación. Las características de las principales ondas en ambos estados se resume en la siguiente tabla [2C] [tC]:
| Onda | PSD con ojos cerrados | PSD con ojos abiertos |
| -----  |  :------: |  :-----: |
| delta | mayor | menor |
| theta | mayor | menor |
| alpha | mayor | menor |
| beta | menor | mayor |
| gamma | - | - |
</div>

En la siguiente gráfica se compara y analiza la FFT de los canales involucrados en la percepción visual: 1 (Fp1), 2 (Fp2), 7 (O7) y 8 (O8) con ojos cerrados (EC) y abiertos (EO).</a> 

<p>
<img width="500" height="400" src="https://user-images.githubusercontent.com/89707127/233773525-d2cf0096-fd0e-42ad-afaa-08bceeb9edba.png">
<p>
     
* Ondas delta (δ): Se observa una mayor densidad espectral de potencia en el canal 8 con ojos cerrados (color rojo).
* Ondas theta (Ө): Se observa una mayor densidad espectral de potencia en el canal 8 con ojos cerrados (color rojo).
* Ondas alpha (α): Se observa una mayor densidad espectral de potencia en el canal 8 con ojos cerrados (color rojo) y en el canal 2 con ojos cerrados (color anaranjado).
* Ondas beta (β): Se observa un pico en el canal 8 con ojos abiertos (color plomo).
     
Al cerrar los ojos, la actividad de las ondas delta indicaría una actividad cerebral similar al del tiempo de sueño, esto va acorde a la actividad, ya que al mantener los ojos cerrados se limitan el resto de estímulos y se induce a un estado similar a la del sueño. Al abrir los ojos, se genera una activación, lo cual se representa con un aumento en la actividad de la región occipital (canal 8 EO), lo cual se corrobora con los resultados obtenidos en la gráfica anterior.

b) Problema sencillo vs problema complejo: Resolver problemas requieren numerosas operaciones cognitivas, que incluyen compresión, razonamiento y cálculo. Las regiones asociadas para analizar su correspondiente actividad cerebral son las cortezas parietales (P3, P4), temporales (T3, T4)y prefrontales (F3, F4).

En la siguiente gráfica se compara y analiza la FFT de los canales involucrados en operaciones cognitivas: 1 (F3), 2 (F4), 3 (T3), 4 (T4), 5 (P3) Y 6 (P4) al realizar un ejercicio sencillo y complejo (EO).</a> 

<p>
<img width="500" height="400" src="https://user-images.githubusercontent.com/89707127/233775954-d82699f7-9719-4888-a07c-0f21b15023d7.png">
<p>
     
* Ondas delta (δ): Se observa una mayor densidad espectral de potencia en el canal 4 al efectuar un ejercicio sencillo (color rojo).
* Ondas theta (Ө): Se observa una mayor densidad espectral de potencia en el canal 4 al efectuar un ejercicio sencillo (color rojo).
* Ondas alpha (α): Se observa una mayor densidad espectral de potencia en el canal 2 al efectuar un ejercicio complejo (color plomo).
* Ondas beta (β): Se observa una mayor densidad espectral de potencia en el canal 4 al efectuar un ejercicio sencillo (color rojo).
     
Asimismo, se observa:
     
* Canal 1: Se observa una mayor densidad espectral de potencia de las ondas theta al efectuar un ejercicio complejo que uno sencillo (Ver que la línea rosada (Ch1PC) tiene valores más altos que la línea turquesa (Ch1PS) en el rango de frecuencias de la onda theta (4-8Hz)).
* Canal 5: Se observa una mayor densidad espectral de potencia de las ondas alpha al efectuar un ejercicio complejo que uno sencillo (Ver que la línea lila (Ch5PC) tiene valores más altos que la línea turquesa oscura (Ch5PS) en el rango de frecuencias de la onda alpha (8-13Hz)).
* Canal 4: Se observa una menor densidad espectral de potencia en las ondas beta al efectuar un ejercicio complejo que uno sencillo (Ver que la línea celeste (Ch4PC) tiene valores más bajos que la línea roja (Ch4PS) en el rango de frecuencias de la onda beta (13-30Hz)).
     
Tras la realizar un ejercicio, en el análisis por frecuencias se identificó una mayor presencia de ondas delta y beta 2. La presencia de ondas beta 2 indicaría la alta actividad por parte del lóbulo frontal encargado de funciones cognitivas, al estar sometido a una tarea altamente compleja. Sin embargo, durante las experimentación el voluntario tampoco realizó el problema de forma completamente mental debido a que lo hizo hablando con voz alta. Asimismo, casi al final del ejercicio este fue interrumpido.
     
Además, en el estudio "EEG correlation during the solving of simple and complex logical–mathematical problems", del cual se tomó como referencia los ejercicios sencillos y complejos presentaron resultados muy similares al análisis anterior para el canal 1 (F3), 5 (P3) y 4 (T4).     
     
## **Archivos** <a name="id17"></a>

## **Conclusiones** <a name="id18"></a>
<p align="justify">
-Para el análisis de las pruebas de ojos abierto,ojos cerrados y con estimulación luminosa:

Conclusión :

-Durante la prueba de estimulación luminosa se puede apreciar que las ondas alfa disminuyen cuando los ojos están abiertos o expuestos a una fuente de luz ,en cambio cuando están cerrados esta banda suele aumentarse.Así mismo existen medios difusores que alteraron la señal como la estimulación de la retina o una fuente no fisiológico como un electrodo frontopolar de alta impedancia [11].</p>
</p>

<p align="justify">
-Para las pruebas de memoria y razonamiento:

Conclusión:
Estudios previos han demostrado la ocurrencia  de  oscilaciones lentas (4Hz a 7 Hz) y rapidas (20 Hz y 30 Hz) en las posiciones de los electrodos frontal y prefrontal durante el procesamiento de la memoria ,lo cual se puede apreciar en la gráficas ya que se obtuvieron medidas de frecuencia alrededor de  15- 22 Hz .Así mismo durante este registro EEG se puede observar que se dio un aumento en las bandas theta y gamma en FP1 ,lo cual está relacionado con la memorización de palabras,ya que  estudios fisiológicos se han demostrado que las altas frecuencias en los rangos beta y gamma ,(frecuencias de 15 a 30 y 30 a 60 Hz) ,está relacionado a un estado de atención enfocada.Finalmente podemos ver que todo esto indica la participación de la corteza prefrontal durante el procesamiento de la información [12].</p>
</p>

## **Referencias** <a name="id18"></a>
---
1. Electroencefalografía (EEG) - Mayo Clinic. (2022, 19 de julio). Mayo Clinic - Mayo Clinic. https://www.mayoclinic.org/es-es/tests-procedures/eeg/about/pac-20393875#:~:text=Un%20electroencefalograma%20(EEG)%20es%20un,el%20tiempo,%20incluso%20mientras%20duermes.
2. Clínica Universidad de Navarra. (s.f.). Clínica Universidad de Navarra | Centrados en el paciente. https://www.cun.es/enfermedades-tratamientos/pruebas-diagnosticas/electroencefalograma#:~:text=Puede%20detectar%20alteraciones%20de%20todo,metabólicas,%20infecciosas%20etc.).
3. How to Read an EEG. (s.f.). Epilepsy Foundation. https://www.epilepsy.com/diagnosis/eeg/how-read
4. Controlando los humos generados durante un Electroencefalograma EGG; colocando y retirando electrodos. (s.f.). Sentry Air Systems. http://sentryairsystemsmexico.blogspot.com/2015/10/controlando-los-humos-generados-durante.html
5. ¿Qué son las ondas Cerebrales? - NeuroFeedBack Barcelona. (s.f.). NeuroFeedBack Barcelona. https://www.neurofeedback.cat/que-son-las-ondas-cerebrales/
6. Ondas o Registros Cerebrales que detectan el Funcionamiento Cerebral. (s.f.). encolombia.com. https://encolombia.com/medicina/psiquiatria-salud-mental/azar-determinista/ondas-registros-cerebrales/
7. "El cerebro". (s.f.). Neurofeedback y sus aplicaciones, Psicotecnologia, equipos y cursos de entrenamiento. http://sicotecnologia.com/cerebro.htm
8. Técnicas de procesamiento de EEG para detección de eventos. (s.f.). SEDICI - Repositorio de la Universidad Nacional de La Plata. http://sedici.unlp.edu.ar/handle/10915/32602
9. Aguilar, C., Muñóz, A., Paulucci, P., Carrere, L., & Tabernig, C. (2022). A hybrid BCI for Neurofeedback-Based Attention Training: Design and Preliminary Evaluation. IEEE LATIN AMIRECA TRANSACTIONS, 20(5), 746–753. https://latamt.ieeer9.org/index.php/transactions/article/view/5835/1355
10. BITalino – PrototipadoLAB. (s.f.). PrototipadoLAB – by Paola Guimerans. https://prototipadolab.com/2018/08/06/bitalino/
11. U. Modi and P. Hwang, “6. Frontopolar sharp potentials,” Clin. Neurophysiol., vol. 127, no. 4, pp. e162–e163, 2016.
12. B. Schack, N. Vath, H. Petsche, H.-G. Geissler, and E. Möller, “Phase-coupling of theta-gamma EEG rhythms during short-term memory processing,” Int. J. Psychophysiol., vol. 44, no. 2, pp. 143–163, 2002.
13. A. Aldridge et al ., "Electroencefalogramas (EEG) accesibles: una revisión comparativa con los auriculares Ultracortex Mark IV de OpenBCI", 29.° Congreso Internacional Radioelektronika (RADIOELEKTRONIKA) de 2019 , Pardubice, República Checa, 2019, págs. 1 a 6, doi: 10.1109 /RADIOELEK.2019.8733482.
14. Millán, E., Jiménez, C., Ospina, D., & Henao, O. (2015). Caracterización del sensor EEG BR8 Plus: Verificación del estado base y los ritmos beta y theta utilizando la prueba Stroop de atención visual. Avances en Ingeniería, 172.
