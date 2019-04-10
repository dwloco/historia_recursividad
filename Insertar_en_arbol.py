from Nodo import Nodo
import Contar_hojas

def InsertarEnArbol(NodoFijo, NodoAgregar):
    if NodoAgregar is not None and NodoFijo is not None:
            if NodoAgregar.val < NodoFijo.val: #Si es menor va a la izquierda
                if NodoFijo.izq is None:
                    NodoFijo.izq = NodoAgregar
                else:
                    InsertarEnArbol(NodoFijo=NodoFijo.izq, NodoAgregar=NodoAgregar)
            else:  # Si es mayor o igual va a la derecha
                if NodoFijo.der is None:
                    NodoFijo.der = NodoAgregar
                else:
                    InsertarEnArbol(NodoFijo=NodoFijo.der, NodoAgregar=NodoAgregar)
                    

            
def CrearArbolPrueba():
    """
                                    5
                    2                            10
            1               3              7             28
        0                                                   50 
                                                                100
    """
    nodoInicial = Nodo(val=5)
    InsertarEnArbol(NodoFijo=nodoInicial, NodoAgregar=Nodo(val=2))
    InsertarEnArbol(NodoFijo=nodoInicial, NodoAgregar=Nodo(val=1))
    InsertarEnArbol(NodoFijo=nodoInicial, NodoAgregar=Nodo(val=0))
    InsertarEnArbol(NodoFijo=nodoInicial, NodoAgregar=Nodo(val=3))
    InsertarEnArbol(NodoFijo=nodoInicial, NodoAgregar=Nodo(val=10))
    InsertarEnArbol(NodoFijo=nodoInicial, NodoAgregar=Nodo(val=7))
    InsertarEnArbol(NodoFijo=nodoInicial, NodoAgregar=Nodo(val=28))
    InsertarEnArbol(NodoFijo=nodoInicial, NodoAgregar=Nodo(val=50))
    InsertarEnArbol(NodoFijo=nodoInicial, NodoAgregar=Nodo(val=100))
    return nodoInicial

def mainCrearArbol():
    nodo = CrearArbolPrueba()
    return nodo
