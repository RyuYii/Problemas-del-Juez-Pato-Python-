# mercado
import sys

if __name__ == "__main__":
    for lin in sys.stdin:
        k, t = lin.split()
        k, t = int(k), int(t)
        z = k
        cont = 1
        while k != t:
            z *= 2
            k += (z)
            cont += 1
        print(cont)
