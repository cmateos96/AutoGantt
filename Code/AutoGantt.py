import os
import sys
import Proyecto
import GestionTareas
import Parse
import datetime
import Tarea
import GestorErrores

MAIN="AutoGantt.py"
PROGRAM_FILES_RELATIVA="../Program_Files/"

def obtener_path_absoluto_codigo():
    """
    Obtiene el path absoluto de la carpeta que contiene el script
    """    
    return os.path.abspath(sys.argv[0])

def ls(ruta = os.getcwd()):
    """
    Lista todos los archivos del directorio que se reciba como parámetro

    Devuelve:
    Lista con los nombres de los archivos

    Prámetros:
    ruta(string) - path del directorio del cual se quieren obtener los nombres de sus archivos
    """    
    return [arch.name for arch in os.scandir(ruta) if arch.is_file()]

def comprobar_existencia_planitlla_y__devolver_path_absoluto():
    """
    Comprueba que exista un archivo con extensión .cvs en el directorio de Program_files del programa
    y devuelve el path absoluto de dicho archivo 
    
    Devuelve:
    path absoluto del archivo .csv

    Excepciones:
    termina la ejecución del programa si no encuentra un archivo .csv
    """
    code_folder = obtener_path_absoluto_codigo().split(MAIN)[0]
    lista_documentos = ls(code_folder + PROGRAM_FILES_RELATIVA)
    encontrado = False
    counter = 0
    for archivo in lista_documentos:
        if os.path.splitext(archivo)[1] == ".csv":
            counter += 1
            encontrado = True
            path = code_folder + PROGRAM_FILES_RELATIVA + archivo
    if not encontrado:
        GestorErrores.reportar_error(1)
    if counter > 1:
        GestorErrores.reportar_error(2)
    return path

def escribir_projetc(proyecto):
    """
    Escribe en el documento de definición de TaskJuggler el elemento project y sus campos

    Prámetros:
    proyecto(Proyecto) - objeto de tipo proyecto que contiene toda la información necesaria para definir el elemento proyecto de TaskJuggler
    """
    code_folder = obtener_path_absoluto_codigo().split(MAIN)[0]
    f = open( code_folder + PROGRAM_FILES_RELATIVA + proyecto.nombre + ".tjp","w")
    f.write("#PROYECTO\n")
    f.write("project \"" + proyecto.nombre + "\" "
             + str(proyecto.inicio.date()) + " +"
             + str(proyecto.duracion_estimada) + "d "
            "{\n timezone \" Europe/Madrid\" \n timeformat \"%Y-%m-%d\"\n}\n\n")
    f.close()

def tabular(f,tabuladores):
    """
    Escribe en el fichero f tantos tabuladores como indique la variable tabuladores

    Parámetros:
    f(file) - fichero donde se van a escribir los tabuladores
    tabuladores(int) - cantidad de tabuladores que se van a insertar en el fichero
    """    
    for i in range(tabuladores):
        f.write("\t")

def escribir_duracion_tarea(file,tabuladores,tarea):
    """
    Escribe en el fichero file la duracion de la tarea, precedida de tantos tabuladores como indique tabuladores

    Parámetros:
    f(file) - fichero donde se van a escribir los tabuladores
    tabuladores(int) - cantidad de tabuladores que se van a insertar en el fichero
    tarea(tarea) - tarea procesada
    """  
    tabular(file,tabuladores)
    file.write("duration " + str(tarea.duracion) + "d\n" )

def escribir_inicio_tarea(file,tabuladores,tarea):
    """
    Escribe en el fichero file el inicio de la tarea, precedida de tantos tabuladores como indique tabuladores

    Parámetros:
    f(file) - fichero donde se van a escribir los tabuladores
    tabuladores(int) - cantidad de tabuladores que se van a insertar en el fichero
    tarea(tarea) - tarea procesada
    """  
    tabular(file,tabuladores)
    file.write("start " + datetime.datetime.strftime(tarea.inicio, "%Y-%m-%d\n") )

def escribir_subtareas_tarea(file,tabuladores,nodo,arbol):
    """
    Escribe en el fichero file las subtareas de la tarea contenida en nodo, precedida de tantos tabuladores como indique tabuladores

    Parámetros:
    f(file) - fichero donde se van a escribir los tabuladores
    tabuladores(int) - cantidad de tabuladores que se van a insertar en el fichero
    nodo(arbol) - tarea procesada cuyos hijos son sus subtareas
    arbol(arbol) - árbol al que pertenece nodo
    """ 
    for subtarea in nodo.hijos:
        tabuladores += 1
        escribe_tarea(arbol,subtarea,file,tabuladores)
        tabuladores -= 1

def escribir_dependencias_tarea(file,tabuladores,tarea,arbol):
    """
    Escribe en el fichero file las dependencias de tarea, precedida de tantos tabuladores como indique tabuladores

    Parámetros:
    f(file) - fichero donde se van a escribir los tabuladores
    tabuladores(int) - cantidad de tabuladores que se van a insertar en el fichero
    tarea(tarea) - tarea procesada
    arbol(arbol) - árbol al que pertenece la tarea
    """ 
    tabular(file,tabuladores)
    file.write("depends " )
    auxiliar = len(tarea.dependencias)
    for dependencia in tarea.dependencias:
        aux = Tarea.Tarea(dependencia,"",[] ,None ,None ,[])
        camino_de_nodos = arbol.obtener_camino(aux)
        path_absoluto_tarea =  GestionTareas.obtener_path_absoluto_tarea(camino_de_nodos)
        file.write( path_absoluto_tarea)
        auxiliar -= 1
        if auxiliar > 0:
            file.write(", ") 
    file.write("\n")

def escribe_tarea(arbol,nodo,file,tabuladores):
    """
    Escribe en file el contenido de la tarea que haya en el nodo del arbol.
    Prámetros:
    arbol(arbol) - arbol cuyo contenido son objetos tarea
    nodo(arbol) - nodo que contiene la tarea a escribir
    file(file) - descriptor de fichero abierto donde se va a escribir
    tabuladores(int) - variable interna que indica el número de tabuladores que hay que escribir antes de cada línea para que quede estético
    """   
    tabular(file,tabuladores)
    tarea = nodo.elemento
    file.write("task " + tarea.id + " \"" + tarea.nombre + "\" {\n" )
    if tarea.duracion != None:
        escribir_duracion_tarea(file,tabuladores,tarea)
    if tarea.inicio != None:
        escribir_inicio_tarea(file,tabuladores,tarea)
    if tarea.dependencias != []:
        escribir_dependencias_tarea(file,tabuladores,tarea,arbol)
    if tarea.subtareas != []:
        escribir_subtareas_tarea(file,tabuladores,nodo,arbol)

    tabular(file,tabuladores)
    file.write("}\n\n")
    tabuladores = tabuladores - 1

def definir_tareas(proyecto):
    """
    Escribe en el documento de definición de TaskJuggler los elementos task y sus campos elemento.
    Prámetros:
    proyecto(proyecto) - objeto de tipo proyecto que contiene toda la información necesaria para definir las tareas de TaskJuggler
    """
    code_folder = obtener_path_absoluto_codigo().split(MAIN)[0]
    f = open( code_folder + PROGRAM_FILES_RELATIVA + proyecto.nombre + ".tjp","a")
    f.write("#TAREAS\n")
    tabuladores = 0
    for nodo in proyecto.tareas.hijos:
        escribe_tarea(proyecto.tareas,nodo,f,tabuladores)
    f.close()

def gererar_reportes(proyecto):
    """
    Escribe en el documento de definición de TaskJuggler los comandos necesarios para que TaskJuggler genere reportes.

    Parámetros:
    proyecto(proyecto) - objeto que tiene toda la información que decine el proyecto
    """   
    code_folder = obtener_path_absoluto_codigo().split(MAIN)[0]
    f = open( code_folder + PROGRAM_FILES_RELATIVA + proyecto.nombre + ".tjp","a")
    f.write("#REPORTES\n")
    f.write(
    """
    macro TaskTip [
    tooltip istask() -8<-
    ->8-
    ]

    textreport frame "" {
    header -8<-
        == """ + proyecto.nombre + """ ==
    ->8-
    footer "----"
    textreport index "Diagrama de Gantt """ + proyecto.nombre + """"  {
        formats html
        center '<[report id="overview"]>'
    }
    }

    taskreport overview "" {
    columns bsi { title 'ID' },
    name, start, end, chart { ${TaskTip} }
    timeformat "%a %Y-%m-%d"
    loadunit days
    hideresource @all
    }
    """
    )
    f.close()

def crear_tjp(proyecto):
    """
    Crea el archivo .tjp para después ser procesado por la herramienta TaskJuggler

    Prámetros:
    proyecto(proyecto) - objeto de tipo proyecto que contiene toda la información necesaria para definir las tareas de TaskJuggler
    """
    escribir_projetc(proyecto)
    definir_tareas(proyecto)
    gererar_reportes(proyecto)

def main():
    """
    Método principal.
    """
    path_csv = comprobar_existencia_planitlla_y__devolver_path_absoluto()
    print("Abriendo el archivo para procesar...")
    nombre_proyecto = path_csv.split(PROGRAM_FILES_RELATIVA)[1].split(".csv")[0]
    duracion_proyecto,lista_tareas = Parse.parsear_tareas_csv(path_csv)
    inicio_proyecto = GestionTareas.obtener_fecha_inicio(lista_tareas)
    arbol_tareas = GestionTareas.obtener_arbol_tareas(lista_tareas)
    proyecto = Proyecto.Proyecto(nombre_proyecto, inicio_proyecto, duracion_proyecto, arbol_tareas)
    print("...")
    print("Archivo procesado") 
    print("Creación  del archivo" + proyecto.nombre + ".tjp" + " de definicion de proyecto para TaskJuggler ")
    crear_tjp(proyecto)
    print("...")
    print("Archivo creado correctamente\n\n\n")

main()
exit(0)




