
class Arbol:
    def __init__(self, elemento):
        """
        Constructor arbol

        Prámetros:
        elemento - dato que contendrá el nodo
        """
        self.hijos = []
        self.elemento = elemento

    def buscar_subarbol(self, elemento_a_buscar):
        """
        Busca un elemento en un arbol

        Devuelve:
        El elemento y el subarbol que cuelga del elemento buscado si lo encuentra, si no devuelve None

        Prámetros:
        self - arbol donde buscará el elemento
        elemento - elemento buscado
        """
        if self.elemento == elemento_a_buscar:
            return self
        for subarbol in self.hijos:
            arbol_buscado = subarbol.buscar_subarbol(elemento_a_buscar)
            if (arbol_buscado != None):
                return arbol_buscado
        return None

    def agregar_elemento(self, elemento, elemento_padre):
        """
        Agrega un elemento a un arbol

        Prámetros:
        self - arbol donde se agregará el elemento
        elemento - elemento a agregar
        elemento_padre - punto del arbol donde se insertará el elemento
        """
        subarbol = self.buscar_subarbol(elemento_padre)
        subarbol.hijos.append(Arbol(elemento))
    
    def obtener_camino(self,elemento):
        """
        Obtiene el camino de nodos desde la raiz de un arbol hasta el elemento buscado

        Prámetros:
        self - arbol en el que se va a buscar el elemento
        elemento - elemento buscado en el arbol
        """
        lista_nodos = []
        if self.elemento == elemento:
            lista_nodos.append(self.elemento)
            return lista_nodos
        else:
            for subarbol in self.hijos:
                lista_nodos_subarbol = subarbol.obtener_camino(elemento)
                if lista_nodos_subarbol != []:
                    lista_nodos.append(self.elemento)
                    for nodo in lista_nodos_subarbol:
                        lista_nodos.append(nodo)
                    return lista_nodos
        return lista_nodos