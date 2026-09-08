import pyautogui
import time

def ejecutar_movimiento(movimiento_uci, origen_x, origen_y, ancho_tablero, juego_con_blancas=True):
    """
    Toma una jugada como 'e2e4' y mueve el ratón físicamente en la pantalla.
    """
    # 1. Separar la jugada en origen (e2) y destino (e4)
    casilla_origen = movimiento_uci[0:2]
    casilla_destino = movimiento_uci[2:4]

    # 2. Tamaño de cada casilla en píxeles
    tamano_casilla = ancho_tablero / 8

    # 3. Matemática para convertir notación de ajedrez en coordenadas X, Y
    def calcular_coordenadas(casilla):
        letras = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        columna = letras[casilla[0]]
        fila = int(casilla[1]) - 1

        if juego_con_blancas:
            # Si juegas con blancas, la fila 1 está abajo en la pantalla (mayor Y)
            fila_tablero = 7 - fila  
        else:
            # Si juegas con negras, el tablero está invertido
            columna = 7 - columna 
            fila_tablero = fila

        # Calcular el centro exacto de la casilla
        centro_x = origen_x + (columna * tamano_casilla) + (tamano_casilla / 2)
        centro_y = origen_y + (fila_tablero * tamano_casilla) + (tamano_casilla / 2)
        
        return centro_x, centro_y

    # 4. Obtener las coordenadas físicas finales
    x_origen, y_origen = calcular_coordenadas(casilla_origen)
    x_destino, y_destino = calcular_coordenadas(casilla_destino)

    # 5. Mover el ratón y hacer los clics (con un ligero retraso para imitar a un humano)
    pyautogui.moveTo(x_origen, y_origen, duration=0.2)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.moveTo(x_destino, y_destino, duration=0.2)
    pyautogui.click()