# TFG_Gantt
Se ha probado en Ubuntu 20.04 y CentOS 8 pero debería funcionar en otro sistemas UNIX

## Dependencias
Python3
Instalar Python3
Ubuntu:
sudo apt-get update
sudo apt-get install python3
CentOS/RHEL:
sudo yum install python3
Para otros sistemas operativos:
https://www.python.org/downloads/

Ruby
Instalar Ruby
Ubuntu:
sudo apt-get update
sudo apt-get install ruby
CentOS/RHEL:
sudo yum install ruby
Para otros sistemas operativos:
https://www.ruby-lang.org/es/documentation/installation/


Instalar la gema de taskjuggler
gem install taskjuggler


## Instrucciones de uso

### 1. Clonar el repositorio:
https://github.com/cmateos96/TFG_Gantt.git
### O descargar el código fuente y descomprimir:
https://github.com/cmateos96/TFG_Gantt/archive/main.zip

### 2. Añadir las tareas en la hoja de cálculo TFG_Gantt/Program_Files/Plantilla.xlsx de acuerdo con las siguientes reglas:
    2.1 No modificar el orden ni el nombre de las columnas (celdas en negrita)
    2.2 Para cada tarea del proyecto rellenar una fila de la siguiente forma:
        2.2.1 Rellenar el campo ID con una cadena de caracteres que empiece por letra. Será necesario para rellenar los campos subtareas y dependencias. Se generará uno automáticamente   si no lo rellena
        2.2.2 Rellenar la celda nombre (obligatorio)
        2.2.3 Rellenar la celda subtareas con un id** o la concatenación de varios id separados por & (ej. id1&id2&id3)
        2.2.4 Rellenar la celda inicio si tiene una fecha de inicio fija. La fecha debe tener formato AAAA-MM-DD
        2.2.5 Rellenar la celda duración con alguno de los siguientes formatos (no especificar para las tareas con subtareas):
            - #d: Número de días que dura la tarea(ej. "10d" para una tarea que dure 10 días)
            - #w: Número de semanas que dura la tarea(ej. "10w" para una tarea que dure 70 días)
            - #m: Número de días que dura la tarea(ej. "2m" para una tarea que dure 60 días)
            - #y: Número de días que dura la tarea(ej. "1y" para una tarea que dure 365 días)
            - #: Número de días que dura la tarea(ej. "10" para una tarea que dure 10 días)
        2.2.6 Rellenar la celda dependencias con un id** o la concatenación de varios id separados por & (ej. id1&id2&id3)
    
    **Son válidos tanto los id de tareas como los de milestones.

### 3. Añadir los milestones en TFG_Gantt/Program_Files/Plantilla.xlsx de acuerdo con las siguientes reglas:
    3.1 No modificar el orden ni el nombre de las columnas (celdas en negrita)
    3.2 Para cada milestone del proyecto rellenar una fila de la siguiente forma:
        3.2.1 Rellenar la celda ID con una cadena que empiece por letra (obligatorio).
        3.2.2 Rellenar la celda nombre (obligatorio)
        3.2.3 Rellenar la celda uno de los campos restantes (Inicio y Dependencias) siguiendo las normas 2.2.4 y 2.2.6

### 4. Rellenar la celda 1B, a la derecha de "duración", (valor por defecto 365) con la duración estimada para el proyecto siguiendo alguno de los formatos descritos en el apartado 2.2.5

### 5.Exportar como comma-separated value (.csv) en la carpeta TFG_Gantt/Program_Files.

### 6.Renombrar el archivo .csv al del título del proyecto.(Se utilizará a la hora de generar reportes)

### 7.Ejecutar el archivo TFG_Gantt/Code/TFG.sh (cambiar los permisos si fuera necesario). Los archivos resultantes de la ejecución quedarán en el mismo directorio desde el que se ejecutó el script en una carpeta llamada Gantt_Results.
