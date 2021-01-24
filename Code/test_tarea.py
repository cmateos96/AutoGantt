import Tarea

def test_constructor():
    a = Tarea.Tarea("id_a","tarea_a",["foo1"],"31-12-2020","2m",["foo2"])
    assert a.id == "id_a"
    assert a.nombre == "tarea_a"
    assert a.subtareas == ["foo1"]
    assert a.inicio == "31-12-2020"
    assert a.duracion == "2m"
    assert a.dependencias == ["foo2"]

def test_eq1():
    a = Tarea.Tarea("id_a","tarea_a",["foo1"],"31-12-2020","2m",["foo2"])
    b = Tarea.Tarea("id_a","tarea_b",["foo123"],"30-12-2020","3m",["foo456"])
    c = Tarea.Tarea("id_foo","tarea_a",["foo1"],"31-12-2020","2m",["foo2"])
    assert a == b
    assert a != c
