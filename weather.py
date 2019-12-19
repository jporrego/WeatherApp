import requests, json

api_key = "4dcff09dee99876a903ebfe4277effa9"
base_url = "https://api.openweathermap.org/data/2.5/weather?"


def get_weather_info():
    
    user_info = (requests.get("https://ipinfo.io/json")).json()

    city = user_info["city"]
    country = user_info["country"]
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "," + country
    try:
        x = requests.get(complete_url)
        x = x.json()
        current_temp = int(int(x["main"]["temp"]) -272.15)
        curren_skies = x["weather"][0]["description"]
    except:
        return "Couldn't get weather info"
    
    return f"{current_temp}°C with {curren_skies} in {city}."


print(get_weather_info()) 






