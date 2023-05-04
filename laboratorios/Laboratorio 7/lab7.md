# **LABORATORIO 7: – Filtros**
Realizado el 3 de mayo de 2023

En el presente laboratorio se filtró las señales de ECG obtenidas en el laboratorio 4:
- Basal
- Respiración 1
- Respiración 2
- Post-Ejercicio


A continuación presentamos las gráficas obtenidas:
<div align="center">

|  **Campo**     | **Señal cruda** | **Filtro IIR** |  **Filtro FIR 1** |  **Filtro FIR 2** |
|:--------------:|:---------------:|:--------------:|:-----------------:|:-----------------:|
| Basal          |   <img width="300" height="250" src="https://user-images.githubusercontent.com/89707896/236255855-a51a2dbc-218e-47bb-994a-1fe34bb98898.jpeg">  |       <img width="300" height="250" src="https://user-images.githubusercontent.com/89707896/236256850-9c3e637e-8b25-4cbc-984f-f19a7127547f.jpeg">        |       <img width="300" height="250" src="https://user-images.githubusercontent.com/89707896/236259370-9c92b3b3-1a0c-4a89-90f8-0d90478d289e.jpeg">           |       <img width="300" height="250" src="https://user-images.githubusercontent.com/89707896/236260079-f7c08409-04bd-40a1-9613-e417371d9541.png">           |
| Respiración 1  |   <img width="300" height="250" src="https://user-images.githubusercontent.com/89707896/236255960-8d9e64a7-7821-418d-b876-e458bdb7fc53.jpeg">  |       <img width="300" height="250" src="https://user-images.githubusercontent.com/89707896/236257152-7e10cc31-534f-46f1-8ee8-37b18ed955ff.jpeg">        |       <img width="300" height="250" src="https://user-images.githubusercontent.com/89707896/236259038-376010de-864e-4112-9c55-b2faca169894.jpeg">           |       <img width="300" height="250" src="https://user-images.githubusercontent.com/89707896/236260079-f7c08409-04bd-40a1-9613-e417371d9541.png">           |
| Post-Ejercicio |   <img width="300" height="250" src="https://user-images.githubusercontent.com/89707896/236255188-492cc48d-24e5-4fa7-9805-bee75a721d1b.jpeg">  |       <img width="300" height="250" src="https://user-images.githubusercontent.com/89707896/236257867-b8b9a6ba-00b9-449b-b99f-a6531712ee59.jpeg">        |       <img width="300" height="250" src="https://user-images.githubusercontent.com/89707896/236259161-927fc0b4-de48-4ab7-9785-4cecbaf262e9.jpeg">           |       <img width="300" height="250" src="https://user-images.githubusercontent.com/89707896/236260079-f7c08409-04bd-40a1-9613-e417371d9541.png">           |

</div>
<p align="justify">
  -  El filtro en IIR corresponde al de Butterworth, se seleccionó dado que es un filtro que no presenta rizos; es decir, no introduce distorsiones en las frecuencias dentro de la banda de paso. Asimismo, como queremos preservar la forma de la onda de la señal este filtro es el indicado, ya que, presenta una fase lineal en la banda de paso, además de su alta capacidad de atenuación de las frecuencias no deseadas.
</p>
  
