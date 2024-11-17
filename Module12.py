#1

import requests
import json


request = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(request).json()
    print(response["value"])
except:
    print("Error")



#2

import requests
import json


keyword = input("Enter the Municipality: ")
request = "https://api.openweathermap.org/data/2.5/weather?q="+keyword+"&APPID=f3030340c8d510be07322b293eecbb5f"
response = requests.get(request).json()
print("Description",response["weather"][0]['description'],sep=":")
for i in response['main']:
    temp=["temp","feels_like","temp_min","temp_max"]
    if i in temp:
        print(i, response['main'][i], sep=":", end="")
        print("°F")
    else:
        print(i, response['main'][i], sep=":",)