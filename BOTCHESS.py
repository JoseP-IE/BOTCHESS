import cv2
import numpy as np
import mss
from ultralytics import YOLO
import time

# Importar los submódulos que construimos
import traductor_fen
import motor_llm
import ejecutor_movimientos

# ==========================================
# 1. CONFIGURACIÓN GENERAL
# ==========================================
# Pega tu llave completa entre las comillas manteniendo el "nvapi-"
MODELO_NVIDIA = "llama3.1"

# Tus coordenadas calibradas
ORIGEN_X = 250
ORIGEN_Y = 179
ANCHO_TABLERO = 785

print("Cargando el modelo visual (YOLO)...")
modelo_vision = YOLO("best.pt")

# ==========================================
# 2. FUNCIONES DEL AGENTE (Actualizado)
# ==========================================
def capturar_tablero():
    """Toma una foto rápida y exacta de la región del tablero en tu pantalla"""
    region = {"top": ORIGEN_Y, "left": ORIGEN_X, "width": ANCHO_TABLERO, "height": ANCHO_TABLERO}
    with mss.MSS() as sct:
        captura = sct.grab(region)
        img = np.array(captura)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    return img

def leer_tablero():
    """Captura la pantalla, pasa la red neuronal y devuelve el texto FEN."""
    imagen_tablero = capturar_tablero()
    
    # Inferencia de YOLO
    resultados_yolo = modelo_vision(imagen_tablero, conf=0.3, verbose=False)
    cajas = resultados_yolo[0].boxes
    nombres_clases = resultados_yolo[0].names
    
    # Traducción Matemática
    cadena_fen = traductor_fen.mapear_detecciones_a_fen(cajas, ANCHO_TABLERO, nombres_clases, juego_con_blancas=True)
    return cadena_fen

# ==========================================
# 3. BUCLE DE CONTROL AUTÓNOMO (La línea de producción)
# ==========================================
print("\n¡SISTEMA 100% AUTÓNOMO ACTIVADO!")
print("Presiona Ctrl + C en esta consola para apagar la máquina de emergencia.")

# Memoria inicial: Leemos el tablero antes de empezar
ultimo_fen = leer_tablero()
print(f"Tablero inicial memorizado: {ultimo_fen}")

while True:
    try:
        # El sensor revisa la línea cada 1 segundo
        fen_actual = leer_tablero()
        
        # Si la foto cambió, alguien movió
        if fen_actual != ultimo_fen:
            print("\n[!] Movimiento detectado en el tablero.")
            
            # 1. TIEMPO DE ASENTAMIENTO: Dejamos que la pieza enemiga aterrice
            time.sleep(1.5) 
            
            # Volvemos a leer ya sin piezas "volando"
            fen_estable = leer_tablero()
            print(f"Analizando posición estable: {fen_estable}")
            
            # Consultamos a Stockfish
            mejor_jugada = motor_llm.obtener_mejor_jugada(fen_estable)
            
            if mejor_jugada:
                print(f"¡Ejecutando maniobra física!: {mejor_jugada}")
                # El bot mueve el ratón físicamente
                ejecutor_movimientos.ejecutar_movimiento(mejor_jugada, ORIGEN_X, ORIGEN_Y, ANCHO_TABLERO, juego_con_blancas=True)
                
                # 2. TIEMPO DE ASENTAMIENTO POST-JUGADA: Esperamos a soltar nuestra pieza
                time.sleep(1.0)
                
                # 3. ACTUALIZAR MEMORIA: Tomamos una foto de cómo dejamos el tablero
                ultimo_fen = leer_tablero()
                print("Turno finalizado. Esperando movimiento del oponente...")
            else:
                print("Stockfish no encontró jugada. ¿Jaque Mate o Error?")
                time.sleep(5)
                
        else:
            # El tablero sigue igual, dormimos el sensor para no quemar el CPU
            time.sleep(1.0)
            
    except KeyboardInterrupt:
        print("\n[!] Apagado de emergencia activado. ¡Línea detenida!")
        break