diccionario = { 'a' : True , 5: "esto es un string", (1,2) : False }

#insertar
diccionario['c']= "nuevo string"
print (diccionario)

#modificar
diccionario['a']= False
print (diccionario)

#eliminar
del diccionario[5]
print (diccionario)
