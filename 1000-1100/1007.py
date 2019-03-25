#Pipo el Payaso


def obtCantPref(n):     #recibimos como parametro la lista con las palabras de la frase
    pre = []
    for i in n:
        pre.append(i[0])#extraemos los primeros caracteres y lo ponemos en una nueva lista
    letra = []
    mayor = 0
    for i in pre:       #recorremos la nueva lista
        if i in letra:  #conrol para no repetir procesos
            continue
        letra.append(i) #guardamos las letras que ya visitamos
        nu = pre.count(i)
        if nu > mayor:  #buscamos el mayor
            mayor = nu
    return mayor        #lo retornamos


casos = int(input())
for i in range(casos):
    jug = []
    num = int(input())
    cant = []
    mayor = 0
    for j in range(num):            #para cada frase
        frase = input().split()
        nu = obtCantPref(frase)     #obtenemos la cantidad de palabras que empiezan igual
        if nu > mayor:              #para saber cual es mayor
            mayor = nu
        cant.append(nu)             # guardamos en una lista el resultado de cada jugador
    print("El ganador es "+str(cant.index(mayor)+1)) #buscamos en la lista
