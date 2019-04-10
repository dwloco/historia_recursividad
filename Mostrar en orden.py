from Nodo import Nodo

def MostrarEnOrden (Nodo):
    if (Nodo is not None):
        MostrarEnOrden(Nodo.izq)
        print(Nodo.val)
        MostrarEnOrden(Nodo.der)
