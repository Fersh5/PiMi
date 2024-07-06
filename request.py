import requests

response = requests.get(f'https://pekeapi.co/api/v2/pokemon/1')
if response.status_code == 200:
    print('Se conecto ala PokeAPI:')