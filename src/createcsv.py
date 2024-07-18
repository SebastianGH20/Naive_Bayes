import pandas as pd
import requests

# URL del CSV
url = "https://raw.githubusercontent.com/4GeeksAcademy/naive-bayes-project-tutorial/main/playstore_reviews.csv"

# Hacer la solicitud usando requests con verificación SSL desactivada
response = requests.get(url, verify=False)

# Leer el contenido del CSV desde la respuesta
csv_content = response.content

# Guardar el contenido en un archivo CSV en la computadora
with open("playstore_reviews.csv", "wb") as file:
    file.write(csv_content)

print("Archivo CSV guardado como 'playstore_reviews.csv'")

















