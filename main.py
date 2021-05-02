from PIL import Image
import numpy

'''
def contarColoresExistenes():
    for unaFila in range(0, height):
        for unaColumna in range(0, width):
            colorActual = numpy_array[unaFila][unaColumna]

            if noExisteEnArray(colorActual):
                coloresExistentes.append(colorActual)


def noExisteEnArray(unaTupla):
    for unaTuplaColor in coloresExistentes:
        if unaTupla[0] == unaTuplaColor[0] and \
                unaTupla[1] == unaTuplaColor[1] and \
                unaTupla[2] == unaTuplaColor[2]:
            return False
    return True
'''


def printearMatriz():
    for unaFila in range(0, height):
        for unaColumna in range(0, width):
            print(numpy_array[unaFila][unaColumna], end=" ")
        print("")


def reemplazarColores():
    for unaFila in range(0, height):
        for unaColumna in range(0, width):
            for unNum in range(0, len(coloresAReemplazar)):
                if estaEnUnMargen(numpy_array[unaFila][unaColumna], 0, unNum) and \
                        estaEnUnMargen(numpy_array[unaFila][unaColumna], 1, unNum) and \
                        estaEnUnMargen(numpy_array[unaFila][unaColumna], 2, unNum):
                    numpy_array[unaFila][unaColumna] = coloresReemplazados[unNum]
        if unaFila % 100 == 0:
            porcentajeTerminado = unaFila * 100 / height
            print("Porcentaje terminado: " + str(porcentajeTerminado))


def estaEnUnMargen(unaTupla, indexColor, indexArray):
    margen = 1
    return coloresAReemplazar[indexArray][indexColor] - margen <= \
           unaTupla[indexColor] <= \
           coloresAReemplazar[indexArray][indexColor] + margen


def leerPaleta():
    imagePaleta = Image.open("C:\\Users\ignac\Desktop\Imagenes\ModeloPaleta" + str(numeroPaleta) + ".png")
    imagePaleta = imagePaleta.convert('RGBA')
    numpy_arrayPaleta = numpy.array(imagePaleta)
    for unNum in range(0, len(coloresAReemplazar)):
        coloresReemplazados.append(numpy_arrayPaleta[0][unNum])


numeroPaleta = 0

for unNumFor in range(4, 6):

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
