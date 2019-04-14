from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index_page'),
    path('details/', views.details, name='details_page')
]
