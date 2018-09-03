
lista = [4,12,8,2,1]


#anexar
lista.append(7)
print (lista)

#insertar
lista.insert(0,9)
print (lista)

#modificar
lista[1]=13
print(lista)

#eliminar
del lista[2]
print(lista)

lista.remove(2)
print (lista)

#ordenar
for recorrido in range(1,len(lista)):
	for posicion in range(len(lista)- recorrido):
		if lista [posicion] > lista[posicion + 1]:
			temp = lista[posicion]
			lista[posicion] = lista[posicion + 1]
			lista [posicion + 1] = temp

print (lista)