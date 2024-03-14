import streamlit as st
import requests
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def main():
    st.title("Formulario de Datos del Paciente")

    # Recopilar datos del usuario
    valor_edad = st.slider("Edad", min_value=0, max_value=100, value=25)
    valor_bmi = st.slider("BMI", min_value=10.0, max_value=40.0, value=20.0, step=0.1)
    valorHbA1c = st.slider("Nivel de HbA1c", min_value=4.0, max_value=10.0, value=5.0, step=0.1)
    valor_glucosa = st.slider("Nivel de Glucosa en Sangre", min_value=70, max_value=300, value=100)
  
    # Crear un array llamado 'paciente' con los datos recopilados
    paciente = [valor_edad, valor_bmi, valorHbA1c, valor_glucosa]

    # Mostrar los datos del paciente en la interfaz de usuario
    st.write("Datos del Paciente:", paciente)

    # Llamar al modelo de machine learning
    resultado_prediccion = predecir_con_modelo(valor_glucosa, valor_bmi, valor_edad, valorHbA1c)

    # Mostrar el resultado de la predicción
    st.write("Resultado de la Predicción:", resultado_prediccion)

#preprocesamos las variables que tomamos
def cargar_modelo_desde_bytes(modelo_bytes):
    # Esta función debe ser implementada según la forma en que guardaste tu modelo.
    # Puedes usar pickle, joblib, o cualquier otro formato de serialización.
    # Aquí, como ejemplo, se asume que se utiliza pickle.
    import pickle
    modelo = pickle.loads(modelo_bytes)
    return modelo


#llamamos a nuestro modelo de predicción    
def predecir_con_modelo(valor_glucosa, valor_bmi, valor_edad, valorHbA1c):
    # URL del modelo en GitHub
    url_modelo_entrenamiento = "https://raw.githubusercontent.com/fedraameneiro/DataScientistFinalProject/main/Proyecto_final_Ciencia_de_Datos_FedraAmeneiro_api_backend.ipynb"

    # Realizar una solicitud HTTP para entrenar el modelo
    #response 1, ok. response 0 not ok
    response = requests.get(url_modelo_entrenamiento)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Cargar el modelo desde el contenido de la respuesta
        modelo = cargar_modelo_desde_bytes(response.content)

        # Realizar la predicción
       
        paciente= np.array([[valor_edad, valor_bmi, valorHbA1c, valor_glucosa]])
        scaler = StandardScaler()
        paciente = scaler.fit_transform(paciente)
        nuevos_datos_scaled = scaler.transform(paciente)

        resultado_prediccion = modelo.predict(nuevos_datos_scaled)

        # Convierte las probabilidades en predicciones binarias usando un umbral (por ejemplo, 0.5)
        prediccion_binaria =  (resultado_prediccion >= 0.5).astype(int)
        # Mapea las predicciones binarias a etiquetas más descriptivas
        resultado = "Diabetes" if prediccion_binaria[0] == 1 else "No Diabetes"
       
        # Devolver el resultado de la predicción
        return resultado

    else:
        st.error(f"No se pudo obtener el modelo. Código de estado: {response.status_code}")
        return None



main()
