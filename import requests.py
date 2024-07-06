import requests
import json

# Sustituye con tu propio token y el ID de la base de datos
token = 'secret_gvVhYzOY3VNzNvlBhXu2RACrJcv9QYNB7kSLWzVRJtJ'
database_id = '3ebb2b66e34747f8b7fd5294e9e51bd2'

# Configuración del encabezado de la solicitud
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Realizar la solicitud POST a la base de datos de Notion
url = f'https://api.notion.com/v1/databases/{database_id}/query'
response = requests.post(url, headers=headers)

if response.status_code == 200:
    print('Conectado a la API de Notion')
    data = response.json()
    
    # Aquí puedes adaptar los datos obtenidos según la estructura de tu base de datos
    for result in data['results']:
        properties = result['properties']
        nombre_proyecto = properties['Nombre del proyecto']['title'][0]['text']['content']
        colaborador = properties['Colaborador']['rich_text'][0]['text']['content']
        estado = properties['Estado']['select']['name']
        fecha_entrega = properties['Entrega']['date']['start']
        avance = properties['Avance']['formula']['number']
        
        proyecto = {
            'nombre_proyecto': nombre_proyecto,
            'colaborador': colaborador,
            'estado': estado,
            'fecha_entrega': fecha_entrega,
            'avance': avance
        }
        
        print(proyecto)

else:
    print(f'No se pudo conectar a la API de Notion. Código de respuesta: {response.status_code}')
    print('Contenido de la respuesta:', response.text)
