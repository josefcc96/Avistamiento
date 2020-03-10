Utilize el framework de Django para la creacion del sistema de informacion,dentro del repositorio se encuentra el archivo requeriments.txt donde se encuentran todos los paquetes utilizados para el desarrollo las bases de datos se encuentran creadas en postgrest.
Para hacer uso de la plataforma es necesario crear un superusuario con el siguiente comando

python manage.py createsuperuser
En donde se nos solicitara un nombre y contraseña.
La base de datos principal se llama invemar y su dueño es el usuario jose, en esta se encuentran las relaciones entre los diferentes listados. Para la creacion se utilizo el siguiente script.

"$ psql -U postgres -W "
"# CREATE USER jose;"
"# CREATE DATABASE invemar OWNER jose;"

La contraseña por defecto del usuario jose es 1234.

Al ejecutar el comando  "python manage.py makemigrations" con el entorno virtual activado, se crean las respectivas tablas en la base de datos antes configurada. Al ejecutar "python manage.py migrate" los modelos se actualizan y se cargan a la base de datos  

En este caso las tablas Lugar y Avistamiento tienen una relacion de muchos a uno, debido a que considere que pueden exisitir varios avistamientos en un solo lugar ya que esta tabla tiene informacion mas general y las coordenadas se encuentran en el modelo de avistamiento.
En el caso de las tablas Avistamiento y Especie la relacion es de muchos a muchos debido a que una especie puede haberse encontrado en muchos Avistamientos y viceversa, puede que se hayan encontrado varias especies en un avistamiento.
