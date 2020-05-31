import requests
from django.shortcuts import render


def index(request):

    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=41cf57a23a0785ed1c0f028ac06962d9'
    city='Las Vegas'
    res=requests.get(url.format(city))
    print(res.text)
    return render (request,'landing.html')
