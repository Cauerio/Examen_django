from django.db import models

'''El DNI tengo establecido como "unique" para que no se pueda introducir un mismo DNI otra vez,
y el max_length para que no se pueda poner un DNI con más de 9 caracteres. 
El numero_socio puse como AutoField para que se auto rellene y como primary_key'''
class Socios(models.Model):
    DNI= models.CharField(unique=True, max_length=9)
    numero_socio= models.AutoField(primary_key=True)
    password= models.CharField() 
