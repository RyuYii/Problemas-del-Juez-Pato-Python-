"""Problema: Mediana
corregido
"""
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        n = int(line)    #leemos la catidad de numeros

#como los n numeros vienen en una linea procedemos con lo siguiente
        m = input()
        v = m.split()
        c = []
        for i in v:
            c.append(int(i))
#como resultado los datos estaran almacenados en un vector de enteros
        c.sort()    #ordenamos el vector

#verificamos lo que se nos pide
        if(n%2!=0):
            pos = n//2
            print(c[pos])
        else:
            print(-1)
