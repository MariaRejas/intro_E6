# **LABORATORIO 5 PARTE 2: – Uso de Ultracortex y BiTalino para EEG**
Realizado el 19 de abril de 2023
<p align="center">
     <img width="500" height="300" src="https://images.squarespace-cdn.com/content/v1/5f7b55a801226812a44f7180/1609441748072-S5NU5R5YSQF4LYBO7KZT/OpenBCI-WebXR-EEG.gif">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/17307/31218894-586281e4-a9c4-11e7-81d8-bd6f3dfd4267.gif">
</p>

# **Tabla de contenidos**
  5.4 [Ploteo de la señal en Python](#id8)\
  5.5 [Archivos](#id9)

6. [Análisis de la señal EEG con Ultracortex](#id10)\
  6.1 [Conexión usada](#id11)\
  6.2 [Procedimiento](#id12)\
  6.3 [Videos de la señal](#id13)\
  6.4 [Ploteo de la señal en OpenBCI](#id14)\
  6.5 [Ploteo de la señal en Python](#id15)\
  6.6 [Archivos](#id16)
7. [Conclusiones](#id17)
8. [Referencias](#id18)

### **Ploteo de la señal en tiempo y frecuencia en Python** <a name="id8"></a>
---

a) Registro de ojos abiertos:
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707896/233435534-127743c3-b838-42a4-9e89-a6ecc3f1d1f3.png">
</p>
<p align="center">
<img width="500" height="400" src="https://user-images.githubusercontent.com/89707896/233439133-4e5b1aa6-027c-4258-bbea-e636d4a65388.png">
</p>

Análisis:
En este la señal oscila su amplitud entre 600 y 425.
</p>

b) Registro de ojos cerrado:
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707896/233436145-77ea47c1-b1b0-41c0-8a16-e9290dcd5a55.png">
</p>

<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707896/233439372-ab14d194-e4e2-4668-a8d4-749c7b9369cc.png">
</p>
Análisis:
<p align="justify">
En este la señal oscila su amplitud entre 620 y 430 con algunos picos que superan los 700. En su análisis por frecuencias encontramos una mayor amplitud entre 0-25 Hz.
Los ritmos que destacan son principalmente los beta indicando una mayor actividad de la región parietal y frontal. Estos aparecen en estados de atención o en problemas cotidianos. Estos a la vez  se dividen en tres beta 1,2 y 3, sin embargo en la gráfica podemos observar que destacan las ondas Beta 2(15-22 Hz) lo que indicaría que el voluntario está atento a  cumplir la tarea. Al mismo tiempo, esta respuesta va acorde a la acción realizada ya que a pesar de lo simple del ejercicio el mantener los ojos abiertos permite mantener un estado de alerta y atención en una tarea específica. 
</p>

</p>

c) Registro de ojos con exposición a luz (linterna)
<p align="justify">
Análisis:
</p>

<p align="justify">
Las ondas que destacan son principalmente las Delta(0.2-4 Hz) pero también encontramos una alta actividad de ondas Alfa y de ondas Beta 1. La actividad de las ondas Delta indicaría una actividad cerebral similar al del tiempo de sueño, esto va acorde a la actividad, ya que al mantener los ojos cerrados se limitan el resto de estímulos y se induce a un estado similar a la del sueño. Sin embargo, la actividad de las ondas Alfa indicarían actividad en la región occipital en el cual  a pesar del reposo el cuerpo se encuentra en un estado de atención, esto va acorde a la actividad ya que el voluntario se encuentra expectante a cumplir los 30 segundos de la actividad.
</p>
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707896/233440545-7a638e07-4b30-491a-b5b3-cf2903a15524.png">
</p>
<p align="justify">
En este caso las frecuencias destacan en los rangos de 0.2-4 Hz y de 12-15 Hz, sin embargo a comparación de los casos anteriores en donde la actividad era constante en este se sometió al voluntario a estímulos variables a lo largo del tiempo. Por ello la actividad en el rango de frecuencias de 15 hasta 25 alcanzan valores mínimos de magnitud. Sin embargo, estos vuelven a aumentar a los 30 Hz. Por lo tanto, las ondas mas destacadas en el ejercicio son la Delta y Beta 1 y 3. 
Asimismo, en el ejercicio uno de los ojos se mantuvo tapado lo que explicaría la presencia de ondas Delta. Mientras que la información recibida desde el ojo abierto aumentaría la actividad frontal y parietal al estar sometido a un estado de excitación o ansiedad, este estado se vería representado por la luz de la linterna.
</p>


d) Registro de memoria
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707896/233437078-a52679d2-54c3-4a41-82e1-2f9a68aba8e8.png">
</p>
<p align="justify">
Análisis:
En este la amplitud osciló entre 450 Y 600 con picos que superan los 650 .Mientras que las frecuencias más destacadas se encontraron entre 0 y 25 Hz.
</p>

e) Registro de razonamiento de un problema matemático
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707896/233438470-38edfe1e-7f6b-4ab0-9307-37dd809a14c6.png">
</p>
<p align="justify">
Análisis:
En este caso la señal varía su amplitud entre 450 y 650 ciertos picos de 700 o superiores y valles menores a 300. 
</p>

### Análisis de las gráficas FFT
a) Registro de ojos abiertos:
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707896/233439133-4e5b1aa6-027c-4258-bbea-e636d4a65388.png">
</p>
b) Registro de ojos cerrado:

c) Registro de ojos con exposición a luz (linterna)
<p align="justify">
Las ondas que destacan son principalmente las Delta(0.2-4 Hz) pero también encontramos una alta actividad de ondas Alfa y de ondas Beta 1. La actividad de las ondas Delta indicaría una actividad cerebral similar al del tiempo de sueño, esto va acorde a la actividad, ya que al mantener los ojos cerrados se limitan el resto de estímulos y se induce a un estado similar a la del sueño. Sin embargo, la actividad de las ondas Alfa indicarían actividad en la región occipital en el cual  a pesar del reposo el cuerpo se encuentra en un estado de atención, esto va acorde a la actividad ya que el voluntario se encuentra expectante a cumplir los 30 segundos de la actividad.
</p>
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707896/233440545-7a638e07-4b30-491a-b5b3-cf2903a15524.png">
</p>
<p align="justify">
En este caso las frecuencias destacan en los rangos de 0.2-4 Hz y de 12-15 Hz, sin embargo a comparación de los casos anteriores en donde la actividad era constante en este se sometió al voluntario a estímulos variables a lo largo del tiempo. Por ello la actividad en el rango de frecuencias de 15 hasta 25 alcanzan valores mínimos de magnitud. Sin embargo, estos vuelven a aumentar a los 30 Hz. Por lo tanto, las ondas mas destacadas en el ejercicio son la Delta y Beta 1 y 3. 
Asimismo, en el ejercicio uno de los ojos se mantuvo tapado lo que explicaría la presencia de ondas Delta. Mientras que la información recibida desde el ojo abierto aumentaría la actividad frontal y parietal al estar sometido a un estado de excitación o ansiedad, este estado se vería representado por la luz de la linterna.
</p>

d) Registro de memoria
</p>
e) Registro de ejercicio
<p align="center">
     <img width="500" height="400" src="https://user-images.githubusercontent.com/89707896/233441116-6d0dc378-c755-4574-a05f-2dd79b3852f9.png">
</p>
<p align="justify">
En el análisis por frecuencias encontramos una alta actividad en las frecuencias de 0.4-4 Hz y de 15 a 20 Hz lo que indicaría una mayor presencia de ondas delta y beta 2. La presencia de ondas beta 2 indicaría la alta actividad por parte del lóbulo frontal encargado de funciones cognitivas, al estar sometido a una tarea altamente compleja. Sin embargo, durante las experimentación el voluntario tampoco realizó el problema de forma completamente mental debido a que lo hizo hablando con voz alta. Asimismo, casi al final del ejercicio este fue interrumpido. A pesar de ello incluso en la gráfica Amplitud vs. Con el tiempo son visibles los picos de actividad debido a la pregunta compleja. 
</p>

### **Archivos** <a name="id9"></a>
Se encuentran en la carpeta del laboratorio 5.
#

## **Análisis de la señal EEG con Ultracortex** <a name="id10"></a>

## **Conexión usada** <a name="id11"></a>
Ultracortex: 
Con los ojos cerrados
Con los ojos abiertos y cerrados cada 5 segundos
Descanso de 30 segundos
Tras realizar un problema matemático
Tras realizar un ejercicio simple
##**Procedimientos**<a name="id12"></a>
<p align="justify">
La colocación de los 16 electrodos está de acuerdo con la configuración del sistema 10-20,por lo cual la ubicación es la siguiente: AF3, AF4, F7, F3, F4, F8, T7, C3,C4, T8, P7, P3, P4, P8, O1, O2 como se indica con nodos coloreados en la Fig. 9.Así mismo los electrodos de referencia (barra de resistencia superficial - SRB) y de tierra (Bias) se colocaron en la oreja izquierda y derecha, respectivamente. Los headsets Mark IV de 16 canales funcionaron a una frecuencia de muestreo de 125 Hz.</p>
<p align="center">
     <img width="400" height="300" src="https://user-images.githubusercontent.com/89707896/233443718-3bb5e437-ca15-4c20-9b96-161e88d367a1.png">
</p>
<p align="center">
Figura 9.Ubicación de los electrodos por colores [13].
</p>

<p align="center">
     <img width="400" height="300" src="https://user-images.githubusercontent.com/89707896/233444811-fa8a818b-0f62-4931-ba6c-8960a7975086.png">
</p>
<p align="center">
Figura 10.Colocación de los electrodos en el participante según  el sistema 10-20. [Elaboración propia]
</p>

## **Video de la señal** <a name="id13"></a>
| Ojos cerrados (30 segundos) | Ojos abiertos y cerrados cada 5 segundos |
| ------------ |  :------------------------------------: |
| <video src="https://user-images.githubusercontent.com/89707896/233442308-de4777a2-3905-44e2-af35-e8746f135485.mp4" width="200" /> | <video src="https://user-images.githubusercontent.com/89707896/233442497-0aa75cf9-b259-4a4d-a311-e5f739a25960.mp4" width="200" /> |
</div>

| Problema matemático | Ejercicio simple |
| ------------|  :------------------------------------: |
| <video src="https://user-images.githubusercontent.com/89707896/233442765-5d02bcae-2369-440f-a0b1-012d3ee6a1c2.mp4" width="200" /> | <video src="https://user-images.githubusercontent.com/89707896/233442836-6cbd091a-8c92-460c-ad9c-0b920519a1a7.mp4" width="200" /> |
</div>



## **Ploteo de la señal en OpenBCI** <a name="id14"></a>

## **Ploteo de la señal en Python** <a name="id15"></a>

## **Archivos** <a name="id16"></a>

## **Conclusiones** <a name="id17"></a>
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
----
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
