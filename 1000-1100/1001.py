"""Material
solo leemos, almacenamos en un vector y mostramos"""

N = int(input())
vector = []
for i in range(0, N):   #leemos
    vector.append(input())

for i in vector:        #mostramos
    print(i)