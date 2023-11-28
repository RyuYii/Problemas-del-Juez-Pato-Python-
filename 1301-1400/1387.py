def x(num,aux):
    cp = 0
    while True:
        a = num // 10
        b = num % 10
        suma = a + b
        c = suma % 10
        u = int(f'{b}{c}')
        num = u
        cp += 1
        if aux == num:
            break
    print(cp)
while True:
    try:
        num = int(input());
        if num == "":
            break
        aux = num
        if num >= 9:
            x(num,aux)
        else:
            x(num,aux)
    except(EOFError):
        break
