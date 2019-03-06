import sys
def cambio(num, base):
    print(int(str(num),base))

if __name__ == '__main__':
    for line in sys.stdin:
        n = int(line)
        c = []
        for i in  range(0, n):
            c.append(int(input()))
        sum = 0
        for i in c:
            sum += i
        print(sum)