import requests
from django.shortcuts import render
from .models import Place
from .forms import PlaceForm

def index(request):


    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=41cf57a23a0785ed1c0f028ac06962d9'
    err_msg=''
    message=''
    message_class=''

    if request.method =='POST':
            form=PlaceForm(request.POST)
            

            if form.is_valid():
                    new_place=form.cleaned_data['name']
                    existing_pcount=Place.objects.filter(name=new_place).count()
                    if existing_pcount==0:
                            res=requests.get(url.format(new_place)).json()
                            if res['cod']==200:
                                    form.save()
                            else:
                                err_msg='no such place exist'
                            

                    else:
                        err_msg='Place already exist'  

            if err_msg:

                    message=err_msg
                    message_class='is-danger'
            else:
                    message='place added '
                    message_class='is-success'         
    
    print(err_msg)
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

    context={'w_data':w_data,
    'form':form,
    'message':message,
    'message_class':message_class,
    }
    return render(request,'landing.html',context)  
            

    
        
     
     
   
