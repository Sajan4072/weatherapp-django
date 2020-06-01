import requests
from django.shortcuts import render
from .models import Place
from .forms import PlaceForm

def index(request):


    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=41cf57a23a0785ed1c0f028ac06962d9'

    if request.method =='POST':
            form=PlaceForm(request.POST)
            form.save()
    

    form=PlaceForm()
    cities=Place.objects.all()
    w_data=[]

    for place in cities:
        res=requests.get(url.format(place)).json()

        cweather={
              'city' : place.name,
              'temperature' : res['main']['temp'],
               'description' : res['weather'][0]['description'],
               'icon' : res['weather'][0]['icon'],
        }
        w_data.append(cweather)
    
    print(w_data) 

    context={'w_data':w_data,'form':form}
    return render(request,'landing.html',context)  
            

    
        
     
     
   
