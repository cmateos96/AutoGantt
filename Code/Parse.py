import datetime
import csv
import Tarea
import random
import sys
import re
import GestorErrores

def validar_id(id):
    return bool(re.match("[a-zA-Z_][a-zA-Z_0-9]*", id))

def id_existe(id,lista_ids):
    """
    Comprueba si existe un id entre los una lista de id

    Parámetros:
    id(string) - id de la tarea que se quiere comprobar
    lista_ids(list) - lista donde se va a buscar
    """
    return lista_ids.count(id) == 1

def anhadir_id_lista (id,lista_ids):
    """
    Añade un id a una lista

    Parámetros:
    id(string) - id a añadir
    lista_ids(list) - lista de id a la que se añadirá
    """
    if lista_ids.count(id) == 0:
        lista_ids.append(id)
    else:
        GestorErrores.reportar_error(3,id)

def comprobar_espacios(id):
    if " " in id:
        GestorErrores.reportar_error(4,id)

def cast_fecha(fecha_string):
    """
    Convierte un cadena en un objeto datetime

    Parámetros:
    fecha_string(string) - cadena con la fecha a castear 

    Excepciones:
    Si no tiene el formato %YYYY-%mm-%dd o es una fecha imposible termina la ejecución del programa y comunica el error.
    """
    if fecha_string != "":
        try:
            return datetime.datetime.strptime(fecha_string, "%Y-%m-%d")
        except ValueError:
            GestorErrores.reportar_error(5)
    else:
        return None

def cast_subtareas(subtareas_string):
    """
    Convierte una cadena con las subtareas de una tarea en una lista que contiene el número de dichas tareas.

    Devuelve:
    Lista con la las subtareas. Si no tiene subtareas devuelve una lista vacía.

    Parámetros:
    subtareas_string(string) - cadena que contiene las subtareas en formato id1&id2 o id
    Excepciones:
    Si la cadena no tiene alguno de los formatos válidos detiene la ejecución.
    """
    lista_subtareas = []
    if subtareas_string != "":
        if "&" in subtareas_string:
            lista_aux=subtareas_string.split("&")
            for id in lista_aux:
                comprobar_espacios(id)
                lista_subtareas.append(id)
        else:
            lista_subtareas.append(subtareas_string)
    return lista_subtareas

def cast_dependencias(dependencias_string):
    """
    Convierte una cadena con las dependecias de una tarea en una lista que contiene el ID de dichas tareas.

    Devuelve:
    Lista con la las dependencias. Si no tiene dependencias devuelve una lista vacía.

    Parámetros:
    dependencias_string(string) - cadena que contiene las subtareas en formato num1&num2&num3... o num

    Excepciones:
    Si la cadena no tiene alguno de los formatos válidos detiene la ejecución.
    """
    lista_dependencias = []
    if dependencias_string != "":
        if "&" in dependencias_string:
            lista_aux = []
            lista_aux=dependencias_string.split("&")
            for id in lista_aux:
                comprobar_espacios(id)
                lista_dependencias.append(id)
        else:
            lista_dependencias.append(dependencias_string)
    return lista_dependencias

def cast_duracion(duracion_string):
    """
    Convierte una cadena con formato #d,#w,#m o #y en el número de días equivalente.

    Devuelve:
    Número de días equivalente a la cadena indicada.

    Parámetros:
    duracionString(string) - Cadena con formato #d,#w,#m o #y a ser transformada.

    Excepciones:
    Si la cadena no tiene el formato deseado termina la ejecución
    """
    duracion_en_dias = 0
    try:
        if duracion_string != "":
            if "w" == duracion_string[len(duracion_string)-1]:
                numero_semanas = duracion_string.split("w")
                duracion_en_dias = int(numero_semanas[0]) * 7
            elif "m" == duracion_string[len(duracion_string)-1]:
                numero_meses = duracion_string.split("m")
                duracion_en_dias = int(numero_meses[0]) * 30
            elif "y" == duracion_string[len(duracion_string)-1]:
                numero_anhos = duracion_string.split("y")
                duracion_en_dias = int(numero_anhos[0]) * 365
            elif "d" == duracion_string[len(duracion_string)-1]:
                numero_dias = duracion_string.split("d")
                duracion_en_dias = int(numero_dias[0])
            else:
                duracion_en_dias = int(duracion_string)
            return duracion_en_dias
    except ValueError:
        GestorErrores.reportar_error(6)

def comprobar_existencia_subtareas(tarea,lista_ids):
    """
    Comprueba que el id de las subtareas de una tarea existe
    
    Parámetros:
    tarea(tarea) - tarea que se desean comprobar
    lista_ids(list) - lista donde se va a buscar la tarea
    """
    if tarea.subtareas != []:
            for id in tarea.subtareas:
                if not id_existe(id,lista_ids):
                    GestorErrores.reportar_error(7,id)

def comprobar_existencia_dependencias(tarea,lista_ids):
    """
    Comprueba que el id de las dependencias de una tarea existe
    
    Parámetros:
    tarea(tarea) - tarea que se desean comprobar
    lista_ids(list) - lista donde se va a buscar la tarea
    """
    if tarea.dependencias != []:
            for id in tarea.dependencias:
                if not id_existe(id,lista_ids):
                    GestorErrores.reportar_error(7,id)

def comprobar_dependencias_y_subtareas(lista_tareas,lista_ids):
    """
    Comprueba que el id de las dependencias y subtareas existe en el proyecto
    
    Parámetros:
    lista_tareas(list) - lista de las tareas que se desean comprobar
    lista_id(list) - lista de los id válidos
    """
    for tarea in lista_tareas:
        comprobar_existencia_subtareas(tarea,lista_ids)
        comprobar_existencia_dependencias(tarea,lista_ids)

def hay_tarea(row):
    """
    Comprueba si en la fila hay especificada alguna tarea
    
    Parámetros:
    row(row) - fila que se quiere comprobar
    """
    return not row[0]==row[1]==row[2]==row[3]==row[4]==row[5]==""

def hay_milestone(row):
    """
    Comprueba si en la fila hay especificada algún milestone
    
    Parámetros:
    row(row) - fila que se quiere comprobar
    """
    return not row[7]==row[8]==row[9]==row[10] == ""

def crear_tarea(row):
    """
    Crea una tarea a partir de los datos que obtiene de la fila
    
    Parámetros:
    row(row) - fila que contiene los datos a procesar
    """
    #Compruebo que el nombre no es nulo
    nombre = row[1]
    if nombre == "":
        GestorErrores.reportar_error(8)
    #Compruebo que el id no es nulo y si lo es genero uno aleatorio
    id_tarea = row[0]
    if id_tarea == "":
        id_tarea = "rand" + str(random.randint(1, 10000000))
    if not validar_id(id_tarea):
        GestorErrores.reportar_error(9,id_tarea)
    subtareas = cast_subtareas(row[2])
    inicio = cast_fecha(row[3])
    duracion = cast_duracion(row[4])
    dependencias = cast_dependencias(row[5])
    nueva_tarea = Tarea.Tarea(id_tarea,nombre,subtareas, inicio,duracion,dependencias)
    return nueva_tarea

def crear_milestone(row):
    """
    Crea una tarea a partir de los datos que obtiene de la fila
    
    Parámetros:
    row(row) - fila que contiene los datos a procesar
    """
    milestone_id = row[7]
    if milestone_id == "":
        GestorErrores.reportar_error(10)
    milestone_nombre = row[8]
    if milestone_nombre == "":
        GestorErrores.reportar_error(11)
    if row[9]==row[10]=="":
        GestorErrores.reportar_error(12)
    else:
        milestone_inicio = cast_fecha(row[9])
        milestone_dependencias = cast_dependencias(row[10])
        nuevo_milestone = Tarea.Tarea(milestone_id,milestone_nombre,[], milestone_inicio,0,milestone_dependencias)
        return nuevo_milestone

def parsear_tareas_csv(path_csv):
    """
    Convierte cada linea del archivo .csv en objetos tarea con los campos especificados.

    Devuelve:
    lista_tareas: una lista que contiene todos los objetos tarea procesados.

    Prámetros:
    path_csv - Path absoluto del archivo csv exportado de Google Sheets.
    """
    with open(path_csv, 'r') as file:
        lista_tareas = []
        reader = csv.reader(file)
        aux = 0
        lista_ids = []
        for row in reader:
            aux += 1
            #Salto las primeras lineas del CSV, que no contienen datos útiles
            if aux == 1: duracion_proyecto = cast_duracion(row[1])
            if aux < 5: continue
            if hay_tarea(row):
                nueva_tarea = crear_tarea(row)
                lista_tareas.append(nueva_tarea)
                anhadir_id_lista(nueva_tarea.id, lista_ids)           
            if hay_milestone(row):
                nuevo_milestone = crear_milestone(row)
                lista_tareas.append(nuevo_milestone)
                anhadir_id_lista(nuevo_milestone.id, lista_ids)
        comprobar_dependencias_y_subtareas(lista_tareas,lista_ids)
    return duracion_proyecto,lista_tareas