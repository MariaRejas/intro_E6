# Bienvenidos al repositorio del Grupo 6 del curso : "Introducción a Señales Biomédicas"
## Proyecto: ANÁLISIS DE SEÑALES DE ELECTROMIOGRAMA

#### *Proyecto realizado por estudiantes de la carrera de Ingeniería Biomédica, pertenecientes a la Pontificia Universidad Católica del Perú (PUCP) y la Universidad Peruana Cayetano Heredia (UPCH), en el semestre 2023-1*

<p align="center">
  <img width="500" height="400" src="https://i.postimg.cc/Njm7463m/Whats-App-Image-2023-03-29-at-19-41-08.jpg">
</p>


-**Descripcion del curso**: Desarrollo y analisis del tratamiento de señales provenientes de dispositivos médicos relacionados a sistemas fisiológicos con el fin de crear simulaciones.


<p align="center">
  <img width="220" height="100" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6ya1d0H7YLeihci8A-LiSkSsiT-c08azerg&usqp=CAU">
  <img width="220" height="100" src="https://www.my-ekg.com/imag/sindrome-coronario-agudo.png">
</p>


## Tabla de contenidos:

* [¿Qué es una bioseñal?](https://github.com/MariaRejas/intro_E6/blob/main/README.md#qu%C3%A9-es-una-biose%C3%B1al)

* [Contenido del curso](https://github.com/MariaRejas/intro_E6/blob/main/README.md#contenido-del-curso)

* [Metodología](https://github.com/MariaRejas/intro_E6/blob/main/README.md#metodolog%C3%ADa)

* [Temática del proyecto](https://github.com/MariaRejas/intro_E6/blob/main/README.md#tem%C3%A1tica-del-proyecto)

* [Materiales](https://github.com/MariaRejas/intro_E6/blob/main/README.md#materiales)

* [Participantes](https://github.com/MariaRejas/intro_E6/blob/main/README.md#participantes)
  
* [Docentes del curso](https://github.com/MariaRejas/intro_E6/blob/main/README.md#docentes)

* [Laboratorios](#id1)
  
* **Señal de interés:** electromiograma 


## ¿Qué es una bioseñal?
<p align="justify">
Es aquella señal medida y controlada en los seres biológicos, de muy bajo potencial eléctrico en orden de mV, sometidos a ruido, perjudicando su observación y presentación en el análisis médico del paciente. Como ejemplo de ella tenemos a la señal biomédica obtenida del corazón por medio de un electrocardiograma (ECG), la señal recibida por el electroencefalograma (EEG) que mide la actividad eléctrica en el cerebro por medio de electrodos colocados sobre el cuero cabelludo o un electromiograma (EMG), nuestra señal de estudio, que verifica la salud de los músculos y los nervios que controlan. De modo que, estas señales permiten informar si un órgano o sistema biomédico precisa ayuda en cuanto a su estado o situación, facilitando su diagnóstico y permitiendo el respectivo tratamiento.
</p>
<p align="center">
  <img width="200" height="400" src="https://my.clevelandclinic.org/-/scassets/images/org/health/articles/4825-electromyography">
</p>


## Contenido del Curso
El proyecto se desarrollará siguiendo las 4 unidades del curso:
<p align="center">
    <img width="500" height="700" src="https://upchlabib.com/wp-content/uploads/2023/03/contenidos-1.png">
  </p>
  
  

## Metodología

## Temática del Proyecto
<p align="justify">
La obtención del electromiograma (EMG), se da por medio de un procedimiento de diagnóstico que evalua la salud de los músculos, tanto en reposo como en actividad, y las células nerviosas que los controlan. Para ello, se puede obtener la señal por un electrodo de aguja, que ingresa en el músculo a evaluar, o por parches de electrodos, que van en la superficie de la piel posicionados sobre el músculo de interés; siendo el último empleado para los fines académicos en el presente proyecto. 

Como la señal emitida por el electromiograma está en el orden de los mV se tiene que amplificar, para posteriormente ser filtrada, eliminando el ruido, y así obtener la información deseada.
</p>



## Materiales
<div align="center">


|   **Dispositivo**   | **Descripción** |  **Imagen**  |
|:-------------------:|:---------------:|:------------:|
| Arduino nano 33 IoT | Es una placa de desarrollo de tamaño reducido que integra capacidades de conectividad inalámbrica, procesamiento de datos y sensores, diseñada para proyectos de Internet de las cosas (IoT), que requieren de baja potencia y alta eficiencia energética |<img width="200" height="150" src="https://i.postimg.cc/wMSnyzCJ/arduino-nano-33-iot.webp">|
|       BITalino      | Es un kit de herramietnas de prototipado rápido para proyectos de salud y bienestar personal, Incluye sensores inalámbricos y una plataforma de software para adquirir, procesar y visualizar datos biomédicos |<img width="200" height="150" src="https://i.postimg.cc/VvLXqb8P/14022-01a.jpg">|
|  Arduino TinyML Kit | Es un paquete de hardware y software que permite a ,os usuarios implementar aprendizaje automático en dispositivos pequeños y de bajo consumo de energía, utilizando la plataforma Arduino y Edge Impulse |<img width="200" height="150" src="https://i.postimg.cc/XYMp3yzN/AKX00028-00-default.jpg">|


</div>



## Participantes
  - María Cristina Orihuela Flores: Estudiante de séptimo ciclo de Ingeniería Biomédica interesada en el área de Ingeniería de Tejidos y biomateriales (colaboradora) - maria.orihuela@upch.pe
  <p align="center">
    <img width="150" height="200" src="https://i.postimg.cc/jjX8YGb5/Foto-Cristina-Orihuela.png">
  </p>
  
  - Fabricio Nava Castañeda: Estudiante de séptimo ciclo de la carrera de Ingeniería Biompedica. Interesado principalmente en las área de Biomecánica y Rehabilitación (colaborador) - fabricio.nava@upch.pe
  <p align="center">
    <img width="150" height="200" src="https://i.postimg.cc/rwhCq50t/Whats-App-Image-2023-04-04-at-20-58-57.jpg">
  </p>
  
  - María Angélica Rejas Núñez: Estudiante de séptimo ciclo, interesada en el área de Ingeniería de Biomecánica y Rehabilitación (colaboradora) - maria.rejas@upch.pe
  <p align="center">
    <img width="150" height="200" src="https://i.postimg.cc/VNDJz5yd/foto.png">
  </p>

  - Alexandra Juneth Cordero Donaire: Estudiante de octavo ciclo, interesada en el rumbo de caracterizacion de materiales e ingenieria clinica (colaboradora) - alexsandra.cordero@upch.pe
   <p align="center">
    <img width="150" height="200" src="https://i.postimg.cc/XqMrVYk5/Imagen1.png">
  </p>
  
  - Alonso Bryan Castañeda Moron: Estudiante de octavo ciclo, interasado en ingenieria clinica (colaborador) - alonso.castaneda@upch.pe
  <p align="center">
    <img width="150" height="200" src="https://i.postimg.cc/WzQwcVhY/Whats-App-Image-2023-04-04-at-20-58-13.jpg">
  </p>
  
  - Leonardo Sebastián Sandoval Carranza: Estudiante de séptimo ciclo de Ingeniería Biomédica interesado en el área de Señales e imagenes biomedicas (colaborador) - leonardo.sandoval@upch.pe
    <p align="center">
      <img width="150" height="200" src="https://i.postimg.cc/ryNj0h0w/Whats-App-Image-2023-02-12-at-3-14-04-AM-1.png">
    </p>
    
## Docentes
  -  Lewis De La Cruz - umbert.de.la.cruz@upch.pe
  -  Moises Meza - moises.meza@upch.pe
  -  José Alonso Cáceres - jo.alonsok@gmail.com
  -  Julissa Venancio - julissa.venancio@upch.pe

## Laboratorios <a name="id1"></a>
  - [Laboratorio 3](https://github.com/MariaRejas/intro_E6/blob/main/laboratorios/lsab3/entregable3.md) : EMG
  - [Laboratorio 4](https://github.com/MariaRejas/intro_E6/blob/main/laboratorios/laboratorio4/lsb4.md) : ECG
  - [Laboratorio 5](https://github.com/MariaRejas/intro_E6/blob/main/laboratorios/laboratorio5/lsb5.md) : EEG
  - [Laboratorio 6](https://github.com/MariaRejas/intro_E6/tree/main/laboratorios/laboratorio6)
```python
print("Hola, Biomédicos :D")
