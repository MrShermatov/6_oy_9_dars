from django.urls import path
from .views import index, car_detail, get_car_by_model, add_car, add_model
urlpatterns = [
    path('', index, name='index'),
    path('car_detail/<int:car_id>/', car_detail, name='car_detail'),
    path('car_by_model/<int:model_id>/', get_car_by_model, name='car_by_model'),
    path('car/add/', add_car, name='add_car'),
    path('model/add/', add_model, name='add_model' )
]