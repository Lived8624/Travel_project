from django.http import HttpResponse
from django.shortcuts import render
from .models import place , emp


# def demo(request):
#     return HttpResponse("Hello world")

def demo(request):
    obj = place.objects.all()
    obj2=emp.objects.all()
    return render(request, "index.html", {'result': obj,'emp':obj2})

# def about(request):
#     return render(request, 'about.html')
#
#
# def contact(request):
#     return HttpResponse("contact page")
