</div>

<p align="justify">
<p align="center"><img src="https://i.postimg.cc/SsgzGz7b/1.png" width="600" height="266"></p>
</p>
Se muestra que tenemos 105 muestras donde 35 de ellas son para cada uno de los objetos (fingerboard con ruedas, sin ruedas y toycar)
</div>

<p align="justify">
<p align="center"><img src="https://i.postimg.cc/yWqtpWsv/2.png" width="400" height="266"></p>
</p>

Tratamos de tener un train/test split de 80/20 ya que es lo recomendado por edgeimpulse. Seguimos con “Create impulse” donde seleccionamos las siguientes configuraciones para nuestro modelo de ML.
</div>

<p align="justify">
<p align="center"><img src="https://i.postimg.cc/QxyJ3v7Z/3.png" width="800" height="300"></p>
</p>

Luego de generar los features de nuestro modelo obtenemos la siguiente gráfica, modelos ver que existe una dispersión en los resultados pero además podemos notar existe una tendencia a dónde se ubican en la gráfica las imagenes del fingerboard con ruedas, mientras el fingerboard sin ruedas y el auto de juguete se encuentran muy próximos.
</div>

<p align="justify">
<p align="center"><img src="https://i.postimg.cc/T3B0rB2J/4.png" width="300" height="300"></p>
</p>

Se muestra que tenemos 105 muestras donde 35 de ellas son para cada uno de los objetos (fingerboard con ruedas, sin ruedas y toy car).
</div>

<p align="justify">
<p align="center"><img src="https://i.postimg.cc/KvMR1WV2/5.png" width="400" height="300"></p>
</p>

Tratamos de tener un train/test split de 80/20 ya que es lo recomendado por edgeimpulse. Seguimos con “Create impulse” donde seleccionamos las siguientes configuraciones para nuestro modelo de ML.
</div>
<p align="justify">
<p align="center"><img src="https://i.postimg.cc/VLQbW1X6/6.png" width="800" height="300"></p>
</p>

Luego de generar los features de nuestro modelo obtenemos la siguiente gráfica, modelos ver que existe una dispersión en los resultados pero además podemos notar existe una tendencia a dónde se ubican en la gráfica las imagenes del fingerboard con ruedas, mientras el fingerboard sin ruedas y el auto de juguete se encuentran muy próximos.

</div>
<p align="justify">
<p align="center"><img src="https://i.postimg.cc/X7Rx5TYc/7.png" width="800" height="300"></p>
</p>

Luego de entrenar el modelo obtuvimos lo siguiente. Que teníamos una precisión del 100% y una pérdida del 0.17, así mismo podemos apreciar que la dispersión entre las clases es más notoria a comparación de la gráfica anterior.
</div>
<p align="justify">
<p align="center"><img src="https://i.postimg.cc/CK1NpYP0/8.png" width="400" height="500"></p>
</p>

Recordemos que nosotros realizamos nuestro dataset con ayuda de un smartphone por lo cual obtuvimos imágenes de la siguiente calidad: 

### **Training sample fb-con ruedas** 
</div>
<p align="justify">
<p align="center"><img src="https://i.postimg.cc/c1XLrST2/9.png" width="400" height="400"></p>
</p>

### **Training sample fb-sinruedas** 
</div>
<p align="justify">
<p align="center"><img src="https://i.postimg.cc/gcSGGK2P/10.png" width="400" height="400"></p>
</p>

### **Training sample toy car** 
</div>
<p align="justify">
<p align="center"><img src="https://i.postimg.cc/rpcB1dwJ/11.png" width="400" height="400"></p>
</p>

Adicionalmente con ayuda del arduino tinyML tomamos diferentes imágenes para poder correrlo como test data debido a que para la Live classification usaremos esta misma cámara, buscamos comprobar la calidad de los resultados. 
