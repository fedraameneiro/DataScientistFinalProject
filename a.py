




# Crear un array llamado 'paciente' con los datos recopilados
    paciente = [valor_edad, valor_bmi, valorHbA1c, valor_glucosa]

    # Mostrar los datos del paciente en la interfaz de usuario
    st.write("Datos del Paciente:", paciente)
    
    paciente= np.array([[valor_edad, valor_bmi, valorHbA1c, valor_glucosa]])
    scaler = StandardScaler()
    paciente = scaler.fit_transform(paciente)
    nuevos_datos_scaled = scaler.transform(paciente)

    resultado_prediccion = modelo.predict(nuevos_datos_scaled)

  
