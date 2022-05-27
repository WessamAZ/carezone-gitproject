from django.urls import path
from . import views
urlpatterns = [
    path('' , views.cars , name = 'cars'),
    path('/<int:id>', views.car_detail, name='car_detail'),
    # id : is the id of car row in table in DB
    path('/search' , views.search , name = 'search'),
]
  