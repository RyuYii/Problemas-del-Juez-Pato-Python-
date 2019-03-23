# numeros Balanceados
import sys

if __name__ == '__main__':
    for line in sys.stdin:
        n = int(line)
        """Con esto fragmento lo que hacemos es leer las dos lineas
        con las rectas como son cadenas tenemos que convertirlas
        a enteros para luego ordenarlas"""
        i = input().split()
        j = input().split()
        X, Y = [], []
        for x in i:
            X.append(int(x))
        for y in j:
            Y.append(int(y))

        X.sort()
        Y.sort()
        """ una vez ordenados lo que procede es que contamos las rectas en este intervalo: ]0 , n[
        una vez que obtengamos la cantidad tanto en x como en y
        imcrementamos cada cantidad en 1 para asi obtener el resultado """
        rx = 0
        for i in X:
            if i > 0:
                if i >= n:
                    break
                else:
                    rx += 1
        ry = 0
        for i in Y:
            if i > 0:
                if i >= n:
                    break
                else:
                    ry += 1
        #son muchos for para esto
        #y todo por que la entrada no esta hecha para python :v
        print((rx + 1) * (ry + 1))
