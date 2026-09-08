# ♟️ BOTCHESS: Agente Autónomo de Ajedrez con IA y Visión Computacional

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![YOLOv8](https://img.shields.io/badge/YOLO-v8-yellow.svg)
![Stockfish](https://img.shields.io/badge/Stockfish-16.1-green.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Vision-red.svg)

BOTCHESS es un sistema robótico de software (RPA) y visión artificial diseñado para jugar ajedrez de forma completamente autónoma en interfaces digitales. El agente "ve" la pantalla, interpreta la posición de las piezas, calcula matemáticamente la jugada óptima y toma el control del cursor para ejecutar el movimiento físico.

*(Inserta aquí un GIF o imagen de tu bot jugando)*
<!-- ![Demo BOTCHESS](enlace_a_tu_imagen_o_gif.gif) -->

## 🧠 Arquitectura del Sistema

El proyecto orquesta múltiples tecnologías en un flujo de trabajo continuo de 5 pasos:

1. **Captura en Tiempo Real:** Análisis continuo de la región del tablero en la pantalla.
2. **Visión Computacional (YOLOv8):** Un modelo neuronal entrenado a medida detecta y clasifica la posición exacta de las 32 piezas y las casillas del tablero.
3. **Traducción Espacial:** Las coordenadas de los *bounding boxes* se transforman matemáticamente en notación estándar **FEN** (Forsyth-Edwards Notation).
4. **Motor de Inferencia:** Se inyecta la cadena FEN al motor **Stockfish**, el cual evalúa millones de posiciones por segundo para determinar la jugada con mayor probabilidad de victoria.
5. **Ejecución Física (PyAutoGUI):** El sistema toma control del ratón del sistema operativo, traduciendo la jugada (ej. `e2e4`) en coordenadas de píxeles (X, Y) para arrastrar y soltar la pieza en la interfaz.

## ⚙️ Tecnologías Utilizadas

* **Lenguaje Core:** Python
* **Visión Artificial:** Ultralytics YOLOv8 / OpenCV
* **Motor de Ajedrez:** Stockfish
* **Automatización GUI:** PyAutoGUI
* **Tratamiento de Datos:** NumPy / Pandas

## 🚀 Instalación y Configuración

> **Nota de Arquitectura:** Por buenas prácticas y para mantener el repositorio ligero, el motor de Stockfish y los pesos del modelo YOLO (`.pt`) no están incluidos en este repositorio.

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TuUsuario/BOTCHESS.git](https://github.com/TuUsuario/BOTCHESS.git)
   cd BOTCHESS
