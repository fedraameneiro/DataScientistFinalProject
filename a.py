import streamlit as st
import requests
import pandas as pd

Modelo, Preprocesador=load('algoritmo.joblib')


def main():
    st.title("Formulario de Datos del Paciente")

    # Recopilar datos del usuario
    age = st.slider("Edad", min_value=0, max_value=100, value=25)
    bmi = st.slider("BMI", min_value=10.0, max_value=40.0, value=20.0, step=0.1)
    hba1c_level = st.slider("Nivel de HbA1c", min_value=4.0, max_value=10.0, value=5.0, step=0.1)
    blood_glucose_level = st.slider("Nivel de Glucosa en Sangre", min_value=70, max_value=300, value=100)

    # Crear un array llamado 'paciente' con los datos recopilados
    paciente = [age, bmi, hba1c_level, blood_glucose_level]

    # Mostrar los datos del paciente en la interfaz de usuario
    st.write("Datos del Paciente:", paciente)

    # Llamar al modelo de machine learning
    resultado_prediccion = predecir_con_modelo(valor_glucosa, valor_bmi, valor_edad, valorHbA1c)

    # Mostrar el resultado de la predicción
    st.write("Resultado de la Predicción:", resultado_prediccion)

def predecir_con_modelo(valor_glucosa, valor_bmi, valor_edad, valorHbA1c):
    # URL del modelo en GitHub
    url_modelo = "https://raw.githubusercontent.com/tu_usuario/tu_repositorio/ruta/a/tu/modelo/modelo.pkl"

    # Realizar una solicitud HTTP para obtener el modelo
    response = requests.get(url_modelo)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Cargar el modelo desde el contenido de la respuesta
        modelo = cargar_modelo_desde_bytes(response.content)

        # Realizar la predicción
        resultado_prediccion = modelo.predict([valor_glucosa, valor_bmi, valor_edad, valorHbA1c])

        # Devolver el resultado de la predicción
        return resultado_prediccion[0]

    else:
        st.error(f"No se pudo obtener el modelo. Código de estado: {response.status_code}")
        return None

def cargar_modelo_desde_bytes(modelo_bytes):
    # Esta función debe ser implementada según la forma en que guardaste tu modelo.
    # Puedes usar pickle, joblib, o cualquier otro formato de serialización.
    # Aquí, como ejemplo, se asume que se utiliza pickle.
    import pickle
    modelo = pickle.loads(modelo_bytes)
    return modelo

if __name__ == "__main__":
    main()
