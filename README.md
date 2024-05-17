# RM.APItoMySQL

Este proyecto es un script de Python diseñado para extraer información de la API de "Rick and Morty" y cargarla en una base de datos MySQL. El script obtiene datos de los episodios de la serie y almacena los nombres, especies y estados de los personajes en una tabla MySQL, evitando duplicados. Este proyecto es ideal para aprender sobre la integración de APIs con bases de datos y manejo de datos en Python.

> Nota: Actualmente, me encuentro estudiando la carrera de Data Engineer. Como todo aventurero, decidí meter mano en un simple código de manipulación de datos mediante el uso de una API, en este caso, la de una serie de TV. Recientemente, empecé a ver Bases de Datos relacionales y quería ver qué sucedía si aplicaba un poco de esto a la exploración de datos, ya que he visto que muchos primero generan un archivo para luego pasarlo a la base de datos. Sin embargo, se me ocurrió ver qué pasaría si creaba un script que los insertara de una sola vez en MySQL. También investigué cómo podía hacer para que los personajes no se repitieran en la base de datos, ya que eso me sucedía al principio. Más allá de eso, espero que les guste y les sea de utilidad a todos, ya que quizás cambiando algún que otro parámetro puedan incorporarlo a sus proyectos.

## Características:

    Conexión y manipulación de datos en MySQL.
    Uso de la API de "Rick and Morty" para obtener información de episodios y personajes.
    Inserción de datos en la base de datos con manejo de duplicados.
    Transformación y normalización de datos (traducción de especies y estados).

## Requisitos:

    Python 3.x
    requests
    mysql-connector-python

## Cómo usar:

    Clona el repositorio.
    Configura las credenciales de tu base de datos MySQL en el script.
    Ejecuta el script para poblar la base de datos con la información de "Rick and Morty".
