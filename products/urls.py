from django.urls import path
from . import views

# URLConf
urlpatterns = [
    # path('products/hello', views.say_hello)
    path('hello/', views.say_hello)
]
