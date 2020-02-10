from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView
import json
from django.core.cache import cache
from until.sprider import *

class Index(APIView):

    def get(self,request, *args, **kwargs):
        data = {}
        data['count'] = '123'
        data['dog'] = 'dog'

        return JsonResponse(data)

    def post(self,request, *args, **kwargs):
        pass

    def put(self,request, *args, **kwargs):
        pass

    def delete(self,request, *args, **kwargs):
        pass


class Sprider_type(APIView):


    def get(self,request, *args, **kwargs):
        data = {}
        if 'type' in kwargs and 'type_id' in kwargs:
            type_in = kwargs['type']
            type_id = kwargs['type_id']

            if type_in == 'V2EX':
                data['type'] = 'V2EX'
                V2EX_mes = cache.get('V2EX')
                if V2EX_mes is None:
                    V2EX_mes = get_V2EX()
                    cache.set('V2EX', V2EX_mes, 60*5)  # 缓存5分钟
                data['mes'] = V2EX_mes

            return HttpResponse(json.dumps(data), status=201)

            # return JsonResponse(data)

    def post(self,request, *args, **kwargs):
        pass

    def put(self,request, *args, **kwargs):
        pass

    def delete(self,request, *args, **kwargs):
        pass
