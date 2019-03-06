"""Problema Cadena Bailarina"""

T = int(input())                #cantidad de casos
for i in range(0,T):
    cad = input()               #leemos la cadena
    bailarina = ""
    sw = True
    for i in cad:
        c = str(i)
        if(c!=" "):             #omitimos los espacios
            if(sw):
                c = c.upper()   #volvemos a mayuscula
                sw = False
            else:
                c = c.lower()   #volvemos a minuscula
                sw = True
        bailarina+=c            #mostramos la cadena bailarina
    print(bailarina)



