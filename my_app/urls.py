from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('',views.book_list,name='book_list'),
    path('<int:id>/',views.book_detail,name='book_detail'),
]
