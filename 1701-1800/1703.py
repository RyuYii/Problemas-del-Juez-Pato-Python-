"""origami"""
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        line = line.split()
        n = int(line[0])        #asignamos los amigos
        k = int(line[1])        #cantidad de hojas
        hoj = [8, 5, 2]         #hojas por color
        c = 0                   #cantidad de cuadernos
        for i in hoj:
            a = n*i             #cantidad de hojas que se necesitan
            if(a%k!=0):         #control para saber cuantos cuadernos comprar por color
                c+=(a//k)+1
            else:
                c+=a//k
        print(c)                #cuadernos en total