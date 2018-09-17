from PIL import Image

im = Image.open('imagen.jpg') # Can be many different formats.
pix = im.load()
width, height = im.size
print (im.size)  # Get the width and hight of the image for iterating over
print (pix[0,0])  # Get the RGBA Value of the a pixel of an image
#Recorremos la imagen
for i in range(0,width):
    for j in range(0,height):
        print (pix[i,j])
im.save('imagen_modificada.png')  # Save the modified pixels as .png
