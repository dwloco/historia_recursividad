from Nodo import Nodo

def TwoChilds(nodo, nodoReemplazo):
    if nodo.izq is not None:
        nodoHijoReemplazo = TwoChilds(nodo.izq)
        if nodoHijoReemplazo is not None:
            nodo.der = nodoHijoReemplazo
        return None
    else:
        nodoReemplazo[0] = nodo
        if nodo.der is not None:
            return nodo.der
        

def Eliminar(nodoFijo, valBorrar):
    if nodoFijo.val == valBorrar:
        if nodoFijo.izq is None and nodoFijo.der is None:
            nodoFijo = None
        elif nodoFijo.izq is not None and nodoFijo.der is not None:  # Tiene hijos en los dos lados
            nodoReemplazo = []  # Al pasar una lista, simulo un parametro por referencia
            TwoChilds(nodo= nodoFijo.der, nodoReemplazo= nodoReemplazo)
            nodoFijo = nodoReemplazo[0]
        elif nodoFijo.izq is not None: # Tiene un hijo a la izquierda
            nodoFijo = nodoFijo.izq
        else:  # Tiene un hijo a la derecha
            nodoFijo = nodoFijo.der
    elif valBorrar < nodoFijo.val:
        Eliminar(nodoFijo = nodoFijo.izq, valBorrar = valBorrar)
    else:
        Eliminar(nodoFijo = nodoFijo.der, valBorrar = valBorrar)