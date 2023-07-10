## Bienvenidos al repositorio del Grupo 6 del curso : "Introducción a Señales Biomédicas
# Project: Analysis of EEG signals of blinking patterns in order to control a wheelchair for people with ALS
# Proyecto: Análisis de señales EEG de patrones de parpadeo para controlar una silla de ruedas para personas con ELA

<p align="center">
  <img width="500" height="400" src="https://github.com/MariaRejas/intro_E6/assets/89707896/ad74b0ff-496d-4e6c-b7b9-3e14765cac55">
 </p>

#### *Proyecto realizado por estudiantes de la carrera de Ingeniería Biomédica, pertenecientes a la Pontificia Universidad Católica del Perú (PUCP) y la Universidad Peruana Cayetano Heredia (UPCH), en el semestre 2023-1*

-**Resumen :**
La esclerosis lateral amiotrófica (ELA) es una enfermedad neurodegenerativa progresiva que afecta el control de los músculos voluntarios y carece de una cura conocida.[1] Las interfaces cerebro-computadora (BCI) han surgido como una solución potencial para mejorar la calidad de vida de los pacientes con ELA. [2] Se enfocó en el uso de señales de electroencefalograma (EEG) para desarrollar mecanismos de control de sillas de ruedas eléctricas. Se destacan tres estudios significativos, cada uno con enfoques y limitaciones únicas. El estudio de Montesano [3] implementa una interfaz de pantalla táctil, pero no fue adecuado para pacientes completamente paralizados. La investigación de Galán [4], que utilizó señales de EEG con 64 canales, obtuvo resultados de baja calidad para individuos paralíticos. El estudio de Tanaka [5], que empleó 15 electrodos, no fue adecuado para un uso práctico.

-**Características de la enfermedad ELA:**
  Enfermedad neurodegenerativa progresiva.
  - Prevalencia entre pacientes de 80 y 89 años [6].
  - Etiología: Factores genéticos y hereditarios, pero aún se   desconoce. 
  - Patogenia: Degeneración y atrofia de neuronas motoras y debilidad muscular progresiva. 
  - Manifestaciones clínicas: debilidad muscular, afecta la deglución [7].
  - Incidencia estandarizada: 1.68 por 100 000 personas al año [8]
  - Mortalidad (2016): 49 muertes [9]
  - 3° enfermedad neurodegenerativa con mayor incidencia [10]
  - Promedio de vida: 2 - 5 años desde el diagnóstico [11]


-**Motivación:**
Al realizar una revisión bibliográfica sobre la tecnología BCI para la mejora de calidad de vida para personas que sufren ELA se encontró el siguiente problema: "La ausencia de un dataset que permita controlar una silla de ruedas de una forma sencilla y práctica por medio de señales EEG y sin ninguna interfaz inalámbrica, para poder mejorar la calidad de vida del paciente con la enfermedad de ELA."

-**Principales hallazgos (español)**
Como propuesta de solución, se presentó una metodología basada en el análisis de señales de ojos abiertos y cerrados, así como de pestañeos cortos y largos. Se realizaron diferentes etapas, como la obtención y procesamiento de las señales EEG, la extracción de características y la clasificación de las señales para generar comandos de movimiento de la silla de ruedas. Además, se utilizó la entropía espectral de potencia como característica para distinguir los pestañeos cortos y largos. Se creó un dataset que almacenó la señal filtrada de cada ejercicio y los parámetros relevantes. En los resultados, se observó que el valor del parámetro "w" fue mayor cuando los participantes tenían los ojos cerrados, lo que permitió traducir estos patrones en acciones específicas. Asimismo, se demostró la efectividad del algoritmo en la detección de pestañeos cortos y largos mediante la característica de entropía espectral de potencia. En conclusión, aunque se encontraron artefactos en las señales debido al estado de los electrodos, la metodología propuesta mostró prometedoras diferenciaciones y resultados más óptimos en la clasificación de las señales de pestañeos.

-**Problemática**
"La ausencia de un dataset que permita controlar una silla de ruedas de una forma sencilla y práctica por medio de señales EEG y sin ninguna interfaz inalámbrica, para poder mejorar la calidad de vida del paciente con la enfermedad de ELA."

- **Publico objetivo:**
Jovenes entre 18 a 24 años de edad.



-**Referencias:**</p>
[6] E.Gakidou et al.,”Global, regional and national comparative risk assessment of 84 behavioural, environmental and 
occupational and metabolic risks or clusters of risks,1990-2016: A systematic analysis for the Global Burden of Disease Study 
2016”, Lancet, vol. 390, no. 10100, pp. 1345-1422,2017,doi:10.1016/S0140-6736(17)32366-8
[7] A. Verma, “Clinical manifestation and management of amyotrophic lateral sclerosis,” Amyotrophic Lateral Sclerosis, pp. 1–14, 
2021. doi:10.36255/exonpublications.amyotrophiclateralsclerosis.management.2021 
[8] Moro and P. Fondazione, “Global, regional, and national burden of motor neuron diseases 1990-2016: a systematic analysis 
for the Global Burden of Disease Study 2016 GBD 2016 Motor Neuron Disease Collaborators*,” Lancet Neurol, vol. 17, pp. 
1083–97, 2018.
[9] Esclerosis lateral amiotrófica ELA / Enfermedad de Charcot / Enfermedad de Lou Gherig / Enfermedad de la motoneurona, 
2nd ed. United Kingdom: OrphaNet, 2021, p. pag 1.
https://neuroalianza.org/wp-content/uploads/Informe-NeuroAlianza-Completo-v-5-optimizado.pdf
[10] E. Gakidou et al., “Global, regional, and national comparative risk assessment of 84 behavioural, environmental and 
occupational, and metabolic risks or clusters of risks, 1990-2016: A systematic analysis for the Global Burden of Disease Study 
2016,” Lancet, vol. 390, no. 10100, pp. 1345–1422, 2017, doi: 10.1016/S0140-6736(17)32366-8.
[11] ALS Facts and Statistics – ALS News Today. (2017). ALS News Today. 
https://alsnewstoday.com/als-facts-statistics/#:~:text=More%20than%20half%20of%20all,live%2020%20years%20or%20more.

