import requests
response = requests.get(
  'https://api.restcountries.com/countries/v5?q=canada',
  headers={'Authorization': 'Bearer rc_live_8793482b759a4c9697862f01b188a7d7'}
)
data = response.json()
print(f"Nombre comun: {data["data"]["objects"][0]["names"]["common"]}")
print(f"Nombre Oficial: {data["data"]["objects"][0]["names"]["official"]}")
print(f"Descripcion: {data["data"]["objects"][0]["flag"]["description"]}")