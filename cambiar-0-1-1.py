from PIL import Image

im = Image.open('imagen.jpg') 
original = im.load()
width, height = im.size
copia = Image.new("RGB",im.size)
gris = copia.load()

print("Seleccione a que tonalidad quiere convertir la imagen:")
print(" 1.-Gris\n 2.-Gris 2.0\n 3.-Rojo\n 4.-Verde\n 5.-Azul\n 6.-Inverso\n 7.-Sepia\n")
num=int(input())


if num == 1:
	for i in range(0,width):
		for j in range(0,height):
			media = int((original[i,j][0]+original[i,j][1]+original[i,j][2])/3)
			gris[i,j] = (media, media, media)

	im.show()
	copia.show()
	copia.save('imagen_gris.png')

elif num == 2:
	for i in range(0,width):
		for j in range(0,height):
			media = int((original[i,j][0]*0.2989)+(original[i,j][1]*0.5870)+(original[i,j][2]*0.1140))
			gris[i,j] = (media, media, media)
	im.show()
	copia.show()
	copia.save('imagen_gris2.png')

elif num == 3:
	for i in range(0,width):
		for j in range(0,height):
			gris[i,j] = (original[i,j][0], 0, 0)
	im.show()
	copia.show()
	copia.save('imagen_rojo.png')


elif num == 4:
	for i in range(0,width):
		for j in range(0,height):
			gris[i,j] = (0, original[i,j][1], 0)
	im.show()
	copia.show()
	copia.save('imagen_verde.png')


elif num == 5:
	for i in range(0,width):
		for j in range(0,height):
			gris[i,j] = (0, 0, original[i,j][2])
	im.show()
	copia.show()
	copia.save('imagen_azul.png')

elif num == 6:
	for i in range(0,width):
		for j in range(0,height):
			r=int(255-original[i,j][0])
			g=int(255-original[i,j][1])
			b=int(255-original[i,j][2])


			gris[i,j] = (r, g, b)
	im.show()
	copia.show()
	copia.save('imagen_inverso.png')

elif num == 7:
	for i in range(0,width):
		for j in range(0,height):
			tr=int((original[i,j][0]*0.393)+(original[i,j][1]*0.769)+(original[i,j][2]*0.189))
			tg=int((original[i,j][0]*0.349)+(original[i,j][1]*0.686)+(original[i,j][2]*0.168))
			tb=int((original[i,j][0]*0.272)+(original[i,j][1]*0.534)+(original[i,j][2]*0.131))

			if tr>255:
				r=255
			else:
				r=tr

			if tg>255:
				g=255
			else:
				g=tg

			if tb>255:
				b=255
			else:
				b=tb
			gris[i,j] = (r, g, b)
	im.show()
	copia.show()
	copia.save('imagen_sepia.png')

else:
	print("No existe esta opción")



  
