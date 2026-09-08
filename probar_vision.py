import cv2
from ultralytics import YOLO

# 1. Cargar tu modelo recién entrenado
modelo = YOLO("best.pt")

# 2. Leer la imagen y pasarla por la red neuronal
resultados = modelo("imagen_prueba.png")

# 3. Dibujar las "bounding boxes" sobre la imagen
imagen_anotada = resultados[0].plot()

# 4. Mostrar el resultado en pantalla
cv2.imshow("Prueba de Deteccion de Ajedrez", imagen_anotada)
cv2.waitKey(0) # La ventana se quedará abierta hasta que presiones cualquier tecla