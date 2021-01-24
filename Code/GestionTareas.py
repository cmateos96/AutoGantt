import Tarea
import Arbol

def obtener_fecha_inicio(lista_tareas):
    """
    Dada una lista de tareas devuelve la primera fecha cronológicamente.

    Prámetros:
    lista_tareas(list) - lista que contiene objetos de tipo tarea
    """
    minimo = None
    for tarea in lista_tareas:
        if tarea.inicio != None and (minimo == None or tarea.inicio < minimo) :
            minimo = tarea.inicio
    return minimo

def obtener_tarea_desde_id(lista_tareas,id_tarea):
    """
    Obtiene una tarea con un determinado ID que se encuentre dentro de una lista de tareas.

    Prámetros:
    id_tarea(string) - string buscado como id en la lista
    lista_tareas(list) - lista que contiene objetos de tipo tarea
    """
    for tarea in lista_tareas:
        if tarea.id == id_tarea: return tarea
    return None

def agregar_subtareas(arbol,tarea_padre,lista_tareas):
    """
    Agrega en un arbol las subtareas como hijos de una tarea padre
    Prámetros:
    arbol(arbol) - arbol donde se desean agregar la subtareas
    tarea_padre(tarea) - elemento que será el padre de cada una de las subtareas
    lista_tareas(list) - lista donde viene almacenadas los id de las subtareas a agregar
    """
    if tarea_padre.subtareas != []:
        for subtarea_string in tarea_padre.subtareas:
            subtarea = obtener_tarea_desde_id(lista_tareas,subtarea_string)
            if subtarea != None:
                del(lista_tareas[lista_tareas.index(subtarea)])
                arbol.agregar_elemento(subtarea , tarea_padre)
                agregar_subtareas(arbol,subtarea,lista_tareas)

def obtener_arbol_tareas(lista_tareas):
    """
    Obtener un arbol a partir de una lista de Tareas (que contendrán subtareas)
    Prámetros:
    lista_tareas(list) - lista donde viene almacenadas las tareas del arbol
    """
    raiz = Tarea.Tarea("Raiz","",[],None,0,[])
    arbol = Arbol.Arbol((raiz))
    for tarea in lista_tareas:
        arbol.agregar_elemento(tarea , raiz)
        agregar_subtareas(arbol,tarea,lista_tareas)
    return arbol

def representar_arbol(arbol):
    """
    Representación textual del arbol

    Parametros:
    arbol(arbol) - arbol a representar
    """
    print (arbol.elemento)
    if arbol.hijos != []:
        tarea_string = str(arbol.elemento)
        print("Hijos de: " + tarea_string.split("|nombre:")[0])
        for hijo in arbol.hijos:
            representar_arbol (hijo)
        print("--------------------------------")

def obtener_path_absoluto_tarea(camino):
    """
    Obtiene un string del id de las tareas que hay en un camino.
    
    Prámetros:
    Camino(list) - lista de objetos Tarea
    """   
    path = ""
    aux = 0
    for nodo in camino:
        aux += 1
        if aux > 2:
            path = path + "." + nodo.id
        else:
            path = nodo.id
    return path
