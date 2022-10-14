from itertools import product
from django.urls import path
from . import views
app_name = 'cart'



urlpatterns = [
    path('add/<int:pk>' , views.add , name='add'),   
    path('reduce/<int:pk>' , views.reduce , name='reduce'),
    path('delete/<int:pk>' , views.delete , name='delete'),
    path('checkout/<int:pk>' , views.checkout , name='checkout'),
]