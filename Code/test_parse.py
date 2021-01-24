import Parse
import Tarea
import pytest
import datetime
import csv

def test_validar_id():
    assert Parse.validar_id("*foo") == False
    assert Parse.validar_id("Foo") == True
    assert Parse.validar_id("foo") == True
    assert Parse.validar_id("_foo") == True
    

def test_id_existe():
    lista_test = ["id_1","id_1","id_2","id_3"]
    assert Parse.id_existe("id_1",lista_test) == False
    assert Parse.id_existe("foo", lista_test) == False
    assert Parse.id_existe("id_2",lista_test) == True

def test_anhadir_id_lista():
    lista_test = ["id_1","id_1","id_2","id_3"]
    with pytest.raises(SystemExit) as pytest_error:
            Parse.anhadir_id_lista("id_1",lista_test)
    assert pytest_error.type == SystemExit
    Parse.anhadir_id_lista("id_4",lista_test)
    assert lista_test[len(lista_test)-1] == "id_4"

def test_cast_fecha():
    fecha_test = datetime.datetime(2020,12,31)
    assert fecha_test == Parse.cast_fecha("2020-12-31")
    with pytest.raises(SystemExit) as pytest_error:
            Parse.cast_fecha("foo")
    assert pytest_error.type == SystemExit

def test_cast_subtareas():
    assert Parse.cast_subtareas("id") == ["id"]
    assert Parse.cast_subtareas("id_1&id_2&id_3") == ["id_1","id_2","id_3"]

def  test_cast_dependencias():
    assert Parse.cast_dependencias("id") == ["id"]
    assert Parse.cast_dependencias("id_1&id_2&id_3") == ["id_1","id_2","id_3"]

def test_cast_duracion():
    assert Parse.cast_duracion("20") == 20
    assert Parse.cast_duracion("20d") == 20
    assert Parse.cast_duracion("20w") == 140
    assert Parse.cast_duracion("20m") == 600
    assert Parse.cast_duracion("2y") == 730
    with pytest.raises(SystemExit) as pytest_error:
            Parse.cast_duracion("fooy")
    assert pytest_error.type == SystemExit
    with pytest.raises(SystemExit) as pytest_error:
            Parse.cast_duracion("y123")
    assert pytest_error.type == SystemExit

def test_comprobar_existencia_subtareas():
    lista_id =["foo", "id_1", "prueba"]
    tareaBien = Tarea.Tarea("root","raiz",["foo","id_1"],datetime.datetime(2021,1,1),30,[])
    tareaMal = Tarea.Tarea("root","raiz",["error","nop"],datetime.datetime(2021,1,1),30,[])
    try:
        Parse.comprobar_existencia_subtareas(tareaBien,lista_id)
    except SystemExit:
        pytest.fail()
    with pytest.raises(SystemExit) as pytest_error:
            Parse.comprobar_existencia_subtareas(tareaMal, lista_id)
    assert pytest_error.type == SystemExit

def test_comprobar_existencia_dependencias():
    lista_id =["foo", "id_1", "prueba"]
    tareaBien = Tarea.Tarea("root","raiz",["foo","id_1"],datetime.datetime(2021,1,1),30,["foo","id_1"])
    tareaMal = Tarea.Tarea("root","raiz",["error","nop"],datetime.datetime(2021,1,1),30,["error","nop"])
    try:
        Parse.comprobar_existencia_dependencias(tareaBien,lista_id)
    except SystemExit:
        pytest.fail()
    with pytest.raises(SystemExit) as pytest_error:
            Parse.comprobar_existencia_dependencias(tareaMal, lista_id)
    assert pytest_error.type == SystemExit

def test_hay_y_crear_tarea():
    row = ["","","","","","","","","",""]
    assert Parse.hay_tarea(row) == False
    row[0] = "id_1"
    assert Parse.hay_tarea(row) == True
    row = ["id_1","nombre","","2021-1-1","20","","","","",""]
    tarea_test = Tarea.Tarea("id_1","nombre",[],datetime.datetime(2021,1,1),20,[])
    assert Parse.crear_tarea(row) == tarea_test
    row[0]=""
    assert "rand" in Parse.crear_tarea(row).id
    row[1]=""
    with pytest.raises(SystemExit) as pytest_error:
            Parse.crear_tarea(row)
    assert pytest_error.type == SystemExit

def test_hay_y_crear_dependencia():
    row = ["","","","","","","","","","",""]
    assert Parse.hay_milestone(row) == False
    row[7] = "id_1"
    assert Parse.hay_milestone(row) == True
    row = ["","","","","","","","id_1","nombre","2021-1-1",""]
    tarea_test = Tarea.Tarea("id_1","nombre",[],datetime.datetime(2021,1,1),0,[])
    assert Parse.crear_milestone(row) == tarea_test
    row[7]=""
    with pytest.raises(SystemExit) as pytest_error:
            Parse.crear_milestone(row)
    assert pytest_error.type == SystemExit
    row[7]="id_1"
    row[8]=""
    with pytest.raises(SystemExit) as pytest_error:
            Parse.crear_milestone(row)
    assert pytest_error.type == SystemExit
    row[8]="nombre"
    row[9]=""
    with pytest.raises(SystemExit) as pytest_error:
            Parse.crear_milestone(row)
    assert pytest_error.type == SystemExit



