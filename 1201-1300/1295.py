"""problema de cifrado"""
import sys
dic = "abcdefghijklmnopqrstuvwxyz" 		#aqui tendremos la referencia para el alfabeto
if __name__ == "__main__":
	for cod in sys.stdin:				#leemos el diccionario
		n = int(input())				#la cantidad de frases a traducir
		for i in range(0, n):
			trad = ""					#para la traduccion
			cad = input()
			for letra in cad:			#vamos caracter por caracter
				if letra != " ":
					trad += dic[cod.index(letra)]
				else:
					trad += " "
			print(trad)					#tenemos la linea traducida
		print("")						#el salto de linea que se pide
