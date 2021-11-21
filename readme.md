<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h1 align="center">ANIME SUGGESTOR</h3>
</p>

<!-- TABLE OF CONTENTS -->- [Tabla de contenidos:]
- [Descripcion:](#descripcion)
- [Modelo:](#modelo)
  - [Vertices:](#vertices)
  - [Aristas:](#aristas)
- [Implementación:](#implementacion)
  - [Recolección de datos:](#recoleccion-de-datos)
  - [Procesamiento de datos:](#procesamiento-de-datos)
  - [Muestra de datos:](#muestra-de-datos)
- [Resultado final:](#resultado-final)


## Descripcion
Se desarrollo una aplicación que con el uso de grafos ponderados es capaz de generar recomendaciones de series anime con base en los gustos del usuario, especificamente, en los interpretes de voz y generos de obras vistas previamente.
## Hardware: 
### Equipo:
#### Sensores: 
- Acelerometro: MPU-6050.
- Pulsometro: --.
#### Actuadores:
- Bluetooht: HC-05.
- Motor de vibracion: Lilypad vibe.
- Led: Lilypad LED.
#### Baterias:
- Powerbank generica.
- Lilypad LiPower - Baterias de litio.
#### Conexiones:
- Hilo conductor.
- Jummpers.
#### Arduino:
- Arduino Lilypad.
### Esquema del circuito.
![Esquema de conexión](/images/Esquema_final.jpg)



## Software:
- **Arduino**:

  Los programas `Hola mundo` de los sensores de pueden encontrar en la capeta [Sensores](/Sensores).

  El programa [main.ino](\main/main.ino) Se encarga de recolectar los datos de los sensores pulsometro y pulsioximetro de la siguiente manera: Se toman 1800 lecuras del acelerometro, una cada segundo (30 minutos) en donde si se calcula una posicion menor a 50° se generará una alerta, encendiendo el motor de vibracion y el LED. Al pasar las 1800 lecturas, se tomaran 10 lecturas del pulsometro las cuales se promediarán. Todos estos datos son enviados a traves del modulo Bluetooht.
  ### Formato de envio:
  - Lectura de posición: `gx`, `gy`, `gz`, `i`.
  - Lectura de pulso: `"p"`, `BPM`.
  - Alerta: `gx`, `gy`, `gz`, `i`, `a`.
  Donde: `gx`, `gy`, `gz` son la rotación en el eje respectivo, `BPM` es el pulso leído, `i` es un indicador booleano de alerta y `a` es el ángulo que genero dicha alerta.
- **Python - Comicación**:

  Los datos enviados por el arduino son leidos por el archivo llamado [prototipo1](/propotipo1.py), el cual cumple la función de decidir a que tabla de la base de datos asignarlo, esto se logra con los indicadores explicados anteriormente.
- **Postgres SQL**:

  La base de datos cuenta con un total de 5 tablas como se observa en la Imagen 2. El rol de la base de datos es fundamental, puesto que además de almacenar datos y tener eventos al modificar ciertas tablas, también permite una conexión entre la Aplicación Web y Arduino-Python.

  Puntualizando en las tablas, están Usuario, Pulsómetro, Género, Acelerómetro, y Notificaciones. Cada una cumple una función específica. La tabla Usuario almacena los datos de cada usuario como peso, estatura, etc. con el fin de poder aplicar correctamente las fórmulas como la de Karvonen. Las tablas Pulsómetro y Acelerómetro almacenan datos específicos de cada sensor para cada usuario. Finalmente, la tabla Notificaciones se explorará posteriormente en la sección Aplicación Web. 

  ![Diagrama Base de datos](/images/base_de_datos.jpeg)


## Página Web:

Una vez se encuentran almacenados los datos en la base, es indispensable generar una interfaz gráfica de tal modo que el usuario pueda interpretarlos, recibir alertas cuando sea necesario y poder acceder a la documentación sobre el dispositivo. Con esto en mente y buscando mantener la correcta sincronización lograda entre Arduino, el módulo Bluetooth, Python y SQL, se tomó la decisión de hacer una aplicación web, diseñada e implementada con la librería Dash de Python. Esta librería además de crear código HTML sin necesidad de archivos externos, permite generar distintos tipos de gráficos de análisis con información obtenida a través de consultas a la base de datos. 
             
Hacerla en html ofrece la posibilidad de que el modelo tenga una gran adaptabilidad a un uso comercial, ya que puede llevarse a la red usando un servidor en línea, y permitir su acceso desde casi cualquier dispositivo que cuente con un navegador web.
             
Una funcionalidad importante de la aplicación web es la posibilidad de mandar notificaciones al usuario cuando sea necesario. 
Esta notificación se ejecuta cuando hay una nueva inserción en la tabla Notificaciones y toma el valor de la columna 'Mensaje'. Cabe resaltar que la tabla Notificaciones tiene las siguientes tres columnas:
- Usuario.
- Fecha.
- Mensaje.

Sin embargo, como las notificaciones solo se ejecutan al momento de inserción, es necesario revisar constantemente el estado de la Tabla. Esto se logra mediante una función en la aplicación web llamada "manage notifications". Específicamente se utiliza un thread adicional que ejecuta sentencias de count a la tabla Notificaciones para un usuario específico.

![Notificación](/images/notifi.jpeg)
## Resultado final:
![Prototipo Final](/images/prototipo.jpeg)
![Prototipo Final 2](/images/iniciopagina.jpeg)
