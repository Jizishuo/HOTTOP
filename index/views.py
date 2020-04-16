from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView
import json
from django.core.cache import cache
from until.sprider import *

class Index(APIView):

    def get(self,request, *args, **kwargs):
        data = {}
        data['1'] = {'www.v2ex.com': "/type/V2EX/1"}
        data['2'] = {'next': "....."}

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

            if type_in == 'v2ex':
                data['type'] = 'V2EX'
                V2EX_mes = cache.get('V2EX')
                if V2EX_mes is None or V2EX_mes == []:
                    V2EX_mes = GET_v2ex()
                    cache.set('V2EX', V2EX_mes, 60*5)  # 缓存5分钟
                data['mes'] = V2EX_mes


            if type_in == 'ithome':
                data['type'] = 'ithome'
                ithome_mes = cache.get('ithome')
                if ithome_mes is None or ithome_mes == []:
                    ithome_mes = GET_ithome()
                    cache.set('ithome', ithome_mes, 60 * 5)  # 缓存5分钟

                data['mes'] = ithome_mes


            if type_in == 'zhihu':
                data['type'] = 'zhihu'
                zhihu_mes = cache.get('zhihu')
                if zhihu_mes is None or zhihu_mes == []:
                    zhihu_mes = GET_zhihu()
                    cache.set('zhihu', zhihu_mes, 60 * 5)  # 缓存5分钟

                data['mes'] = zhihu_mes

            if type_in == 'weibo':
                data['type'] = 'weibo'
                weibo_mes = cache.get('weibo')
                if weibo_mes is None or weibo_mes == []:
                    weibo_mes = GET_weibo()
                    cache.set('weibo', weibo_mes, 60 * 5)  # 缓存5分钟

                data['mes'] = weibo_mes

            if type_in == 'tieba':
                data['type'] = 'tieba'
                tieba_mes = cache.get('tieba')
                if tieba_mes is None or tieba_mes == []:
                    tieba_mes = Get_tieba()
                    cache.set('tieba', tieba_mes, 60 * 5)  # 缓存5分钟

                data['mes'] = tieba_mes

            return HttpResponse(json.dumps(data), status=201)

            # return JsonResponse(data)

    def post(self,request, *args, **kwargs):
        pass

    def put(self,request, *args, **kwargs):
        pass

    def delete(self,request, *args, **kwargs):
        pass
