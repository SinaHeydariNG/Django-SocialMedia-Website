from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    path('' , views.profile , name='profile'),  
    path('login/' , views.login , name='login'),
    path('register/' , views.register , name='register'),
    path('lgoout/' , views.logout , name='logout'),
    path('users/<int:pk>' , views.user_profile , name='user_profile'),
    path('following/<int:pk>' , views.followToggle , name='following')

]