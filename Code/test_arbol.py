import Arbol

#Hago un arbol manualmente con la siguiente forma para test
# a
# |_h1
# |  |__h11
# |_h2
# |_h3

a = Arbol.Arbol("a")
h1 = Arbol.Arbol(1)
h2 = Arbol.Arbol(2)
h3 = Arbol.Arbol(3)
h11 = Arbol.Arbol(11)

h1.hijos.append(h11)
a.hijos.append(h1)
a.hijos.append(h2)
a.hijos.append(h3)


def test_buscar_subarbol1():
    assert a.buscar_subarbol(1) == h1

def test_buscar_subarbol2():
    assert a.buscar_subarbol("foo") == None

def test_buscar_subarbol3():
    assert a.buscar_subarbol(11)==h11

def test_agregar_elemento1():
    a.agregar_elemento("nuevo","a")
    lista = []
    for elemento in a.hijos:
        lista.append(elemento.elemento)
    assert "nuevo" in lista

def test_obtener_camino1():
    assert a.obtener_camino(2) == ["a",2]

def test_obtener_camino2():
    assert a.obtener_camino(11) == ["a",1,11]

def test_obtener_camino1():
    assert a.obtener_camino("foo") == []

def test_constructor():
    a = Arbol.Arbol("foo")
    assert a.elemento == "foo"
    assert a.hijos == []