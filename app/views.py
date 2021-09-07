from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
import cv2
# Create your views here.

#objects.all() list data
#get => request.GET.get(field)
#post => formularios

def Index(request):
    return render(request,"index.html",{'title':'File Image'})

def Pruebota(request):
     return JsonResponse({"saludo":"django with cv"})

def Prueba(request):
    if request.is_ajax and request.method == "GET":
        nombre = request.GET.get("nombre",None)
        return JsonResponse({"prueba":nombre})
    # class ChangeImage(View):
#     template_name="index.html"
#     def post(self,request):
#         title="recognize"
