import numpy
from skimage.io import imshow
import cv2
from matplotlib import pyplot as plot

# Constantes
IMAGE1_PATH = "imagenes/image1.jpg"
IMAGE2_PATH = "imagenes/image2.jpg"

IMAGE1_CROPPED_PATH = "imagenes/image1_crop.jpg"
IMAGE2_CROPPED_PATH = "imagenes/image2_crop.jpg"

IMAGE1_CROPPED_GRAYSCALE_PATH = "imagenes/image1_crop_gris.jpg"
IMAGE2_CROPPED_GRAYSCALE_PATH = "imagenes/image2_crop_gris.jpg"

DIMENSION = 500

INITIAL_X = 200
FINAL_X = INITIAL_X + DIMENSION
INITIAL_Y = 900
FINAL_Y = INITIAL_Y + DIMENSION


def crop_image(img_path: str, img_cropped_path: str, initial_x: int, final_x: int, initial_y: int,
               final_y: int) -> None:
    """
    Esta función recibe una imagen y devuelve otra imagen recortada.

    Args:
      img_path (str): Ruta de la imagen original que se desea recortar.
      img_cropped_path (str): Ruta donde se guardará la imagen recortada.
      initial_x (int): Coordenada x inicial del área de recorte.
      final_x (int): Coordenada x final del área de recorte.
      initial_y (int): Coordenada y inicial del área de recorte.
      final_y (int): Coordenada y final del área de recorte.

    Return
      None
    """
    try:
        # Abrir la imagen
        image = cv2.imread(img_path)

        # Obtener la imagen recortada
        image_crop = image[initial_x:final_x, initial_y:final_y]

        # Guardar la imagen recortada en la ruta indicada
        cv2.imwrite(img_cropped_path, image_crop)

        print("Imagen recortada con éxito. El tamaño de la imagen es de" + str(image_crop.shape))
    except Exception as e:
        print("Ha ocurrido un error:", str(e))


def step_1_and_2(path_to_img: str) -> None:
    """
    En este paso cargamos una imagen e imprimimos el tamaño de la misma.

    :param path_to_img: El path a la imagen a cargar.
    :return: None
    """
    try:
        # Abrir la imagen
        image = cv2.imread(path_to_img)

        imshow(image)
        plot.show()
        print(f"Imagen cargada con éxito. El tamaño de la {path_to_img} es de" + str(image.shape))
    except Exception as e:
        print("Ha ocurrido un error:", str(e))


def step_3(path_to_img: str, path_to_cropped_img: str, initial_x: int, final_x: int, initial_y: int,
           final_y: int) -> None:
    """
    En este paso, recortamos una imagen, dados parámetros iniciales para los ejes X e Y, y guardamos el resultado
    en el path dado para la imagen recortada.

    :param path_to_img: Path a la imagen a recortar.
    :param path_to_cropped_img: Path donde se guardará el resultado.
    :param initial_x: Punto inicial en el eje vertical.
    :param final_x: Punto final en el eje vertical.
    :param initial_y: Punto inicial en el eje horizontal.
    :param final_y: Punto final en el eje horizontal.
    :return: None.
    """
    crop_image(path_to_img, path_to_cropped_img, initial_x, final_x, initial_y, final_y)
    imshow(path_to_cropped_img)
    plot.show()


def step_4(path_to_cropped_img: str) -> None:
    """
    En este paso imprimimos el resultado de cargar una imagen, dado un path, en consola, para mostrarla en
    formato de matriz.

    :param path_to_cropped_img: Path a la imagen recortada.
    :return: None.
    """
    try:
        # Abrir la imagen
        image = cv2.imread(path_to_cropped_img)

        print(image)
        print("El tamaño de la matriz que forma la imagen es de " + str(image.shape[0]) + "x" + str(image.shape[1])
              + ", con 3 canales de colores, es decir, cada elemento de la matriz es una colección de 3 valores")
    except Exception as e:
        print("Ha ocurrido un error:", str(e))


def step_5(path_to_cropped_img: str) -> None:
    """
    En este paso, calculamos la matriz traspuesta (intercambiar filas por columnas) de la matriz resultante de
    cargar una imagen dado un path.

    :param path_to_cropped_img: Path a la imagen recortada.
    :return: None.
    """
    try:
        # Abrir la imagen
        image = cv2.imread(path_to_cropped_img)

        # Usamos cv2 para convertir la imagen de BGR (formato que usa cv2 por defecto) a RGB (formato que usa matplotlib)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # transpone únicamente los ejes X e Y, no el Z
        transposed = numpy.transpose(image, axes=(1, 0, 2))

        imshow(transposed)
        plot.show()
    except Exception as e:
        print("Ha ocurrido un error:", str(e))


def step_6(path_to_cropped_img: str, path_to_cropped_grayscale_img: str) -> None:
    """
    Transforma una imagen en BGR a escala de grises, utilizando la función cvtColor de la librería OpenCV, la cual por detrás,
    seguramente utilice R+G+B/3 para calcular el nuevo valor de cada uno de los canales de color de un pixel.
    Finalmente, guarda la nueva imagen en escala de grises, en el path dado para esta.

    :param path_to_cropped_img: Path a la imágen recortada.
    :param path_to_cropped_grayscale_img: Path donde se almacenará la imagen resultante.
    :return: None.
    """
    try:
        # Abrir la imagen
        image = cv2.imread(path_to_cropped_img)

        # Convertir la imagen a escala de grises
        # Transforma el color de cada canal (R, G y B) en el mismo valor, calculado como R+G+B/3
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Guardar la imagen en escala de grises
        cv2.imwrite(path_to_cropped_grayscale_img, gray_image)

        imshow(gray_image)
        plot.show()
    except Exception as e:
        print("Ha ocurrido un error:", str(e))


def step_7(path_to_cropped_grayscale_img: str) -> None:
    """
    Verifica si la matriz resultante de cargar una imagen, es invertible y en caso de serlo,
    la invierte e imprime en consola la misma imagen, invertida, en formato de matriz.

    :param path_to_cropped_grayscale_img: Path a la imagen recortada en escala de grises.
    :return: None.
    """
    try:
        # Cargar imagen y utilizar únicamente uno de los canales, ya que los valores de los 3 canales es el mismo
        image = cv2.imread(path_to_cropped_grayscale_img)[:, :, 0]

        # Verificar si es invertible
        determinant = numpy.linalg.det(image)
        if determinant == 0:
            print("La matriz no es invertible :(")
            return
        else:
            print("La matriz es invertible")

        # Invertir finalmente la matriz
        inverse = numpy.linalg.inv(image)
        print(inverse)
    except Exception as e:
        print("Ha ocurrido un error:", str(e))


def step_8(path_to_cropped_grayscale_img: str, scalar: float) -> None:
    """
    En este paso, multiplicamos la matriz por el escalar dado, y mostramos la imagen resultante.

    :param path_to_cropped_grayscale_img: Path a la imagen recortada en escala de grises.
    :param scalar: Número por el cual multiplicaremos cada valor de la matriz.
    :return: None.
    """
    try:
        # Cargar la imagen
        image = cv2.imread(path_to_cropped_grayscale_img)

        image = numpy.multiply(image, scalar).astype(numpy.uint8)

        # Verificamos que los valores no sean menor a 0 o mayor a 255 (en RGB se utilizan únicamente valores de 0 a 255)
        image = numpy.clip(image, min=0, max=255)

        imshow(image)
        plot.show()
    except Exception as e:
        print("Ha ocurrido un error:", str(e))


def paso9(path_to_cropped_grayscale_img: str) -> None:
    """
    En este paso, rotamos la imagen en el eje vertical, utilizando una matriz con 1 en la anti diagonal, y 0 en el
    resto de los espacios.

    :param path_to_cropped_grayscale_img: Path a la imagen recortada en escala de grises.
    :return: None.
    """
    try:
        # Cargar imagen y utilizar únicamente uno de los canales, ya que los valores de los 3 canales es el mismo
        image = cv2.imread(path_to_cropped_grayscale_img)[:, :, 0]

        # Obtenemos la matriz identidad
        identity = numpy.eye(DIMENSION)

        # Rotamos la matriz identidad en el eje vertical
        w = numpy.fliplr(identity)

        flipped = numpy.dot(image, w)

        plot.imshow(flipped, cmap='gray')
        plot.show()
    except Exception as e:
        print("Ha ocurrido un error:", str(e))


def paso10(path_to_cropped_grayscale_img: str) -> None:
    """
    En este paso obtenemos la imagen en negativo de una imagen dada.

    :param path_to_cropped_grayscale_img: Path a la imagen recortada en escala de grises.
    :return: None.
    """
    try:
        # Cargar imagen y utilizar únicamente uno de los canales, ya que los valores de los 3 canales es el mismo
        image = cv2.imread(path_to_cropped_grayscale_img)[:, :, 0]
        auxiliar = numpy.full((500, 500), 255)

        result = auxiliar - image

        plot.imshow(result, cmap='gray')
        plot.show()
    except Exception as e:
        print("Ha ocurrido un error:", str(e))


if __name__ == '__main__':
    # Ejecutamos los pasos en orden
    step_1_and_2(IMAGE1_PATH)
    step_1_and_2(IMAGE2_PATH)
    step_3(IMAGE1_PATH, IMAGE1_CROPPED_PATH, INITIAL_X, FINAL_X, INITIAL_Y, FINAL_Y)
    step_3(IMAGE2_PATH, IMAGE2_CROPPED_PATH, INITIAL_X, FINAL_X, INITIAL_Y, FINAL_Y)
    step_4(IMAGE1_CROPPED_PATH)
    step_5(IMAGE1_CROPPED_PATH)
    step_6(IMAGE1_CROPPED_PATH, IMAGE1_CROPPED_GRAYSCALE_PATH)
    step_6(IMAGE2_CROPPED_PATH, IMAGE2_CROPPED_GRAYSCALE_PATH)

    # De aquí en adelante, usamos las imagenes en escala de grises
    step_7(IMAGE1_CROPPED_GRAYSCALE_PATH)
    step_7(IMAGE2_CROPPED_GRAYSCALE_PATH)
    step_8(IMAGE1_CROPPED_PATH, 2)
    step_8(IMAGE1_CROPPED_PATH, 0.2)
    paso9(IMAGE1_CROPPED_GRAYSCALE_PATH)
    paso10(IMAGE1_CROPPED_GRAYSCALE_PATH)
