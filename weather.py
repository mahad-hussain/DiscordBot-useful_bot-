import requests

api_key = "7d1b9310cdeaaf8491a666e3a476dee5"


"""
Returns the weather of a city by accessing information from the openweathermap API
@param city (str): The name of the city thats information is wanted
"""
def weathercity(city):
    
    #request from the API
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}")
    
    #checks the status of the request, if bad then returns No City Found
    if weather_data.json()['cod'] == '400' or weather_data.json()['cod'] == '404':
        return("No City Found")
    

    #gets all relevant information from the json
    weather = (weather_data.json()['weather'][0]['main'])
    temp = (weather_data.json()['main']['temp'])
    feels_like = (weather_data.json()['main']['feels_like'])
    wind = (weather_data.json()['wind']['speed'])
    humidity = (weather_data.json()['main']['humidity'])

    wind = round(wind*3.6, 2)

    #gets the weather based on geolocation
    """
    city_data = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={city}&units=imperial&appid={api_key}")
        

    city_lat = (city_data.json()[0]['lat'])

    city_lon = (city_data.json()[0]['lon'])

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={city_lat}&lon={city_lon}&units=metric&appid={api_key}")
    """


    return(f"""The weather in {city} is: {weather} and the temperature is: {temp} Celsius,
It feels like: {feels_like} Celsius and the wind is at: {wind}km/h with a humidty of {humidity}%""")
