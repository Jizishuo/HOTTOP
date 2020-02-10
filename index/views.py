from django.shortcuts import render, HttpResponse
# from django.views import View
from django.http import JsonResponse
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
import json


class Index(APIView):


    def get(self,request, *args, **kwargs):
        data = {}
        data['count'] = '123'
        data['dog'] = 'dog'

        # return HttpResponse(json.dumps(data), status=201)

        return JsonResponse(data)

    def post(self,request, *args, **kwargs):
        pass

    def put(self,request, *args, **kwargs):
        pass

    def delete(self,request, *args, **kwargs):
        pass
