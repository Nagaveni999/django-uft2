from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

import json
import requests

def home(request):

        response=requests.get("https://unitforce.talentrecruit.com/API/SearchJobs?")
        da=response.json()
        da=da["Details"]
        return render(request,'navbar_page1.html',{"da":da})
        
    
def index(request):
        response=requests.get("https://unitforce.talentrecruit.com/API/SearchJobs?")
        da=response.json()
        da=da["Details"]
        return render(request,'index.html',{"da":da})
        

def search(request):

    if request.GET.get('q'):
        job =request.GET['q']
        response=requests.get("https://unitforce.talentrecruit.com/API/SearchJobs?Keyword="+"?"+job)
        da=response.json()
        da=da["Details"]
        return render(request,'indextable2.html',{"da":da})

    else:
        response=requests.get("https://unitforce.talentrecruit.com/API/SearchJobs?")
        da=response.json()
        da=da["Details"]
        
        
        return render(request,'indextable2.html',{"da":da})

def apply(request):
    
    return render(request,'indextable2.html')

def about(request):
   return render(request, "navbar_page1.html")



    
    
    















#my code 
#def home1():
    #return HttpResponse('<h1>blog about by nags 02 <h1>')
    #return render(request,'index.html')

    #job="ui developer"
    #response=requests.get("https://unitforce.talentrecruit.com/API/SearchJobs?Keyword="+"?"+job)
    #da=response.json()
    #da1=da['Details']
    #return da1

#var=home()
#print(var)

