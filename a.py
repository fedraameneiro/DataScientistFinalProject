import streamlit as st
import requests
import pandas as pd



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
   # resultado_prediccion = predecir_con_modelo(valor_glucosa, valor_bmi, valor_edad, valorHbA1c)

    # Mostrar el resultado de la predicción
    #st.write("Resultado de la Predicción:", resultado_prediccion)



    main()
