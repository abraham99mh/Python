#Archivo de entrada
f = open("texto.txt", "r")
#Archivo de salida
s = open("salida.txt", "w")
text = f.readlines()

for linea in text:
    s.write(str(len(linea))+" caracteres por linea\n")
f.close()
s.close()
