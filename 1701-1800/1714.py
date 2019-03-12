"""Juego de cartas"""

import sys

if __name__ == "__main__":
    for line in sys.stdin:
        lista = input()                 #leemos todo en una cadena
        lista = lista.split()           #lo convertimos en una lista
        lista2 = []
        for i in lista:
            lista2.append(int(i))       #convertimos cada elemento de la lista en un entero
        turno = 0
        lista2.sort()                   #ordenamos la lista
        for i in range(0, len(lista2)): #recorremos la nueva lista
            elemento = lista2[i]
            if elemento == 0:           #el cero representa que ya eliminamos un elemento (carta)
                continue
            else:                          #por condiciones del problema
                x = lista2.index(elemento)
                if x+1 < len(lista2):
                    if elemento+1 == lista2[x+1]:
                        lista2[x+1] = 0
                if elemento-1 == lista2[x-1]:
                    lista2[x+1] = 0
                lista2[x] = 0
                turno += 1
        print(turno)
