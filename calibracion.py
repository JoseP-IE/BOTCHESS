import cv2
import numpy as np
import mss
import time

# ==========================================
# CALIBRACIÓN DEL TABLERO DE AJEDREZ
# ==========================================

# 1. Ajusta estos valores hasta que el rectángulo verde cubra EXACTAMENTE tu tablero
# (excluyendo bordes, nombres de jugadores, o letras/números de las casillas)
MONITOR = {"top": 150, "left": 150, "width": 800, "height": 800}

# ¿Juegas con blancas o negras? Esto invierte el mapeo matemático de las coordenadas
JUEGO_CON_BLANCAS = True 

def dibujar_cuadricula(imagen):
    """Dibuja una cuadrícula de 8x8 sobre la imagen capturada para verificar la alineación."""
    alto, ancho, _ = imagen.shape
    paso_x = ancho // 8
    paso_y = alto // 8

    # Dibujar líneas verticales y horizontales
    for i in range(1, 8):
        # Líneas verticales
        cv2.line(imagen, (i * paso_x, 0), (i * paso_x, alto), (0, 255, 0), 1)
        # Líneas horizontales
        cv2.line(imagen, (0, i * paso_y), (ancho, i * paso_y), (0, 255, 0), 1)

    # Etiquetar las casillas
    columnas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    filas = ['8', '7', '6', '5', '4', '3', '2', '1']
    
    if not JUEGO_CON_BLANCAS:
        columnas.reverse()
        filas.reverse()

    for fila_idx in range(8):
        for col_idx in range(8):
            casilla = f"{columnas[col_idx]}{filas[fila_idx]}"
            
            # Calcular el centro de la casilla para poner el texto
            centro_x = (col_idx * paso_x) + (paso_x // 2) - 10
            centro_y = (fila_idx * paso_y) + (paso_y // 2) + 5
            
            # Poner el nombre de la casilla en texto claro
            cv2.putText(imagen, casilla, (centro_x, centro_y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
            
            # Dibujar un pequeño punto en el centro de cada casilla (donde hará clic PyAutoGUI)
            cv2.circle(imagen, (centro_x + 10, centro_y - 5), 2, (255, 0, 0), -1)
            
    return imagen

def main():
    print("Iniciando Calibrador Visual...")
    print("Mueve tu ventana de ajedrez o ajusta las variables en MONITOR en el código.")
    print("Presiona 'q' en la ventana de OpenCV para salir.")
    
    with mss.mss() as sct:
        while True:
            # Capturar la región definida
            captura = sct.grab(MONITOR)
            imagen = cv2.cvtColor(np.array(captura), cv2.COLOR_BGRA2BGR)
            
            # Dibujar la cuadrícula de calibración
            imagen_anotada = dibujar_cuadricula(imagen)
            
            # Mostrar la imagen
            cv2.imshow("Calibracion de Tablero", imagen_anotada)
            
            # Salir con 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
            time.sleep(0.05) # Pequeña pausa para no saturar CPU

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
