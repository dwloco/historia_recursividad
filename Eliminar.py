from Nodo import Nodo

"""
Funcion de busqueda y extraccion del nodo de reemplazo
en el caso de que haya 2 hijos
"""
def TwoChilds(nodo, nodoReemplazo):
    if nodo.izq is not None:
        nodoHijoReemplazo = TwoChilds(nodo.izq)
        if nodoHijoReemplazo is not None:
            nodo.der = nodoHijoReemplazo
        return None
    else:
		# Me habia olvidado de borrar el nodo antes de pasarlo
        nodoReemplazo[0] = Nodo(val=nodo.val) # Creo un nodo nuevo con el nodo que estoy por borrar
		nder = nodo.der # Guardo el nodo derecho para poder borrar el nodo actual
		nodo = None # Borro el nodo
        if nder is not None:
            return nodo.der
        
"""
Funcion de busqueda del nodo a eliminar
"""
def Eliminar(nodoFijo, valBorrar):
    if nodoFijo.val == valBorrar: # Si el nodo actual tiene el valor que busco significa que lo encontre
        if nodoFijo.izq is None and nodoFijo.der is None: # No tiene hijos
            nodoFijo = None
        elif nodoFijo.izq is not None and nodoFijo.der is not None:  # Tiene hijos en los dos lados
            # Al pasar una lista, simulo un parametro por referencia (python no tiene parametros por referencia)
			nodoReemplazo = []  
            
			TwoChilds(nodo= nodoFijo.der, nodoReemplazo= nodoReemplazo)
			
			# Asigno al nuevo nodo los hijos del viejo, y hago el reemplazo
			nodoReemplazo[0].izq = nodoFijo.izq
			nodoReemplazo[0].der = nodoFijo.der
            nodoFijo = nodoReemplazo[0]
        elif nodoFijo.izq is not None: # Tiene un hijo a la izquierda
            nodoFijo = nodoFijo.izq
        else:  # Tiene un hijo a la derecha
            nodoFijo = nodoFijo.der
    elif valBorrar < nodoFijo.val:
        Eliminar(nodoFijo = nodoFijo.izq, valBorrar = valBorrar)
    else:
        Eliminar(nodoFijo = nodoFijo.der, valBorrar = valBorrar)