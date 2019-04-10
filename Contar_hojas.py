# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:08:05 2019

@author: ezequiel
"""
cantHojas = 0
def contarHojas(NodoInicial, NodoActual):
    if NodoActual is not None:
        global cantHojas
        """
        Si tiene izquierda, lo mando
        Si tiene derecha, lo mando
        Si no tiene ni izquierda ni derecha, sumo uno
        """
        if NodoActual.izq is not None:
            contarHojas(NodoInicial = NodoInicial, NodoActual = NodoActual.izq)
        
        if NodoActual.der is not None:
            contarHojas(NodoInicial = NodoInicial, NodoActual = NodoActual.der)
        
        if NodoActual.izq is None and NodoActual.der is None:
            cantHojas = cantHojas + 1

def obtenerCantHojas(NodoInicial, NodoActual):
    contarHojas(NodoInicial, NodoActual)
    return cantHojas
