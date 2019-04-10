# -*- coding: utf-8 -*-
from Nodo import Nodo
import Contar_hojas, Insertar_en_arbol

nodoInicial = Insertar_en_arbol.mainCrearArbol()
cantHojas = Contar_hojas.mainCantHojas(nodoInicial)
print(cantHojas)