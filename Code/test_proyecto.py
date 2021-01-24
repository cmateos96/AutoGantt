import Proyecto

def test_proyecto():
    a = Proyecto.Proyecto("Nombre_a", "31-12-2020","20w",[])
    assert a.nombre == "Nombre_a"
    assert a.inicio == "31-12-2020"
    assert a.duracion_estimada == "20w"
    assert a.tareas == []