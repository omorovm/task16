from django.urls import path
from .views import *

urlpatterns = [
    path('get/', get_triangles),
    path('create/', create_triangle),
    path('perimeter/<int:pk>/', get_perimeter),
    path('update/<int:pk>/', update_triangle),
    path('delete/<int:pk>/', delete_triangle),
]