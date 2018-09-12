a = open("txt2.txt")
b = open("salida2.txt", "w")
l = a.readlines()
dicc = { }

for linea in l:

	for letra in linea:

		if letra in dicc:
			dicc[letra]+=1
		else :
			dicc[letra]=1
	
	
	b.write(str(dicc)+ "\n")
	dicc = { }
	
a.close()
b.close()