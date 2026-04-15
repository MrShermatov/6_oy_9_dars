from django.urls import path
from .views import (index, car_detail, get_car_by_model, add_car, add_model,
                    delete_car, update_car, update_model, delete_model)

urlpatterns = [
    path('', index, name='index'),
    path('car_detail/<int:car_id>/', car_detail, name='car_detail'),
    path('car_by_model/<int:model_id>/', get_car_by_model, name='car_by_model'),
    path('car/add/', add_car, name='add_car'),
    path('car/<int:car_id>/update/', update_car, name='update_car'),
    path('car_delete/<int:car_id>/', delete_car, name='delete_car'),
    path('model/add/', add_model, name='add_model'),
    path('model/<int:model_id>/update/', update_model, name='update_model'),
    path('model/<int:model_id>/delete/', delete_model, name='delete_model'),
]