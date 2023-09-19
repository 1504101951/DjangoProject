from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator


# Create your views here.

class HelloWorld(APIView):
    def get(self, request):
        return Response("Hello")    

    def post(self, data):
        return Response("Hello")
