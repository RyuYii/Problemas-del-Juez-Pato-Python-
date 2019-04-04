# Productos

'''Funcion recursiva para multiplicar los digitos de un numero'''
def mul_digitos(n):
    if n//10 == 0:
        return n
    else:
        return mul_digitos(n//10)*(n%10)


casos = int(input())
for i in range(casos):
    n = int(input())
    cont = 0
    while n > 9:
        cont += 1
        n = mul_digitos(n)
    print(cont, "pasos")

