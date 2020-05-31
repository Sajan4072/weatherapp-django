import requests
from django.shortcuts import render


def index(request):

    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=41cf57a23a0785ed1c0f028ac06962d9'
    place='Las Vegas'
    
    res=requests.get(url.format(place)).json()

    cweather={
            'city' : place,
            'temperature' : res['main']['temp'],
            'description' : res['weather'][0]['description'],
            'icon' : res['weather'][0]['icon'],
    }
    print(cweather)

    context={'cweather':cweather}
    
    return render (request,'landing.html'context)
