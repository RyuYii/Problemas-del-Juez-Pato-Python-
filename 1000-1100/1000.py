"""el juez virtual tiene casos de prueba como el siguiente:
2 3
que vienen en una sola linea, y en python se lee linea por linea
2
3
para esto tenemos una solucion:
"""
#primero leemos los datos que vienen en una linea como si fuese una cadena
v = input()
#separamos por espacios y guardamos en una lista
d = v.split()
#obtenemos los numeros convirtiendolos porque eran strings
x = int(d[0])
y = int(d[1])
#imprimimos la suma
print(x+y)