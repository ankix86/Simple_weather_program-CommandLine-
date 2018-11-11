import requests
#install requests using cmd or powershell
#-------------------INSTALL------------------#

city = input("enter your city :")
api_key = "****" #use your openweathermap API_Key 

url = " http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city,api_key)

#simply use for getting url with formated foam with program data like API-keys or City name
#you want more detail about request.get(url) check out = "http://docs.python-requests.org/en/master/user/quickstart/"
res = requests.get(url) 

#get json formated data from the result
data = res.json() 

#try to use "print(data)" you can understad that thing easily

#store json formated data in single variable check out json_formated_example.json file 
country = data['sys']['country'] 
temp = data['main']['temp']
min_temp = data['main']['temp_min']
max_temp = data['main']['temp_max']
wind_speed = data['wind']['speed']
latitude = data['coord']['lat']
longitude = data['coord']['lon']
description = data['weather'][0]['description']

#print output of variable print command
print('city :{},{}'.format(city,country))
print('temperature :{} degree celcius'.format(temp))
print('min_temperature :{} degree celcius'.format(min_temp))
print('max_temperature :{} degree celcius'.format(max_temp))
print('wind_speed :{} m/s'.format(wind_speed))
print('latitude :{}'.format(latitude))
print('longitude :{}'.format(longitude))
print('description :{}'.format(description))
