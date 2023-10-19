"""Bob el jardinero"""
# de hecho se cambio por el estilo de redondeo de C, pero me dio flojera actualizar nombres :v
def round_java_style(numero, decimales=2):
    return int(numero * 100 + 0.5) / 100

def calcular_porcentaje_de_frutas(cadena):
    frutas = 'aeiou'
    total = len(cadena)
    
    porcentajes = {}
    for fruta in frutas:
        count = cadena.count(fruta)
        porcentaje = (count * 100) / total
        porcentajes[fruta] = round_java_style(porcentaje)
    
    return porcentajes

# Función principal para procesar múltiples casos de prueba
def procesar_casos_de_prueba(casos):
    c = 1
    for caso in casos:
        resultado = calcular_porcentaje_de_frutas(caso)
        print(f'Caso {c}:')
        c += 1
        for fruta, porcentaje in resultado.items():
            print(f"{fruta}= {porcentaje:.2f}")

if __name__ == "__main__":
    T = int(input())
    casos = []
    for _ in range(T):
        cadena = input()
        casos.append(cadena)
    
    procesar_casos_de_prueba(casos)
