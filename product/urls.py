from django.urls import path
from . import views
app_name = 'product'

urlpatterns = [

    path('' , views.list , name='list'),
    path('detail/<int:pk>/' , views.detail , name='detail'),
    path('category/<int:pk>' , views.list_by_category , name='category'),
    path('collections/<int:pk>' , views.list_by_category , name='collections'),
    path('search/' , views.list_by_search , name='search'),
    path('detail/<int:pk>/likes' , views.likePost , name='like'),
    path('comments/' , views.addcomment , name='comments'),
    path('create/' , views.create_product , name='create'),
    path('delete/<int:pk>' , views.delete_product , name='delete'),
    path('edit/<int:pk>' , views.edit_product , name='edit'),
    

]