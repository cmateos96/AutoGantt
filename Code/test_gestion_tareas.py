import Tarea, Arbol, GestionTareas, datetime

a = Tarea.Tarea("id_a","nombre_a",["id_b","id_c"],datetime.datetime(2020,12,31),"30",[])
b = Tarea.Tarea("id_b","nombre_b",[],datetime.datetime(2021,1,1),"40",[])
c = Tarea.Tarea("id_c","nombre_c",[],datetime.datetime(2020,12,1),"50",[])
lista_tareas = [a,b,c]

def test_obtener_fecha_inicio():
    assert GestionTareas.obtener_fecha_inicio(lista_tareas) == datetime.datetime(2020,12,1)

def test_obtener_tarea_desde_id():
    assert GestionTareas.obtener_tarea_desde_id(lista_tareas,"id_a") == a
    assert GestionTareas.obtener_tarea_desde_id(lista_tareas, "foo") == None

def test_path_obtener_path_absoluto_tarea():
    assert GestionTareas.obtener_path_absoluto_tarea(lista_tareas) == "id_b.id_c"

def test_obtener_arbol_tareas_y_agregar_subtareas():
    #Estructura del arbol que debería generar
    # raiz
    # |_a
    #    |_b
    #    |_c
    arbol_dummie = GestionTareas.obtener_arbol_tareas(lista_tareas)
    assert arbol_dummie.elemento.id == "Raiz"
    assert arbol_dummie.hijos[0].elemento == a
    assert arbol_dummie.hijos[0].elemento.id == "id_a"
    assert arbol_dummie.hijos[0].hijos[0].elemento == b
    assert arbol_dummie.hijos[0].hijos[0].elemento.id == "id_b"
    assert arbol_dummie.hijos[0].hijos[1].elemento == c
    assert arbol_dummie.hijos[0].hijos[1].elemento.id == "id_c"


