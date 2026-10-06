import requests

def obtener_clima(latitud, longitud):
    url = "https://api.open-meteo.com/v1/forecast"
    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "current": "temperature_2m,wind_speed_10m",
    }
    r = requests.get(url, params=parametros, timeout=10)
    r.raise_for_status()
    datos = r.json()["current"]
    return {"temperatura": datos["temperature_2m"], "viento": datos["wind_speed_10m"]}

ciudades = {
    "Querétaro": (20.59, -100.39),
    "CDMX": (19.43, -99.13),
    "Guadalajara": (20.67, -103.35),
}

print("Ciudad       Temp (°C)  Viento (km/h)")
for nombre, (lat, lon) in ciudades.items():
    clima = obtener_clima(lat, lon)
    print(f"{nombre:<12} {clima['temperatura']:<10} {clima['viento']}")