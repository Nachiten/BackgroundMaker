from PIL import Image
import numpy

'''
def printearMatriz():
    for unaFila in range(0, height):
        for unaColumna in range(0, width):
            print(numpy_array[unaFila][unaColumna], end=" ")
        print("")
'''


def reemplazarColores():
    for unaFila in range(0, height):
        for unaColumna in range(0, width):
            for unNum in range(0, len(coloresAReemplazar)):
                if coloresAReemplazar[unNum][0] == numpy_array[unaFila][unaColumna][0] and \
                        coloresAReemplazar[unNum][1] == numpy_array[unaFila][unaColumna][1] and \
                        coloresAReemplazar[unNum][2] == numpy_array[unaFila][unaColumna][2]:
                    numpy_array[unaFila][unaColumna] = coloresReemplazados[unNum]
        if unaFila % 100 == 0:
            porcentajeTerminado = unaFila * 100 / height
            print("Porcentaje terminado: " + str(porcentajeTerminado))


def leerPaleta():
    imagePaleta = Image.open("C:\\Users\ignac\Desktop\Imagenes\ModeloPaleta" + str(numeroPaleta) + ".png")
    imagePaleta = imagePaleta.convert('RGBA')
    numpy_arrayPaleta = numpy.array(imagePaleta)
    for unNum in range(0, len(coloresAReemplazar)):
        coloresReemplazados.append(numpy_arrayPaleta[0][unNum])


numeroPaleta = 0

for unNumFor in range(5, 6):
    numeroPaleta = unNumFor

    image = Image.open("C:\\Users\ignac\Desktop\Imagenes\ImagenModelo.png")
    image = image.convert('RGBA')
    numpy_array = numpy.array(image)

    width, height = image.size

    coloresAReemplazar = [(0, 0, 0, 255), (255, 255, 255, 255), (50, 50, 50, 255), (180, 180, 180, 255)]
    coloresReemplazados = []

    leerPaleta()
    reemplazarColores()

    im2 = Image.fromarray(numpy_array)
    im2.save("C:\\Users\ignac\Desktop\Imagenes\ImagenEditada" + str(numeroPaleta) + ".png")
