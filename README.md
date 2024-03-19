Proyecto diabetes

Abstract
La diabetes diabetes mellitus es una enfermedad crónica que se presenta cuando el páncreas no secreta suficiente insulina o cuando el organismo no utiliza eficazmente la insulina que produce. La insulina es una hormona que regula la concentración de glucosa en la sangre, es decir, la glucemia. Un efecto común de la diabetes no controlada es la hiperglucemia (es decir, la glucemia elevada) que, con el tiempo daña gravemente muchos órganos y sistemas del organismo, sobre todo los nervios y los vasos sanguíneos.

En 2014, el 8,5% de los mayores de 18 años padecían diabetes. En 2019, esta afección fue la causa directa de 1,5 millones de defunciones y, de todos los fallecidos por diabetes, el 48% tenía menos de 70 años. Además, otras 460 000 personas fallecieron a causa de la nefropatía diabética, y la hiperglucemia ocasiona alrededor del 20% de las defunciones por causa cardiovascular (1).

Entre 2000 y 2019, las tasas de mortalidad por diabetes normalizadas por edades aumentaron en un 3%. En los países ingresos medianos o bajos, la tasa de mortalidad por diabetes aumentó en un 13%.

En cambio, entre 2000 y 2019, la probabilidad de fallecer entre los 30 y los 70 años de edad por alguna de las cuatro principales enfermedades no transmisibles (enfermedades cardiovasculares, cáncer, enfermedades respiratorias crónicas o diabetes) se redujo en un 22% a escala mundial. https://www.who.int/es/news-room/fact-sheets/detail/diabetes

Realizamos el análisis de 100.000 muestras de pacientes hasta los 80 años y analizamos la probabilidad de sufrir diabetes según las variables de hipertensión, problemas cardiovasculares, histórico fumando, índice corporal, nivel de HbA1c y glucosa en sangre.

Queremos saber cuáles son las variables que más nos afectan a la hora de sufrir esta enfermedad.

Qué variables son las preponderantes en el riesgo de tener diabetes?
Qué probabilidad tiene un paciente de sufrir diabetes teniendo en cuenta las variables menos fuertes?
Finalmente analizaremos un algoritmo de Machine learning que mejor nos prediga esta condición.

En este repositorio podemos encontrar:
  - Proyecto final Ciencia de Datos_FedraAmeneiro.ipynb: notebook en Colab con el analisis de los datos utilizados, la comparación entre el uso de varios algoritmos de machine learning y el entrenamiento del elegido por su mejor performance.
  - Proyecto final Ciencia de Datos_FedraAmeneiro_api_backend.ipynb: notebook en Colab con el entrenamiento del algoritmo exclusivamente para su uso en la api
  - a.py: aplicacion codificada en python para la interacción con el usuario. Este puede meter los datos del paciente y le devuelve si el paciente es o no diabetico según el modelo entrenado.
  - requirements.txt: librerías requeridas
  - modelo.h5: modelo descargado para su uso en la api
