#casi igual
import sys

if __name__ == '__main__':
    for i in sys.stdin:
        a, b = i.split()
        cont = 0
        for j in range(len(a)):
            if a[j] != b[j]:
                cont += 1
                if cont > 1:
                    break
        if cont <= 1:
            print('feliz')
        else:
            print('lentes')
