from django.urls import path
from .views import *

urlpatterns = [
    path('', getData, name='getData'),
    path('video/', getVideo, name='getvideo'),
    # path('flight', getFlight, name='getflight'),
    path('post/', getPost, name="getPost"),
    path('update/<str:pk>', updatePost, name='updatePost'),
    path('videos/', querySet, name='querySet'),
]