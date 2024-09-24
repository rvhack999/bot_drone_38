import requests as rq
import os
from dotenv import load_dotenv
import json
import matplotlib
import matplotlib.pyplot as plt
from random import randint


lat: str = None
lon: str = None
lat_example = 52.915541
lon_example = 103.571139
load_dotenv()
API_key = os.getenv("API_KEY")
#url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat_example}&lon={lon_example}&appid={API_key}"
url = "https://api.open-meteo.com/v1/forecast"
params = {
        "latitude": float(lat_example),
        "longitude": float(lon_example),
        "hourly": ["temperature_2m", "precipitation", "wind_speed_10m", "wind_speed_80m", "wind_speed_120m",
                   "wind_speed_180m", "wind_gusts_10m", "temperature_80m", "temperature_120m", "temperature_180m"],
        "wind_speed_unit": "ms",
        "forecast_days": 1,
        "timezone": 'Asia/Irkutsk'
    }

request = rq.get(url, params)
data = request.json()


date = data['hourly']['time'][0][:-6]
time = [i[-5:] for i in data['hourly']['time']]
print(date)
print(time)
x = [1, 2, 3, 4, 5]
y = [25, 32, 34, 20, 25]
matplotlib.use('Qt5Agg')
plt.plot(x, y)
plt.xlabel('Ось х') #Подпись для оси х
plt.ylabel('Ось y') #Подпись для оси y
plt.title('Первый график') #Название
plt.show()