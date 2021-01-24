class Proyecto:
    def __init__(self, nombre, inicio=None, duracion_estimada=None, tareas=None):
        """
        Constructor proyecto
        
        Prámetros:
        nombre(string) - nombre que recibe el proyecto
        inicio(datetime) - fecha de inicio del proyecto 
        duracion_estimada(int) - numero de días que se estima que dure el proyecto
        tareas(list) - lista de tareas que contiene el proyecto
        """
        #El nombre del archivo .csv
        self.nombre = nombre
        #Viene marcada por la fecha más temprana de las tareas
        self.inicio = inicio
        self.duracion_estimada = duracion_estimada
        self.tareas = tareas
        