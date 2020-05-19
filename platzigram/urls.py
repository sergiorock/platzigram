from django.urls import path
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello World!')


urlpatterns = [
    path('hello-world/', hello_world)
]