"""REduciendo Costos"""

n = int(input())    #leemos la catidad de casos

for j in range(0, n):
    #como los numeros vienen en una linea procedemos con lo siguiente
    m = input()
    v = m.split()
    c = []
    for i in v:
        c.append(int(i))
    #como resultado los datos estaran almacenados en un vector de enteros
    c.sort()    #ordenamos el vector
    print('Case {0}: {1}'.format(j+1,c[1])) #finalmente imprimimos