from django.shortcuts import render, get_object_or_404
from .models import Stanowiska, Pracownicy

# Create your views here.

def homepage(request):
       pracownicy = Pracownicy.objects.all()
       p_count = Pracownicy.objects.count()
       data = {
            "pracownicy": pracownicy,
            "p_count": p_count
       }
       return render(request,'index.html',data)

def detail(request, id):
       pracownik = get_object_or_404(Pracownicy, pk=id)
       data = {
              "pracownik": pracownik
       }
       return render(request, "detail.html", data)