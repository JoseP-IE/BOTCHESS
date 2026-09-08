import requests

def consultar_agente_roma(tasa_esperada, tasa_actual):
    """
    Envía los datos de rendimiento al LLM local (qwen2.5-coder) 
    para obtener un diagnóstico de ingeniería industrial.
    """
    url_ollama = "http://localhost:11434/api/generate"
    
    prompt_operativo = f"""
    Eres ROMA, un agente supervisor de ingeniería industrial experto en la Teoría de Restricciones (La Meta).
    Estás monitoreando una línea de empaque agroindustrial en Sinaloa.
    
    Estado actual:
    - Flujo esperado: {tasa_esperada} productos por minuto.
    - Flujo real detectado: {tasa_actual} productos por minuto.
    
    El flujo real ha caído peligrosamente. En máximo 2 oraciones, diagnostica el problema como un cuello de botella e indica al operador una acción inmediata para revisar la línea. Sé directo y profesional.
    """

    payload = {
        "model": "qwen2.5-coder:7b",
        "prompt": prompt_operativo,
        "stream": False 
    }

    try:
        respuesta = requests.post(url_ollama, json=payload)
        respuesta.raise_for_status()
        texto_alerta = respuesta.json()["response"]
        return texto_alerta
    except requests.exceptions.RequestException:
        return "Error de conexión. Verifique que Ollama esté en ejecución."

if __name__ == "__main__":
    print("Consultando al Agente ROMA...")
    # Simulamos una caída de flujo para probar la reacción del modelo
    alerta = consultar_agente_roma(tasa_esperada=60, tasa_actual=15)
    print("\n[ALERTA EN PANTALLA PARA EL OPERADOR]:")
    print(alerta)