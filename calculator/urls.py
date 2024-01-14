from django.urls import path
from .views import add_numbers, result_page

urlpatterns = [
    path('', add_numbers, name='add_numbers'),
    path('result/<int:result>/', result_page, name='result'),
    #path('', views.add_numbers, name='add_numbers'),
]
