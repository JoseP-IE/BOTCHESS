def mapear_detecciones_a_fen(cajas_yolo, ancho_tablero, nombres_clases, juego_con_blancas=True):
    # 1. Crear tablero virtual vacío
    tablero_virtual = [["" for _ in range(8)] for _ in range(8)]
    tamano_casilla = ancho_tablero / 8  

    # 2. Acomodar las piezas detectadas
    for caja in cajas_yolo:
        clase_id = int(caja.cls[0].item())
        nombre_clase = nombres_clases[clase_id]
        
        if nombre_clase == "board":
            continue

        x_centro = caja.xywh[0][0].item()
        y_centro = caja.xywh[0][1].item()

        columna_idx = int(x_centro // tamano_casilla)
        fila_idx = int(y_centro // tamano_casilla)

        if not juego_con_blancas:
            columna_idx = 7 - columna_idx
            fila_idx = 7 - fila_idx

        if 0 <= fila_idx < 8 and 0 <= columna_idx < 8:
            if tablero_virtual[fila_idx][columna_idx] == "":
                # Asignación directa de la letra
                tablero_virtual[fila_idx][columna_idx] = nombre_clase

    # 3. Ensamblar FEN
    lineas_fen = []
    for fila in tablero_virtual:
        espacios_vacios = 0
        fila_texto = ""
        for casilla in fila:
            if casilla == "":
                espacios_vacios += 1
            else:
                if espacios_vacios > 0:
                    fila_texto += str(espacios_vacios)
                    espacios_vacios = 0
                fila_texto += casilla
        if espacios_vacios > 0:
            fila_texto += str(espacios_vacios)
        lineas_fen.append(fila_texto)

    cadena_base = "/".join(lineas_fen)
    
    # 4. CORRECCIÓN DE ESTADO Y ENROQUES
    # Dinámico: 'w' si juegas con blancas, 'b' si juegas con negras
    turno = "w" if juego_con_blancas else "b"
    # '- -' significa que ya no hay enroques disponibles, para evitar errores en el endgame
    cadena_fen_final = f"{cadena_base} {turno} - - 0 1"
    
    return cadena_fen_final