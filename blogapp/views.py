from django.shortcuts import render
from django.http import HttpResponse
from .models import blogtable

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'BLOGS'})
    
def allblogs(request):
    if request.method=='POST':
        Name=str(request.POST["nameinput"])
        blog=str(request.POST["bloginput"])
        if Name!="" and blog!="":
            variable=blogtable(name=Name, blogcontent=blog)
            variable.save()

        content=blogtable.objects.all()
        return render(request, "allblogs.html", {"allblog":content})
