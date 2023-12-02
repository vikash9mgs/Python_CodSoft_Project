import requests

api_key = '3b56bacbaf4147c5109ded97f7a0bc6f'
user_input = input("Enter City: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp_f = round(weather_data.json()['main']['temp'])
    wind_mph = round(weather_data.json()['wind']['speed'])

    temp_c = (temp_f - 32) * 5 / 9
    wind_kmh = wind_mph * 1.60934

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp_c:.1f}ºC")
    print(f"The wind speed in {user_input} is: {wind_kmh:.1f} km/h")
