# **LABORATORIO 7: – Filtros**
Realizado el 3 de mayo de 2023

En el presente laboratorio se filtró las señales de ECG obtenidas en el laboratorio 4:
- Basal
- Respiración 1
- Respiración 2
- Post-Ejercicio


A continuación presentamos las gráficas obtenidas:
<div align="center">

| Campo | Señal Cruda | Filtro IIR | Filtro FIR 1 | Filtro FIR 2|
|----------|----------|----------|----------|----------|
| Basal    | <img width="300" height="150" src="https://user-images.githubusercontent.com/89707896/236255855-a51a2dbc-218e-47bb-994a-1fe34bb98898.jpeg"> |  <img width="300" height="150" src="https://user-images.githubusercontent.com/89707896/236256850-9c3e637e-8b25-4cbc-984f-f19a7127547f.jpeg">    | <img width="300" height="150" src="https://user-images.githubusercontent.com/89707896/236259370-9c92b3b3-1a0c-4a89-90f8-0d90478d289e.jpeg">     | <img width="300" height="150" src="https://user-images.githubusercontent.com/89707896/236266646-f7c04a23-c12e-42bd-8224-8c7c811ec986.jpeg">     |
| Post-Ejercicio    | <img width="300" height="150" src="https://user-images.githubusercontent.com/89707896/236255188-492cc48d-24e5-4fa7-9805-bee75a721d1b.jpeg">  |       <img width="300" height="150" src="https://user-images.githubusercontent.com/89707896/236257867-b8b9a6ba-00b9-449b-b99f-a6531712ee59.jpeg">        |       <img width="300" height="150" src="https://user-images.githubusercontent.com/89707896/236259161-927fc0b4-de48-4ab7-9785-4cecbaf262e9.jpeg">           |       <img width="300" height="150" src="https://user-images.githubusercontent.com/89707896/236266762-581677c3-907a-49ba-a01d-aebc662e3eab.jpeg">           |
| Respiracion   | <img width="300" height="150" src="https://user-images.githubusercontent.com/89707896/236255960-8d9e64a7-7821-418d-b876-e458bdb7fc53.jpeg">  |       <img width="300" height="150" src="https://user-images.githubusercontent.com/89707896/236257152-7e10cc31-534f-46f1-8ee8-37b18ed955ff.jpeg">        |       <img width="300" height="150" src="https://user-images.githubusercontent.com/89707896/236259038-376010de-864e-4112-9c55-b2faca169894.jpeg">           |       <img width="300" height="150" src="https://user-images.githubusercontent.com/89707896/236266786-6f067e29-d190-490c-a5ef-ecae7316c239.jpeg">           |


</div>
<p align="justify">
¿Por qué se eligieron estos filtros?
  
- Filtro IIR (Butterworth): Es un filtro que no presenta rizos; es decir, no introduce distorsiones en las frecuencias dentro de la banda de paso. Asimismo, como queremos preservar la forma de la onda de la señal este filtro es el indicado, ya que, presenta una fase lineal en la banda de paso, además de su alta capacidad de atenuación de las frecuencias no deseadas.

- Filtro FIR 1 (Hamming): El diseño de filtros hamming en python no es complejo. Este tipo de filtro no presenta oscilaciones en la respuesta en frecuencia y es posible controlar los parámetros de este de forma precisa. Asimismo, la pendiente en la banda de paso no es demasiada como para que deje de filtrar señales a frecuencias no deseada. Además, la atenuación de las señales de frecuencias más altas es lo suficiente pequeña en relación con la región de transición. Es decir, esta región no es muy grande comparada con otros tipos de filtros FIR, y la atenuación es suficiente para que las señales filtradas no se muestren.

- Filtro FIR 2 (Blackman): El filtro blakman tiene una caida mas pronunciada a comparación del Hamming o Hanning, esto quiere decir que su ancho de banda es menor al de los otros. Por lo que permitiria aumentar la resolución de una región mas especifica de la señal asi como disminuir la filtración espectral.

</p>
  
