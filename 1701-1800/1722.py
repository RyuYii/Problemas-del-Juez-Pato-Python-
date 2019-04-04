# Pedro y las partidas

partidas = int(input())
datos = []
for i in range(partidas):
    datos.append(input())
if datos.count("2") > datos.count("1"):
    print("Gana el jugador 2!")
else:
    print("Gana el jugador 1!")
