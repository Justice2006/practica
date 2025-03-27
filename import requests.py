import requests

# Configuración inicial
jenkins_url = "http://localhost:8080/job/NombreDe1Job/build"
username = "Lucio"
api_token = "119e02c42ad4d41a1e7cba624d5bd86b01"

try:
    # Disparar un job en Jenkins
    response = requests.post(jenkins_url, auth=(username, api_token))
    if response.status_code == 201:
        print("Job disparado exitosamente.")
    else:
        print(f"Error al disparar el job. Código de estado: {response.status_code}")
except Exception as e:
    print(f"Ocurrió un error: {e}")