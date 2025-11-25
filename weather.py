import requests

API_KEY = "590b7c76b9360953d9e9c99215450fd8"
city = "Accra"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
    print(f'The temperature is: {data.get("main").get("temp")}')
    print(f'Weather description: {data.get("weather")[0].get("description")}')
else:
    print("Error:", response.status_code)
