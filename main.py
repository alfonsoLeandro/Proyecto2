from skimage.io import imshow, imread
import cv2

def recortar_imagen_v2(ruta_img: str, ruta_img_crop: str, x_inicial: int, x_final: int, y_inicial: int, y_final: int)-> None:
    """
    Esta función recibe una imagen y devuelve otra imagen recortada.

    Args:
      ruta_img (str): Ruta de la imagen original que se desea recortar.
      ruta_img_crop (str): Ruta donde se guardará la imagen recortada.
      x_inicial (int): Coordenada x inicial del área de recorte.
      x_final (int): Coordenada x final del área de recorte.
      y_inicial (int): Coordenada y inicial del área de recorte.
      y_final (int): Coordenada y final del área de recorte.

    Return
      None
    """
    try:
        # Abrir la imagen
        image = cv2.imread("./image1.jpeg")

        # Obtener la imagen recortada
        image_crop = image[x_inicial:x_final, y_inicial:y_final]

        # Guardar la imagen recortada en la ruta indicada
        cv2.imwrite(ruta_img_crop, image_crop)

        print("Imagen recortada con éxito. El tamaño de la imagen es de" + str(image_crop.shape))
    except Exception as e:
        print("Ha ocurrido un error:", str(e))

def paso_1(path):
    try:
        # Abrir la imagen
        image = cv2.imread(path)

        imshow("./image1.jpeg")
        print(f"Imagen cargada con éxito. El tamaño de la {path} es de" + str(image.shape))
    except Exception as e:
        print("Ha ocurrido un error:", str(e))


ruta_img = "imagenes/aldeano.jpeg"
ruta_img_crop = "imagenes/aldeano_crop.jpeg"
ruta_img2 = "imagenes/badass.jpeg"
ruta_img_crop2 = "imagenes/badass_crop.jpeg"

x_inicial = 50
x_final = 300
y_inicial = 100
y_final = 400

recortar_imagen_v2(ruta_img, ruta_img_crop, x_inicial, x_final, y_inicial, y_final)
recortar_imagen_v2(ruta_img, ruta_img_crop, x_inicial, x_final, y_inicial, y_final)
paso_1("./image1.jpeg")
paso_1("./image2.jpg")