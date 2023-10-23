from django.http import HttpResponse
from django.views import View

class MiVista(View):
    def get(self, request):
        return HttpResponse("¡Hola! Estás haciendo una solicitud del tipo GET")
    
    def post(self,request):
        return HttpResponse("¡Hola! Estás haciendo una solicitud del tipo POST")