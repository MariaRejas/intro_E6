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
Encontramos que solo para el caso de fbconruedas-2, el modelo no puede determinar que objeto es, procederemos a adjuntar las imágenes:

</div>
<p align="justify">
<p align="center"><img src="https://i.postimg.cc/yNVGJwLp/12.png" width="600" height="400"></p>
</p>

</div>
<p align="justify">
<p align="center"><img src="https://i.postimg.cc/mD0fFmzc/13.png" width="600" height="400"></p>
</p>

</div>
<p align="justify">
<p align="center"><img src="https://i.postimg.cc/XYvH4wqt/14.png" width="600" height="400"></p>
</p>

</div>
<p align="justify">
<p align="center"><img src="https://i.postimg.cc/TPLtWfr9/15.png" width="600" height="400"></p>
</p>

</div>
<p align="justify">
<p align="center"><img src="https://i.postimg.cc/8PpwmhRs/16.png" width="600" height="400"></p>
</p>

</div>
<p align="justify">
<p align="center"><img src="https://i.postimg.cc/yNZT8nHp/17.png" width="600" height="400"></p>
</p>

En la siguiente tabla podemos ver los resultados obtenidos
</div>
<p align="justify">
<p align="center"><img src="https://i.postimg.cc/YSY1H96J/19.png" width="600" height="400"></p>
</p>

El modelo nos da un 95,83% como resultado del modelo
</div>
<p align="justify">
<p align="center"><img src="https://i.postimg.cc/J76HSZws/20.png" width="600" height="600"></p>
</p>
Luego probamos con la cámara del arduino tinyML y realizamos algunos test en vivo para cada caso de objeto. A continuación mostramos un screenshot para el test en vivo con cámara de arduino para el caso de fb-con ruedas.

</div>
<p align="justify">
<p align="center"><img src="https://i.postimg.cc/rmhzXXPB/21.png" width="800" height="600"></p>
</p>

Mostraremos los casos con ayuda de videos.
### ***Video fb-con ruedas**
<video src="https://user-images.githubusercontent.com/89707896/231572641-61aeebae-f397-4627-aebc-913bb9464915.mp4" width="200" /> | <video src="https://user-images.githubusercontent.com/89707896/231574043-44222491-d595-4d5a-9ac8-112adb20757c.mp4" width="200" /> 

<video src="https://github.com/MariaRejas/intro_E6/assets/55772705/0f565868-d1d3-46a5-9fd3-4d2674729a6c" width="200" /> | <video src="https://user-images.githubusercontent.com/89707896/231574043-44222491-d595-4d5a-9ac8-112adb20757c.mp4" width="200" /> 


Similar al screenshot que se muestra arriba podemos encontrar que para este test obtuvimos un 0.86 para fb-con ruedas, lo cual concuerda con el resultado esperado.




### ****Video fb-sin ruedas**

En el video podemos apreciar que obtenemos un 0.95 para fb-sin ruedas, que concuerda con el resultado esperado.


https://github.com/MariaRejas/intro_E6/assets/55772705/eefeee81-aa6f-4b9f-ae41-491160551ba5


### ****Video toy card**


https://github.com/MariaRejas/intro_E6/assets/55772705/f61dc573-c719-47aa-875e-c98c3a904249


Finalmente para este caso, obtenemos un 0.97 para toy card e igualmente que los dos ejemplos anteriores en caja con el resultado esperado.
