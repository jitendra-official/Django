from django.shortcuts import render,HttpResponse
from m1.form import creat_form


# Create your views here.
def index(req):
    if req.method == 'POST':
        s = creat_form(req.POST)
        if s.is_valid():
            s.save()
            return HttpResponse('<h1>Data submitted.</h1>')
    else:    
        s = creat_form()
    return render(req,'index.html',{'s':s})
