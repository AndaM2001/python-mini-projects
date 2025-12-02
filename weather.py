import requests

latitude = 59.33   # Stockholm
longitude = 18.07

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

response = requests.get(url)
data = response.json()

weather = data["current_weather"]
temp = weather["temperature"]
windspeed = weather["windspeed"]
condition = weather["weathercode"]

print(f"Stockholm Weather:")
print(f"Temperature: {temp}°C")
print(f"Wind: {windspeed} m/s")
print(f"Weather Code: {condition}")
