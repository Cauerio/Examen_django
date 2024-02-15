from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from .models import Socios
from django.views.decorators.csrf import csrf_exempt
import json

'''Esta parte introduce un nuevo socio a la base de datos.
Simplemente debes de añadir el DNI del socio y crear una password. Y el numero del socio se genera automaticamente'''
@csrf_exempt
def intro_socio(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        DNI = data.get('DNI')
        password = data.get('password')
        try:
            Socios.objects.create(DNI=DNI, password=password)
            return HttpResponse("Socio introducido")
        except:
            return HttpResponseBadRequest("Error al añadir el socio.")
    else:
        return HttpResponseBadRequest("Solo se acepta post.")
    

'''Esta parte cambia la contraseña del socio con un pequeño control de errores.
Filtra por DNI y hace el update solamente en la password.'''
@csrf_exempt
def chang_pass(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        DNI = data.get('DNI')
        password = data.get('password')
        try:
            Socios.objects.filter(DNI=DNI).update(password=password)
            return HttpResponse("La password ha cambiado")
        except Exception:
            return HttpResponseBadRequest("Fallo al cambiar la password")
    else:
        return HttpResponseBadRequest("Fallo")

'''Esta parte muestra los datos de los socios menos la contraseña.
En el "Socios.objects.values" solo pongo el DNI y el numero_socios para que simplemete me mostre eso '''
@csrf_exempt
def show_socios(request):
    data = Socios.objects.values('DNI', 'numero_socio' )
    return HttpResponse(data, content_type='application/json')


'''Cuenta la cantidad de socios que hay en la base de datos que has buscado'''
@csrf_exempt
def count_pass_iguales(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        password= data.get('password')
        try:
            posts = Socios.objects.filter(password=password).count()
            return JsonResponse({'count':posts})
        except Exception:
            return HttpResponse("Fallo al encontrar socio")
    else:
        return HttpResponse("Fallo")