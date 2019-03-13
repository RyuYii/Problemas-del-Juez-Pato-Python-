"""Bob el jardinero"""

casos = int(input())
for n in range(0, casos):
    cadena = input()
    a = cadena.count("a")
    e = cadena.count("e")
    i = cadena.count("i")
    o = cadena.count("o")
    u = cadena.count("u")
    total = len(cadena)
    print("Caso {0}:".format(n+1))
    print("a=", "{0:.2f}".format((a * 100) / total))
    print("e=", "{0:.2f}".format((e * 100) / total))
    print("i=", "{0:.2f}".format((i * 100) / total))
    print("o=", "{0:.2f}".format((o * 100) / total))
    print("u=", "{0:.2f}".format((u * 100) / total))
