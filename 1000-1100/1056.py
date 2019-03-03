"""al reves"""

n = int(input())

for i in range(0, n):
    a = input()     #lo pide el juez aunque no lo uso
    a = input()     #aqui leo la linea
    a = a.split()   #lo convierto a vector
    a.reverse()     #invierto el vector
    cad = ""
    for j in a:
        cad+=j+" "  #guardo en una cadena
    print(cad)      #imprimo