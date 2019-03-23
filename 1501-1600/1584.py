# Botas y los Museos
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        i = input().split()
        X = []
        for x in i:
            X.append(int(x))
        """Hemos leido los datos que que nos da, que sigue?
            Como cada museo es un punto del eje x
            entonces ordenamos los datos de menor a mayor
            de esta forma al restar el ultimo con el 
            primero tendremos la respuestta correcta"""
        X.sort()
        print(X[-1] - X[0])
