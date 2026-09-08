import pyautogui
import time

print("Rastreador de coordenadas activado.")
print("Mueve el ratón por la pantalla para ver las coordenadas (X, Y).")
print("Presiona Ctrl + C en esta ventana para detenerlo.\n")

try:
    while True:
        # Obtiene la posición actual del ratón
        x, y = pyautogui.position()
        # Imprime las coordenadas reescribiendo la misma línea para no llenar la pantalla
        print(f"Posición actual -> X: {x:4} | Y: {y:4}", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n\n¡Calibración terminada!")