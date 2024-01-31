# data_visualization_app/views.py

from django.shortcuts import render, redirect
from .models import EnvironmentalData, SocialData
from .forms import EnvironmentalDataForm, SocialDataForm
from django.http import JsonResponse
from .models import EnvironmentalData

def get_environmental_data(request):
    data = list(EnvironmentalData.objects.values())
    return JsonResponse(data, safe=False)

def index(request):
    environmental_data = EnvironmentalData.objects.all()
    social_data = SocialData.objects.all()
    return render(request, 'index.html', {'environmental_data': environmental_data, 'social_data': social_data})

def add_environmental_data(request):
    if request.method == 'POST':
        form = EnvironmentalDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EnvironmentalDataForm()
    return render(request, 'form.html', {'form': form})

def add_social_data(request):
    if request.method == 'POST':
        form = SocialDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SocialDataForm()
    return render(request, 'form.html', {'form': form})
