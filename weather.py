import pyowm

owm = pyowm.OWM('2a62786782ef789a0ca6137cd3f912ef')

def get_weather():
	observation = owm.weather_at_coords(12.824732, 80.045154)
	weather = observation.get_weather()
	return weather

def get_temperature():
	weather = get_weather()
	return (weather.get_temperature('celsius')['temp'], weather.get_humidity())


