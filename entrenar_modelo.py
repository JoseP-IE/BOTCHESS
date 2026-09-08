from ultralytics import YOLO

def iniciar_entrenamiento():
    print("Iniciando entrenamiento del modelo visual...")
    
    # Dado que tu dataset dice "yolov8-obb" (Oriented Bounding Boxes),
    # cargamos el modelo base nano específico para cajas orientadas.
    modelo = YOLO("yolov8n-obb.pt") 
    
    # ==========================================
    # CONFIGURACIÓN DEL ENTRENAMIENTO
    # ==========================================
    resultados = modelo.train(
        data="chess seg.v4i.yolov8-obb/data.yaml", 
        epochs=100,       
        imgsz=640,       
        batch=16,        
        device='cpu',        
        plots=True       
    )
    
    print("¡Entrenamiento finalizado exitosamente!")

# Este bloque es obligatorio en Windows para evitar errores al usar múltiples núcleos
if __name__ == '__main__':
    iniciar_entrenamiento()