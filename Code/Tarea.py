import Arbol
class Tarea:
    def __init__(self, id, nombre, subtareas, inicio, duracion, dependencias):
        """
        Constructor tarea

        Prámetros:
        id(string) - id que recibe la tarea
        nombre(string) - nombre que recibe la tarea
        subtareas (list) - lista de los id de sus subtareas
        inicio(datetime) - fecha de inicio la tarea 
        duracion(int) - numero de días que se estima que dure el proyecto
        dependencias(list) - lista de los id de las tareas de las que depende
        """
        self.id = id
        self.nombre = nombre
        self.subtareas = subtareas
        self.inicio = inicio
        self.duracion = duracion
        self.dependencias = dependencias

    def __str__(self):
        """
        Representa el objeto mediante un string
        """
        return "id: " + self.id + "|nombre:" + self.nombre + "|subtareas: " + ', '.join(self.subtareas) + "|dependencias: " + ", ".join(self.dependencias) + "|duracion: " + str(self.duracion) + "|inicio: " + str(self.inicio)

    def __eq__(self, otro):
        """
        Compara el objeto con otro y devuelve true si los id son iguales, false en cualquier otro caso
        
        Prámetros:
        otro(Tarea) - tarea con la que se va a comparar
        """
        if type(otro)==Tarea:
            return otro.id == self.id
        else:
            return False

    def tipos_tarea(self):
        """
        Representación de los tipos de la tarea mediante un string
        """
        return "id: " + str(type(self.id)) + "|nombre:" + str(type(self.nombre)) + "|subtareas: " + str(type(self.subtareas)) + "|dependencias:" + str(type(self.dependencias)) + "|duracion: " + str(type(self.duracion)) + "|inicio: " + str(type(self.inicio))
    