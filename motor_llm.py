from stockfish import Stockfish

def obtener_mejor_jugada(fen):
    try:
        # Apuntamos al ejecutable que acabas de meter en tu carpeta
        motor = Stockfish(path="stockfish.exe")
        
        # Nivel de habilidad (20 es el máximo, el terror de los Grandes Maestros)
        motor.set_skill_level(20) 
        
        # Validación de seguridad: verificamos que la cámara no haya fallado
        if motor.is_fen_valid(fen):
            motor.set_fen_position(fen)
            
            # Le damos 500 milisegundos para pensar la mejor jugada
            mejor_movimiento = motor.get_best_move_time(500) 
            return mejor_movimiento
        else:
            print("ERROR INTERNO: El modelo visual generó un FEN inválido.")
            return None
            
    except Exception as e:
        print(f"Error fatal con Stockfish: {e}")
        print("Asegúrate de que el archivo 'stockfish.exe' está dentro de la carpeta BOTCHESS.")
        return None