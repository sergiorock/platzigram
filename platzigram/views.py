# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))


def sort_integers(request):
    # List comprenhension - Dentro de la sintaxis de una lista se puede escribir la lógica de una línea en un for
    # y nos regresa esa lista
    # Recorre la lista de numbers y convierte cada string en un int 
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    # Ordeno los enteros en una variable nueva, porque las listas son inmutables
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted succesfully.'
    }

    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
    )

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}!, welcome to Platzigram'.format(name)
    
    return HttpResponse(message)
