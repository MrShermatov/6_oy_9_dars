from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from .models import Cars, Models
from .forms import CarForm, ModelForm




def index(request: HttpRequest):
    cars = Cars.objects.all()
    models = Models.objects.all()

    context = {
        'cars': cars,
        'models': models,
        'title': "Mr_Mers"
    }

    return render(request, 'main/index.html', context)

def car_detail(request: HttpRequest, car_id: int):
    car = get_object_or_404(Cars, id=car_id)
    models = Models.objects.all()


    context = {
        'models': models,
        'car': car,
        'title': car.car_name
    }
    return render(request, 'main/car_detail.html', context)

def get_car_by_model(request: HttpRequest, model_id: int):
    model = get_object_or_404(Models, id=model_id)
    models = Models.objects.all()
    cars = Cars.objects.filter(car_model=model)

    context = {
        'model': model,
        'models': models,
        'cars': cars,
        'model_name': model.model_name
    }

    return render(request, 'main/get_car_company.html', context)

def add_car(request: HttpRequest):
    if request.method == 'POST':
        form = CarForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            car = form.save()
            return redirect('car_detail', car_id=car.id)

    form = CarForm()
    models = Models.objects.all()

    context = {
        'form': form,
        'models': models,
        'title': "Mashina qo'shish"
    }
    return render(request, 'main/add_car.html', context)

def add_model(request: HttpRequest):
    if request.method == 'POST':
        form = ModelForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')

    form = ModelForm()

    context = {
        'form': form
    }

    return render(request, 'main/add_model.html', context)
